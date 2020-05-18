import sqlite3, math, js2py, os, requests, models.bloodBowl as models, datetime, crud, constants.emojis as emojis
class GoblinSpy:
    def __init__(self, goblin_token, crud):
        self.goblin_token = goblin_token
        self.crud = crud
    def __str__(self):
        return ('Discord Server: %s - League: %s - Tournament: %s - Goblin: %s' % (self.discord_id, self.league_name, self.tournament_name, self.goblin_token))
    def get_goblin_token(self, league, tournament):
        # Calculate the safe path from Goblin Spy using the same JavaScript script
        jsScripts = '''
            function(k){var j=this;var e=j.toUTF8Array(k);var g="ABCDEFGHIJKLMNOPQRSTUVWXYZ234567";var p="";var n=[0,0,0,0,0,0,0,0];for(var f=0;f<e.length;f+=5){var o=Math.min(e.length-f,5);n=e.slice(f,f+o);n.reverse();while(n.length<8){n.push(0)}n.reverse();for(var m=((o+1)*8)-5;m>3;m-=5){var d=Math.floor(m/8);var h=m-d*8;var b=n.slice(n.length-d-1,n.length-d-1+2);var c=b.length>1?(b[0]<<8)+b[1]:b[0]<<8;var a=(c>>h);var l=a&31;p+=g[l]}}return p}
            function toUTF8Array(d){var a=[];for(var c=0;c<d.length;c++){var b=d.charCodeAt(c);if(b<128){a.push(b)}else{if(b<2048){a.push(192|(b>>6),128|(b&63))}else{if(b<55296||b>=57344){a.push(224|(b>>12),128|((b>>6)&63),128|(b&63))}else{c++;b=65536+(((b&1023)<<10)|(d.charCodeAt(c)&1023));a.push(240|(b>>18),128|((b>>12)&63),128|((b>>6)&63),128|(b&63))}}}}return a}
        '''
        goblin_token = js2py.eval_js(jsScripts)(league + "." + tournament)
        return str(goblin_token)

    def get_goblin_generic_data(self, discord_server_id):
        # Make a get request to recover de .json data from GoblinSpy
        goblin_request = requests.get(os.getenv('SPYURLBASE') + 'overview.' + self.goblin_token + '.json')
        if goblin_request.ok:
            return self.read_tournament(goblin_request.json(), discord_server_id)
        else:
            return None

    def read_tournament(self, json, discord_server_id):
        # Se recuperan los datos del JSON
        info = json["Info"]["rows"][0]
        league = models.League(info[1])
        tournament = models.Tournament(discord_id=discord_server_id, tournament_name=info[2])
        # Ultima actualizacion de goblin spy
        tournament.last_update = info[3]
        # Se guardan las instancias de equipos
        all_teams = {}
        ranking = models.Ranking()
        # Lista de los equipos inscritos ordenados por puntuación
        ranking_data = json["LeagueStandings"]["rows"]
        for team_data in ranking_data:
            # team[10] es la casilla del coachbame. Get_Coach revisa si el nombre está inscrito en la DB de usuarios
            coach = models.Coach(team_data[10], team_data[10])
            bd_coach = self.crud.recover_coach(discord_server_id, bb_coach_name=team_data[10])
            if bd_coach:
                coach.display_name = bd_coach.discord_client_name
                coach.user_discord_id = bd_coach.discord_client_id
            # Se guarda la raza como el emoticono de la raza (bb<race_name>)
            team = models.Team(coach = coach, team_name=team_data[17], race=emojis.get_race_emoji(int(team_data[16])), wins=team_data[22], draws=team_data[23], loses=team_data[24], rank=team_data[18], td=team_data[25])
            ranking.add_team(team)
            all_teams[team.team_name] = team
        # Primero se recuperan los datos del histórico. Después, si la competición no es de tipo escalera y tiene partidos programados, se recuperan estos, incluidos los ya jugados
        # NOTA: Se crea una nueva instancia de un mismo partido porque en el json no hay ningun identificador comun entre Matches y Schedule
        # Recuoperación del histórico
        tournament.ranking = ranking
        history = models.History()
        matches_data = json["Matches"]["rows"]
        for match_data in matches_data:
            match = models.Match(local_team=all_teams[match_data[14]], visitor_team=all_teams[match_data[17]], local_score=match_data[15], visitor_score=match_data[16], status="played", played_time=match_data[4])
            history.add_match(match)
        tournament.match_history = history
        schedule_data = json["Schedule"]["rows"]
        if schedule_data == None or len(schedule_data) == 0:
            tournament_type = "ladder"
        else:
            tournament_type = schedule_data[0][7]
            schedule = models.Schedule()
            for match_data in schedule_data:
                match = models.Match(local_team=all_teams[match_data[19]], visitor_team=all_teams[match_data[25]], local_score=match_data[29], visitor_score=match_data[30]
                        , status=match_data[10], contest_id = match_data[6])
                if match.status == "scheduled":
                    if schedule.current_round == 0:
                        schedule.current_round = match_data[8]
                    # Recupera si los usuarios de dicord han establecido una hora para jugar
                    db_programmed_time = self.crud.recover_match_programmed_time(discord_server_id, match_contest_id = match.contest_id)
                    if db_programmed_time:
                        match.programmed_time = db_programmed_time.proposed_time
                        match.accepted = db_programmed_time.accepted
                schedule.add_match(match_data[8], match)
            tournament.schedule = schedule
        league.add_tournament(tournament)
        return league

    def get_player_next_match(self, round_matchs, user_discord_id):
        for match in round_matchs:
            if match.local_team.coach.user_discord_id == user_discord_id or match.visitor_team.coach.user_discord_id == user_discord_id:
                return match
        return None
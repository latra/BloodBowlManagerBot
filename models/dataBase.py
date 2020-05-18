class DBServer:
    def __init__(self, discord_server_id, league_name, tournament_name, goblin_token, discord_channel_id, language):
        self.discord_server_id = discord_server_id
        self.league_name = league_name
        self.tournament_name = tournament_name
        self.goblin_token = goblin_token
        self.discord_channel_id = discord_channel_id
        self.language = language   
class DBUser:
    def __init__(self, discord_server_id, discord_client_id, discord_client_name, coach_name):
        self.discord_server_id = discord_server_id
        self.discord_client_id = discord_client_id
        self.discord_client_name = discord_client_name
        self.coach_name = coach_name
class DBMatch:
    def __init__(self, match_contest_id, leader_discord_user_id, invited_discord_user_id, discord_server_id, accepted, proposed_time):
        self.match_contest_id = match_contest_id
        self.leader_discord_user_id = leader_discord_user_id
        self.invited_discord_user_id = invited_discord_user_id
        self.discord_server_id = discord_server_id
        self.accepted = accepted
        self.proposed_time = proposed_time
class DBMatchJServer:
    def __init__(self, match_contest_id, leader_discord_user_id, invited_discord_user_id, discord_server_id, accepted, proposed_time, local_team, visitor_team, league_name, tournament_name, goblin_token, discord_channel_id, language):
        self.match_contest_id = match_contest_id
        self.leader_discord_user_id = leader_discord_user_id
        self.invited_discord_user_id = invited_discord_user_id
        self.discord_server_id = discord_server_id
        self.accepted = accepted
        self.proposed_time = proposed_time
        self.local_team = local_team
        self.visitor_team = visitor_team
        self.league_name = league_name
        self.tournament_name = tournament_name
        self.goblin_token = goblin_token
        self.discord_channel_id = discord_channel_id
        self.language = language
import re, os, sys, requests, datetime
import discord
from discord.utils import get
import crud, goblinSpy, constants.dictionaries as dictionaries, constants.texts as texts

class Commands:
    def __init__(self, ctx):
        self.ctx = ctx
        self.crud = crud.Crud()
        self.discord_id = ctx.author.id
        self.language = texts.EN()
        self.league_name = None
        self.tournament_name = None
        self.goblin_token = None
        saved_data = self.crud.recover_config(self.discord_id)
        if saved_data:
            self.league_name = saved_data.league_name
            self.tournament_name = saved_data.tournament_name
            self.goblin_token = saved_data.goblin_token
            self.language =  dictionaries.get_language(saved_data.language)
        self.goblin = goblinSpy.GoblinSpy(self.goblin_token, self.crud)
    #region COMMANDS
    #region COMMAND - HELP
    async def help(self):
        command = self.ctx.message.content.split()
        # Select witch help has to show
        if len(command) > 1:
            if command[1] == '1':
                await self.help_setup()
                return
            elif command[1] == '2':
                await self.help_commands()
                return
        # If not list has been selected, it will show the default help, listing the others
        await self.help_generic()

    async def help_generic(self):
        # List the help chapters
        embed = discord.Embed(
            colour = discord.Colour.red(),
            title=self.language.HELP_GENERIC_TITLE,
            description=self.language.HELP_GENERIC_DESCRIPTION
        )
        embed.set_thumbnail(url=self.language.BOT_THUMBAIL)
        for field in self.language.HELP_GENERIC_FIELDS:
            embed.add_field(name= field[0], value=field[1], inline=False)

        await self.ctx.send(embed = embed)

    async def help_setup(self):
        # Shows how to setup the bot on a new server
        embed = discord.Embed(
            colour = discord.Colour.red(),
            title=self.language.HELP_SETUP_TITLE,
            description=self.language.HELP_SETUP_DESCRIPTION
        )
        embed.set_thumbnail(url=self.language.BOT_THUMBAIL)
        for field in self.language.HELP_SETUP_FIELDS:
            embed.add_field(name= field[0], value=field[1], inline=False)

        await self.ctx.send(embed = embed)
    async def help_commands(self):
        # Shows the available commands
        embed = discord.Embed(
            colour = discord.Colour.red(),
            title=self.language.HELP_COMMAND_TITLE,
            description=self.language.HELP_COMMAND_DESCRIPTION
        )
        embed.set_thumbnail(url=self.language.BOT_THUMBAIL)
        for field in self.language.HELP_COMMAND_FIELDS:
            embed.add_field(name= field[0], value=field[1], inline=False)

        await self.ctx.send(embed = embed)
    #endregion
    
    async def configure(self):
        #Configure the server with the passed parammeters
        if (self.ctx.message.author.guild_permissions.administrator):
            regex_exp = "\"(.*)\" \"(.*)\""
            command = re.split(regex_exp, self.ctx.message.content)
            
            if self.goblin_token:
                # If the server is already configured, return an error
                await self.ctx.send(content=self.language.ERROR_ALREADY_CONFIGURED)
            else:
                if len(command) >= 3:
                    # Add the server to DB and reutn OK
                    goblin_token = self.goblin.get_goblin_token(command[1], command[2])
                    print(self.ctx.message.channel.id)
                    if self.crud.create_config(self.discord_id, command[1], command[2], goblin_token, self.ctx.message.channel.id): await self.ctx.send(content=self.language.SUCCESS_SERVER_CONFIGURED)
                    else: await self.ctx.send(content=self.language.ERROR_DEFAULT)
                else:
                    # Syntax error message
                    await self.ctx.send(content=self.language.ERROR_SYNTAX_CONFIGURATION)
        else:
            await self.ctx.send(content=self.language.ERROR_NOT_ALLOWED)
    async def reset(self):
        # Delete the server configuration
        #Only can be do it by an administrator
        if (self.ctx.message.author.guild_permissions.administrator):
            if (self.goblin_token):
                if self.crud.delete_config(self.discord_id): await self.ctx.send(content=self.language.SUCCESS_SERVER_RESET)
                else: await self.ctx.send(content=self.language.ERROR_DEFAULT)
            else:
                await self.ctx.send(content=self.language.ERROR_NOT_CONFIGURED)
        else:
            await self.ctx.send(content=self.language.ERROR_NOT_ALLOWED)

    async def teams(self):
        #Shows the competition team list
        if not self.goblin_token:
            await self.ctx.send(content=self.language.ERROR_NOT_CONFIGURED)
        else:
            #Get data from GoblinSpy
            league = self.goblin.get_goblin_generic_data(self.discord_id)
            if league:
                tournament = league.tournaments[self.tournament_name]
                if tournament:
                    teams = ""
                    coach = ""
                    ranking = ""
                    for team_position in tournament.ranking.ranking:
                        race_logo = get(self.ctx.message.guild.emojis, name = tournament.ranking.ranking[team_position].race)
                        if not race_logo: race_logo = ":grey_question:"
                        teams += "%s %s\n\n" %(race_logo, tournament.ranking.ranking[team_position].team_name)
                        coach += "%s\n\n" % (tournament.ranking.ranking[team_position].coach.display_name)
                        ranking += "%s\n\n" % (dictionaries.get_ranking_emoji(team_position))
                    

                    embed = discord.Embed(
                    colour = discord.Colour.red(),
                    description = self.language.LAST_UPDATE % tournament.last_update,    
                    title = "Teams on %s" % self.tournament_name,
                    )
                    embed.add_field(name = ":trophy:", value=ranking, inline=True)
                    embed.add_field(name = self.language.TEAM_NAME, value=teams, inline=True)
                    embed.add_field(name = self.language.COACH, value=coach, inline=True)

                    await self.ctx.send(embed=embed)
                else:
                    await self.ctx.send(content=self.language.ERROR_DATA_NOT_FOUND)
            else:
                await self.ctx.send(content=self.language.ERROR_DATA_NOT_FOUND)
    async def round(self):
        #Shows the specifyied or current round
        if not self.goblin.goblin_token:
            await self.ctx.send(content=self.language.ERROR_NOT_CONFIGURED)
        else:
            #Get data from GoblinSpy
            league = self.goblin.get_goblin_generic_data(self.discord_id)
            tournament = league.tournaments[self.tournament_name]
            if tournament:
                if tournament.type_of_competition != "ladder":

                    command = self.ctx.message.content.split()

                    if len(command) == 1: get_round = tournament.schedule.current_round
                    else: get_round = command[1]
                    if not str.isdigit(get_round) or int(get_round) > len(tournament.schedule.schedule): await self.ctx.send(content=self.language.ERROR_INCORRECT_ROUND % get_round)
                    # Add local team and visitor team (and result if the match has ended) on respective strings. Every string will be on a different column on embed message
                    local_teams = ""
                    visitor_teams = ""
                    results = ""
                    for match in tournament.schedule.schedule[get_round]:
                        local_teams += "%s\n\n" % (match.local_team.team_name)
                        visitor_teams += " %s\n\n" % (match.visitor_team.team_name)
                        results += "%s - %s\n\n" % (match.local_score, match.visitor_score)
                    embed = discord.Embed(
                        title= self.language.ROUND % (get_round),
                        description = self.language.LAST_UPDATE % tournament.last_update,    
                        colour = discord.Colour.red()
                    )
                    embed.add_field(name = self.language.LOCAL_TEAM, value=local_teams, inline=True)
                    embed.add_field(name = self.language.VS, value=results, inline=True)
                    embed.add_field(name = self.language.VISITOR_TEAM, value=visitor_teams, inline=True)
                    await self.ctx.send(embed=embed)
                else:
                    await self.ctx.send(content=self.language.ERROR_NOT_SCHEDULE)

            else:
                await self.ctx.send(content=self.language.ERROR_DATA_NOT_FOUND)

    async def user_register(self):
        if not self.goblin_token:
            await self.ctx.send(content=self.language.ERROR_NOT_CONFIGURED)
        else:
            command = self.ctx.message.content.split()
            if len(command) > 1 and self.coach_exists(' '.join(command[1:])):
                # Tries create the user. Returns a dictionary status, action
                result = self.crud.create_or_update_coach(self.discord_id, ' '.join(command[1:]), str(self.ctx.message.author), self.ctx.message.author.id)
                if result['status']:
                    if result['action'] == "CREATED":
                        await self.ctx.send(content=self.language.SUCCESS_IAM_REGISTER)
                    elif result['action'] == "UPDATED":
                        await self.ctx.send(content=self.language.SUCCESS_IAM_UPDATE)
                else:
                    await self.ctx.send(content=self.language.ERROR_ALREADY_REGISTERED)
            else:
                await self.ctx.send(content=self.language.ERROR_SYNTAX_IAM)

    def coach_exists(self, coach_name):
        league = self.goblin.get_goblin_generic_data(self.discord_id)
        for team in league.tournaments[self.tournament_name].ranking.ranking:
            if league.tournaments[self.tournament_name].ranking.ranking[team].coach.coach_name ==coach_name:
                return True
        else: return False

    async def my_next_match(self):
        if not self.goblin.goblin_token:
            await self.ctx.send(content=self.language.ERROR_NOT_CONFIGURED)
        else:
            coach_name = self.crud.recover_coach(self.discord_id, discord_user_id=self.ctx.message.author.id)
            if coach_name:
                league = self.goblin.get_goblin_generic_data(self.discord_id)
                tournament = league.tournaments[self.tournament_name]
                if tournament.schedule:
                    embed = discord.Embed(
                        colour = discord.Colour.red(),
                        title = self.language.NEXT_MATCH
                    )
                    next_match = self.goblin.get_player_next_match(tournament.schedule.schedule[tournament.schedule.current_round], self.ctx.message.author.id)
                    if next_match.status == 'played':
                        embed.description = self.language.NEXTMATCH_GAME_PLAYED
                    else:
                        embed.add_field(name="%s %s" % (get(self.ctx.message.guild.emojis, name=next_match.local_team.race), next_match.local_team.team_name) , value="_%s_" 
                            % (next_match.local_team.coach.display_name))
                        embed.add_field(name=self.language.VS, value="-")
                        embed.add_field(name="%s %s" % (get(self.ctx.message.guild.emojis, name=next_match.visitor_team.race), 
                            next_match.visitor_team.team_name), value="_%s_" % next_match.visitor_team.coach.display_name)
                            
                        if not next_match.programmed_time:
                            embed.description= self.language.NEXTMATCH_TIME_NON_DEFINED
                        else:
                            programmed_info = self.crud.recover_match_programmed_time(self.discord_id, match_contest_id=next_match.contest_id)
                            if programmed_info.accepted:
                                embed.description=self.language.NEXTMATCH_TIME_DEFINED % next_match.programmed_time
                            elif programmed_info.invited_discord_user_id == self.ctx.message.author.id:
                                embed.description= self.language.NEXTMATCH_TIME_DEFINED_USER_NO_ACCEPTED % next_match.programmed_time
                            else:
                                embed.description= self.language.NEXTMATCH_TIME_DEFINED_RIVAL_NO_ACCEPTED % next_match.programmed_time
                    await self.ctx.send(embed=embed)
                else:
                    await self.ctx.send(content=self.language.ERROR_NOT_SCHEDULE)
            else:
                await self.ctx.send(content=self.language.ERROR_NOT_REGISTERED)

    async def establish_date_match(self):
        if not self.goblin.goblin_token:
            await self.ctx.send(content=self.language.ERROR_NOT_CONFIGURED)
        else:
            try:
                command = ' '.join(self.ctx.message.content.split()[1:])
                setted_time = datetime.datetime.strptime(command, "%d/%m/%Y %H:%M")
                bd_coach = self.crud.recover_coach(self.discord_id, discord_user_id= self.ctx.message.author.id)
                if bd_coach:
                    league = self.goblin.get_goblin_generic_data(self.discord_id)
                    tournament = league.tournaments[self.tournament_name]
                    if tournament.schedule:
                        next_match = self.goblin.get_player_next_match(tournament.schedule.schedule[tournament.schedule.current_round], self.ctx.message.author.id)
                        rival_id = next_match.local_team.coach.user_discord_id if self.ctx.message.author.id != next_match.local_team.coach.user_discord_id else next_match.visitor_team.coach.user_discord_id
                        if next_match and next_match.status == 'scheduled':
                            db_programmed_time = self.crud.create_or_update_match_programmed_time(self.discord_id, next_match.contest_id, 
                                datetime.datetime.strftime(setted_time, '%Y-%m-%d %H:%M'), self.ctx.message.author.id, rival_id, next_match.local_team.team_name, next_match.visitor_team.team_name)
                            await self.ctx.send(content=self.language.ERROR_ESTABLISHDATE_INVITED if not db_programmed_time['status'] else self.language.SUCCESS_ESTABLISHDATE_UPDATE if db_programmed_time['action'] == "UPDATED" else self.language.SUCCESS_ESTABLISHDATE_REGISTER)
                            # If it's created or updated, we will send a MD message notifying to the other user
                            invited_user = self.ctx.message.guild.get_member(rival_id)
                            if invited_user and db_programmed_time['action'] == 'CREATED':
                                await invited_user.send(self.language.INFO_MATCHCREATED % command)
                            elif invited_user and db_programmed_time['action'] == 'UPDATED':
                                await invited_user.send(self.language.INFO_MATCHUPDATED % command)
                        else:
                            await self.ctx.send(content=self.language.ERROR_ESTABLISHDATE_MATCHERROR)
                    else:
                        await self.ctx.send(content=self.language.ERROR_NOT_SCHEDULE)
                else:
                    await self.ctx.send(content=self.language.ERROR_NOT_REGISTERED)
            except:
                await self.ctx.send(content=self.language.ERROR_SYNTAX_ESTABLISHDATE)

    async def accept_time(self):
        if not self.goblin.goblin_token:
            await self.ctx.send(content=self.language.ERROR_NOT_CONFIGURED)
        else:
            db_programmed_time = self.crud.recover_match_programmed_time(self.discord_id, invited_discord_user_id = self.ctx.author.id)
            if db_programmed_time and not db_programmed_time.accepted:
                self.crud.accept_match_programmed_time(self.discord_id, db_programmed_time.match_contest_id)
                await self.ctx.send(content=self.language.SUCCESS_MATCH_ACCEPTED)
                leader_user = self.ctx.message.guild.get_member(db_programmed_time.leader_discord_user_id)
                await leader_user.send(self.language.INFO_USERACCEPT % db_programmed_time.proposed_time)
            else:
                #already accepted
                await self.ctx.send(self.language.ERROR_ACCEPT_NOMATCH)
    #endregion
    async def change_language(self):
        if not self.goblin.goblin_token:
            await self.ctx.send(content=self.language.ERROR_NOT_CONFIGURED)
        else:
            command = self.ctx.message.content.split()
            if len(command) > 1 and dictionaries.get_language(command[1]):
                if self.crud.change_language(self.ctx.message.author.guild.id, command[1]):
                    self.language = dictionaries.get_language(command[1])
                    await self.ctx.send(self.language.LANGUAGE_UPDATED)
                else:
                    await self.ctx.send(self.language.ERROR_DEFAULT)
            else:
                await self.ctx.send(self.language.ERROR_LANGUAGE_INVALID)
        
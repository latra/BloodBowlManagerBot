import sqlite3, os
import models.dataBase as models
class Crud:
    def __init__(self):
        self.database = sqlite3.connect(os.getenv('SQLITE_CONNECTION'))
        self.database.execute("PRAGMA foreign_keys = 1")


    def recover_config(self, discord_server_id):
        #Recovers a server configuration using the discord server id
        query = "SELECT * FROM SERVERS WHERE discordServerId = %i;" % discord_server_id
        cursor = self.database.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()

        if result:
            return models.DBServer(result[0], result[1], result[2], result[3])
        else:
            return None

    def create_config(self, discord_server_id, league_name, tournament_name, token):
        #Creates a new entry on tournaments table. Used when the bot is configured on a new server
        try:
            query = "INSERT INTO SERVERS (discordServerId, leagueName, tournamentName, goblinToken) VALUES (%i, '%s', '%s', '%s');" % (discord_server_id, league_name, tournament_name, token)
            cursor = self.database.cursor()
            cursor.execute(query)
            self.database.commit()
            cursor.close()
            return True
        except:
            return False
    def delete_config(self, discord_server_id):
        #Deletes a server config and all the items related to it
        try:
            query = "DELETE FROM SERVERS WHERE discordServerId = %i;" % discord_server_id
            cursor = self.database.cursor()
            cursor.execute(query)
            self.database.commit()
            cursor.close()
            return True
        except:
            return False
    def recover_coach(self, discord_server_id, bb_coach_name = None, discord_user_id = None):
        #Recovers a coach or returns None if not found
        if bb_coach_name:
            query = "SELECT * FROM USERS WHERE discordServerId = %i AND coachName = '%s';" % (discord_server_id, bb_coach_name)
        elif discord_user_id:
            query = "SELECT * FROM USERS WHERE discordServerId = %i AND discordClientId = %i;" % (discord_server_id, discord_user_id)
        else:
            # when is IA player
            return models.DBUser(discord_server_id, None, 'IA', None)
        cursor = self.database.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        if result:
            return models.DBUser(result[0], result[1], result[2], result[3])
        else:
            return None
    def create_or_update_coach(self, discord_server_id, bb_coach_name, discord_user_name, discord_user_id):
        #Links a coach name to discord account. Return None if the coach has already taken
        coach = self.recover_coach(discord_server_id, discord_user_id=discord_user_id)
        try:
            if self.recover_coach(discord_server_id, bb_coach_name=bb_coach_name):
                return None
            elif coach:
                query = "UPDATE USERS SET coachName = '%s' WHERE discordServerId = %i AND discordClientId=%i;" % (bb_coach_name, discord_server_id, discord_user_id)
                action = "UPDATED"
            else:
                query = "INSERT INTO USERS (discordServerId, discordClientId, discordClientName, coachName) VALUES (%i, %i, '%s', '%s')" % (discord_server_id, discord_user_id, discord_user_name, bb_coach_name)
                action = "CREATED"
            cursor = self.database.cursor()
            cursor.execute(query)
            self.database.commit()
            cursor.close()
            return {'status':True, 'action':action}
        except:
            return {'status':False, 'action':None}
    def recover_match_programmed_time(self, discord_server_id, match_contest_id = None, invited_discord_user_id = None):
        #Recovers a match using the match_id or the invited user_id
        if match_contest_id:
            query = "SELECT * FROM MATCHES WHERE matchContestId='%s';" % match_contest_id
        else:
            query = "SELECT * FROM MATCHES WHERE invitedDiscordUserId = %i" % invited_discord_user_id
        cursor = self.database.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        if result:
            return models.DBMatch(result[0], result[1], result[2], result[3], result[4], result[5] )
        else:
            return None
    def create_or_update_match_programmed_time(self, discord_server_id, match_contest_id, proposed_date, leader_discord_user_id, invited_discord_user_id, accepted = 0):
        #Creates a new entry on matches table or update one
        if not invited_discord_user_id:
            invited_discord_user_id = -1
            accepted = 1
        match = self.recover_match_programmed_time(discord_server_id=discord_server_id, match_contest_id=match_contest_id)
        if match and match.leader_discord_user_id == leader_discord_user_id:
            query = "UPDATE MATCHES SET proposedTime = '%s', accepted = %i WHERE discordServerId=%i AND matchContestId='%s';" % (proposed_date, accepted, discord_server_id, match_contest_id)
            action = "UPDATED"
        elif match:
            return {'status':False, 'action':None}
        elif not match:
            query = "INSERT INTO MATCHES (matchContestId, leaderDiscordUserId, InvitedDiscordUserId, discordServerId, accepted, proposedTime) VALUES ('%s', %i, %i, %i, %i, '%s');" % (match_contest_id, leader_discord_user_id, invited_discord_user_id, discord_server_id, accepted, proposed_date)
            action = "CREATED"
        try:
            cursor = self.database.cursor()
            cursor.execute(query)
            self.database.commit()
            cursor.close()
            return {'status':True, 'action':action}
        except:
            return {'status':False, 'action':None}
    def accept_match_programmed_time(self, discord_server_id, match_contest_id):
        #Changes the accepted status to one of the selected match
        query = "UPDATE MATCHES SET accepted = 1 WHERE matchContestId='%s' AND discordServerId = %i;" % (match_contest_id, discord_server_id)
        try:
            cursor = self.database.cursor()
            cursor.execute(query)
            self.database.commit()
            cursor.close()
            return True
        except:
            return False
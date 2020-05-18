# Setup a empty DB with the needed rows
from dotenv import load_dotenv
import sqlite3, os

QUERYS = [  
        'CREATE TABLE "SERVERS" ('+
        '	"discordServerId"	INTEGER NOT NULL,'+
        '	"leagueName"	TEXT NOT NULL,'+
        '	"tournamentName"	TEXT NOT NULL,'+
        '	"goblinToken"	TEXT NOT NULL,' +
        '	"discordChannelId"	INTEGER,'+
	    '   "language"	TEXT DEFAULT \'EN\',' + 
        '	PRIMARY KEY("discordServerId")'+
        ')',
        'CREATE TABLE "USERS" (' +
        '	"discordServerId"	INTEGER NOT NULL,' +
        '	"discordClientId"	INTEGER NOT NULL,' +
        '	"discordClientName"	TEXT NOT NULL,' +
        '	"coachName"	TEXT NOT NULL,' +
        '	PRIMARY KEY("discordClientId","discordServerId"),' +
        '   FOREIGN KEY("discordServerId") REFERENCES "SERVERS"("discordServerId") ON DELETE CASCADE' +
        ')',
        'CREATE TABLE "MATCHES" (' +
        '	"matchContestId"	INTEGER NOT NULL UNIQUE,' +
        '	"leaderDiscordUserId"	INTEGER,' +
        '	"invitedDiscordUserId"	INTEGER,' +
        '	"discordServerId"	INTEGER NOT NULL,' +
        '	"accepted"	INTEGER DEFAULT 0,' +
        '	"proposedTime"	TEXT,' +
        '   "localTeamName"	TEXT,' +'
	    '   "visitorTeamName"	TEXT,' +
        '	PRIMARY KEY("matchContestId"),' +
        '	FOREIGN KEY("discordServerId") REFERENCES "SERVERS"("discordServerId") ON DELETE CASCADE' +
        ');'
        
]

load_dotenv()
connect = sqlite3.connect(os.getenv('SQLITE_CONNECTION'))
cursor = connect.cursor()
for query in QUERYS: 
    cursor.execute(query)

connect.commit()
cursor.close()
class EN:
    SUCCESS_SERVER_CONFIGURED = "The server has been configured successfully"
    SUCCESS_SERVER_RESET = "The configuration has been deleted"
    SUCCESS_IAM_REGISTER = "You has been registered successfully!"
    SUCCESS_IAM_UPDATE =  "Your coach name has been updated"
    SUCCESS_ESTABLISHDATE_UPDATE= "Match date updated!"
    SUCCESS_ESTABLISHDATE_REGISTER="Match date established!"
    SUCCESS_MATCH_ACCEPTED = "Match accepted!"
    NEXTMATCH_TIME_DEFINED = "The match date has been defined for %s."
    NEXTMATCH_TIME_DEFINED_USER_NO_ACCEPTED = "Your rival proposed play the match on %s, but you didn't accepted it yet. Use ```bb2!acceptTime``` to do it."
    NEXTMATCH_TIME_DEFINED_RIVAL_NO_ACCEPTED = "You proposed play the match on %s, but your rival didn't accepted yet."

    NEXTMATCH_TIME_NON_DEFINED = "You have not defined the match day. Use ```bb2!iwillplay DD/MM/YYY HH:mm``` to stablish it."
    NEXTMATCH_GAME_PLAYED = "You already played this round!"
    ERROR_ESTABLISHDATE_INVITED = "You has been invited to play this match. Use ```bb2!nextMatch``` to check it and ```bb2!acceptMatch``` to accept the proposed time."
    ERROR_ESTABLISHDATE_MATCHERROR = "Error: Next match not found."
    ERROR_SYNTAX_ESTABLISHDATE = "Error: Invalid syntax. Please, use ```bb2!iwillplay DD/MM/YYYY HH:mm``` to set or update the match day"
    ERROR_NOT_CONFIGURED="Error: There is no tournament configured"
    ERROR_ALREADY_CONFIGURED = "Error: The server is already configured"
    ERROR_NOT_ALLOWED = "Error: Only server admins can do this action"
    ERROR_DATA_NOT_FOUND = "Error: Data not found. Remember to follow the configuration steps. If you have already done so, it may take a few hours the first time to retrieve your league data. Try it again later."
    ERROR_NOT_SCHEDULE = "Error: This type of tournament does not have a schedule"
    ERROR_SYNTAX_CONFIGURATION = "Error: Invalid syntax. Please, use ```bb2!configure \"league name\" \"tournament name\"```, including the quotes, to configure your server."
    ERROR_SYNTAX_IAM = "Error: Invalid syntax. Please, use ```bb2!iam {your coach name}``` to link your discord account to your coach name"
    ERROR_NOT_REGISTERED = "Error: You are not identified. Use  ```bb2!iam {your coach name}``` to link your discord account to your coach name and try again."
    ERROR_ALREADY_REGISTERED = "Error: This coach is already registered. If it's your coach name, talk with an administrator."
    ERROR_INCORRECT_ROUND="Error: Round '%s' does not exist."
    BOT_THUMBAIL = "https://i.imgur.com/8eptQlM.png"

    HELP_GENERIC_TITLE = "Blood Bowl Manager"
    HELP_GENERIC_DESCRIPTION = "To see a page, just add the page number after the bb2!help command.\nLike this: ```bb2!help 2```"
    HELP_GENERIC_FIELDS = [
        ("Chapter 1: Set up your tournament", "Check the firsts steps on Blood Bowl Bot")
        ,("Chapter 2: Blood Bowl Commands", "Check the available commands on Blood Bowl Bot after configure your tournament")
    ]

    HELP_SETUP_TITLE = "Setup - Blood Bowl Manager"
    HELP_SETUP_DESCRIPTION = "Follow the next steps to configure your tournament on the discord server"
    HELP_SETUP_FIELDS = [
        ("#1 Allow GoblinSpy recover data from your tournament.", "Join http://www.mordrek.com/goblinSpy/web/activate.html?, introduce your tournament data and click on \"Activate\" button.")
        ,("#2 Configure the tournament on the bot", "Use ```bb2!config \"League name\" \"Tournament name\"```, including quotation marks, to configure the tournament.")
        ,("#3 Install the custom emojis", "Install the following emoji package on your server with the races icons")
    ]

    HELP_COMMAND_TITLE = "Commands - Blood Bowl Manager"
    HELP_COMMAND_DESCRIPTION = "Use the following commands to get info about the configured tournament. Newly played matches may take a while to update."
    HELP_COMMAND_FIELDS = [
        ("```bb2!teams```", "List all teams from the tournament"),
        ("```bb2!round <round number>```", "Show the matches of the selected round. If no round is specified, it will show the current round."),
        ("```bb2!Iam <coach name>```", "Link your Discord acc to your BloodBowl nickname, changing the coach name by your discord id on the messages."),
        ("```bb2!nextMatch```", "It shows your next match and the programmated day."),
        ("```bb2!IWillPlay <DD-MM-YYYY hh:mm>```", "Define a date time  .")
        ]

    INFO_MATCHCREATED = "Your opponent has proposed you play on %s. Go to the server and use ```bb2!acceptMatch``` to accept it or ```bb2!declineMatch``` to decline."
    INFO_MATCHUPDATED = "Your opponent changed the proposed date to play to %s. Go to the server and use ```bb2!acceptMatch``` to accept it or ```bb2!declineMatch``` to decline."
    INFO_USERACCEPT = "Your opponent has accepted your proposal. The match is scheduled to start at %s"
    ROUND= "Round %s"
    TEAM_NAME = "Team name"
    COACH = "Coach"
    LAST_UPDATE = "Last update at %s"
    LOCAL_TEAM = "Local Team"
    VS = "VS"
    VISITOR_TEAM = "Visitor Team"
    NEXT_MATCH = "Next Match"
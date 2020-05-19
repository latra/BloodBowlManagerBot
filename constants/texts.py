class EN:
    SUCCESS_SERVER_CONFIGURED = "The server has been configured successfully"
    SUCCESS_SERVER_RESET = "The configuration has been deleted"
    SUCCESS_IAM_REGISTER = "You has been registered successfully!"
    SUCCESS_IAM_UPDATE =  "Your coach name has been updated"
    SUCCESS_ESTABLISHDATE_UPDATE= "Match date updated!"
    SUCCESS_ESTABLISHDATE_REGISTER="Match date established!"
    SUCCESS_MATCH_ACCEPTED = "Match accepted!"
    NEXTMATCH_TIME_DEFINED = "The match date has been defined for %s."
    NEXTMATCH_TIME_DEFINED_USER_NO_ACCEPTED = "Your rival proposed play the match on %s, but you didn't accepted it yet. Use ```bb2!accept``` to do it."
    NEXTMATCH_TIME_DEFINED_RIVAL_NO_ACCEPTED = "You proposed play the match on %s, but your rival didn't accepted yet."

    NEXTMATCH_TIME_NON_DEFINED = "You have not defined the match day. Use ```bb2!register DD/MM/YYY HH:mm``` to stablish it."
    NEXTMATCH_GAME_PLAYED = "You already played this round!"
    ERROR_ACCEPT_NOMATCH = "There is not match to accept"
    ERROR_DEFAULT = "An unknown error has occurred. Please, try it later."
    ERROR_ESTABLISHDATE_INVITED = "You has been invited to play this match. Use ```bb2!next``` to check it and ```bb2!accept``` to accept the proposed time."
    ERROR_ESTABLISHDATE_MATCHERROR = "Error: Next match not found."
    ERROR_SYNTAX_ESTABLISHDATE = "Error: Invalid syntax. Please, use ```bb2!register DD/MM/YYYY HH:mm``` to set or update the match day"
    ERROR_NOT_CONFIGURED="Error: There is no tournament configured"
    ERROR_ALREADY_CONFIGURED = "Error: The server is already configured"
    ERROR_NOT_ALLOWED = "Error: Only server admins can do this action"
    ERROR_DATA_NOT_FOUND = "Error: Data not found. Remember to follow the configuration steps. If you have already done so, it may take a few hours the first time to retrieve your league data. Try it again later or use ```bb2!IWantReset```."
    ERROR_NOT_SCHEDULE = "Error: This type of tournament does not have a schedule"
    ERROR_SYNTAX_CONFIGURATION = "Error: Invalid syntax. Please, use ```bb2!configure \"league name\" \"tournament name\"```, including the quotes, to configure your server."
    ERROR_SYNTAX_IAM = "Error: Invalid syntax. Please, use ```bb2!register {your coach name}``` to link your discord account to your coach name"
    ERROR_NOT_REGISTERED = "Error: You are not identified. Use  ```bb2!register {your coach name}``` to link your discord account to your coach name and try again."
    ERROR_ALREADY_REGISTERED = "Error: This coach is already registered. If it's your coach name, talk with an administrator."
    ERROR_INCORRECT_ROUND="Error: Round '%s' does not exist."
    ERROR_LANGUAGE_INVALID ="Error: Invalid or not implemented language"
    ERROR_INVALID_COMMAND="Error. This command is invalid. Check ```bb2!help```"
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
        ("```bb2!register <coach name>```", "Link your Discord acc to your BloodBowl nickname, changing the coach name by your discord id on the messages."),
        ("```bb2!next```", "It shows your next match and the programmated day."),
        ("```bb2!date <DD-MM-YYYY hh:mm>```", "Define a date time to your next time."),
        ("```bb2!accept```", "Accepts a date proposed by your rival.")
    ]

    INFO_MATCHCREATED = "Your next match on %s league and %s tournament is against %s.\nYour opponent has proposed you play on %s. Go to the server and use ```bb2!acceptMatch``` to accept it or ```bb2!declineMatch``` to decline."
    INFO_MATCHUPDATED = "Your opponent changed the proposed date to play your next match on %s league and %s tournament to %s. Go to the server and use ```bb2!acceptMatch``` to accept it or ```bb2!declineMatch``` to decline."
    INFO_USERACCEPT = "Your opponent has accepted your proposal. The match is scheduled to start at %s"
    ROUND= "Round %s"
    TEAM_NAME = "Team name"
    COACH = "Coach"
    LAST_UPDATE = "Last update at %s"
    LOCAL_TEAM = "Local Team"
    VS = "VS"
    VISITOR_TEAM = "Visitor Team"
    NEXT_MATCH = "Next Match"
    NEAR_MATCH_TITLE= "%s VS %s"
    NEAR_MATCH_DESCRIPTION = "The match will start at %s, stay tuned for the match!"
    LANGUAGE_UPDATED = "Ok! I will speak in English from now on."
    DM_SENDED  = "Sent you a DM containing the help message!"
class ES:
    SUCCESS_SERVER_CONFIGURED = "¡Servidor configurado correctamente!"
    SUCCESS_SERVER_RESET = "¡Se ha reiniciado la configuración del servidor!"
    SUCCESS_IAM_REGISTER = "¡Te has registrado correctamente!"
    SUCCESS_IAM_UPDATE =  "¡Se ha actualizado tu nombre de entrenador!"
    SUCCESS_ESTABLISHDATE_UPDATE= "¡Se ha actualizado la fecha del partido!"
    SUCCESS_ESTABLISHDATE_REGISTER="¡Se ha establecido la fecha del partido!"
    SUCCESS_MATCH_ACCEPTED = "¡Patido aceptado!"
    NEXTMATCH_TIME_DEFINED = "Se ha establecido el día y hora %s para el partido."
    NEXTMATCH_TIME_DEFINED_USER_NO_ACCEPTED = "Tú oponente te ha propuesto jugar el %s, pero aún no has aceptado. Utiliza ```bb2!accept``` para aceptar la hora."
    NEXTMATCH_TIME_DEFINED_RIVAL_NO_ACCEPTED = "Has propuesto jugar el %s, pero tu rival aún no ha aceptado el encuentro."

    NEXTMATCH_TIME_NON_DEFINED = "Aún no habéis definido la fecha del encuentro. Usa ```bb2!register DD/MM/YYY HH:mm``` para hacerlo."
    NEXTMATCH_GAME_PLAYED = "¡Ya has jugado esta ronda!"
    ERROR_ACCEPT_NOMATCH = "No tienes ningún partido pendiente de ser aceptado."
    ERROR_DEFAULT = "Ha ocurrido un error. Vuelve a intentarlo más tarde."
    ERROR_ESTABLISHDATE_INVITED = "Tu rival ya ha propuesto la hora del partido. Utiliza ```bb2!next``` para revisar la hora propuest y ```bb2!accept``` para aceptar."
    ERROR_ESTABLISHDATE_MATCHERROR = "Error: No se ha encontrado el próximo partido."
    ERROR_SYNTAX_ESTABLISHDATE = "Error: Comando inválido. Por favor, utilice ```bb2!register DD/MM/YYYY HH:mm``` para establecer o actualizar la hora del partido"
    ERROR_NOT_CONFIGURED="Error: No hay ningún torneo configurado"
    ERROR_ALREADY_CONFIGURED = "Error: El servidor ya está configurado. Reinicie la configuración antes si desea volver a seleccionar la liga"
    ERROR_NOT_ALLOWED = "Error: Solo los administradores pueden realizar esta acción"
    ERROR_DATA_NOT_FOUND = "Error: No se han encontrado los datos. Recuerda seguir los pasos de configuración y, si ya lo has hecho, ten en cuenta que GoblinSpy puede tardar unas horas en recuperar los datos la primera vez."
    ERROR_NOT_SCHEDULE = "Error: No se ha encontrado ningún calendario para este torneo."
    ERROR_SYNTAX_CONFIGURATION = "Error: Sintaxis inválida. Por favor, utiliza ```bb2!configure \"league name\" \"tournament name\"```, incluyendo las comillas, para configurar el servidor."
    ERROR_SYNTAX_IAM = "Error: Sintaxis inválida. Por favor, utilice ```bb2!register {nombre de entrenador}``` para vincular tu cuenta de BloodBowl a Discord"
    ERROR_NOT_REGISTERED = "Error: Aún no te has identificado. Por favor, utilice ```bb2!register {nombre de entrenador}``` para vincular tu cuenta de BloodBowl a Discord"
    ERROR_ALREADY_REGISTERED = "Error: Alguien se ha registrado ya como este entrenador. Si es tu nombre de entrenador ponte en contacto con un administrador."
    ERROR_INCORRECT_ROUND="Error: La ronda '%s' no existe."
    ERROR_LANGUAGE_INVALID = "Error: El idioma seleccionado no es válido o no está disponible. Utiliza ```bb2!help``` para más información."
    ERROR_INVALID_COMMAND="Error. El comando introducido el inválido. Utiliza ```bb2!help``` para más información"

    BOT_THUMBAIL = "https://i.imgur.com/8eptQlM.png"

    HELP_GENERIC_TITLE = "Blood Bowl Manager"
    HELP_GENERIC_DESCRIPTION = "Para ver un capítulo, sencillamente añade el número del capítulo al final del comando de bb2!help.\nPor ejemplo: ```bb2!help 2```"
    HELP_GENERIC_FIELDS = [
        ("Chapter 1: Configura tu torneo", "Revisa como configurar y dar los primeros pasos en Blood Bowl Manager Bot")
        ,("Chapter 2: Blood Bowl Commands", "Revisa los comandos disponibles para los usuarios de la liga.")
    ]

    HELP_SETUP_TITLE = "Configuración - Blood Bowl Manager"
    HELP_SETUP_DESCRIPTION = "Sigue los siguientes pasos para configurar tu liga en Blood Bowl Manager Bot"
    HELP_SETUP_FIELDS = [
        ("#1 Permite a GoblinSpy recuperar los datos de tu torneo.", "Entra a http://www.mordrek.com/goblinSpy/web/activate.html? e introduce los datos de tu torneo. Después, haz click en el botón de \"Activate\".")
        ,("#2 Configura el torneo en el bot", "Utiliza ```bb2!config \"Nombre de la liga\" \"Nombre del torneo\"```, incluyendo las comillas, para configurar el torneo.")
        ,("#3 Instala los emojis", "Descarga e instala este paquete de emojis para tener una mejor experiencia de usuario")
    ]

    HELP_COMMAND_TITLE = "Comandos - Blood Bowl Manager"
    HELP_COMMAND_DESCRIPTION = "Puedes utilizar los siguientes comandos para ver y controlar tus partidos. Los partidos pueden tardar un poco en actualizarse"
    HELP_COMMAND_FIELDS = [
        ("```bb2!teams```", "Muestra todos los equipos de la competición"),
        ("```bb2!round <round number>```", "Muestra los partidos de la ronda seleccionada. Si no se especifica ninguna, se monstrarán los datos de la ronda actual."),
        ("```bb2!register <coach name>```", "Vincula tu usuario de discord a tu nombre de entrenador, permitiendote acceder a otras características."),
        ("```bb2!next```", "Muestra el siguiente partido de tu equipo"),
        ("```bb2!date <DD-MM-YYYY hh:mm>```", "Indica un día y hora para jugar el siguiente partido. Si tu rival está registrado, le llegará una notificación"),
        ("```bb2!accept```", "Acepta la fecha que ha propuesto tu rival y se le notificará.")
    ]

    INFO_MATCHCREATED = "Tu próximo partido de la liga %s en el torneo %s, es contra %s.\nTu oponente te propone jugar el %s. Vuelve al servidor de la liga y utiliza ```bb2!accept``` para aceptar la hora ```bb2!decline``` para rechazarla."
    INFO_MATCHUPDATED = "Tu oponente ha modificado la fecha propuesta para el partido del torneo %s en la liga %s y ahora propone jugar el %s. Vuelve al servidor de la liga y utiliza ```bb2!accept``` para aceptar la hora ```bb2!decline``` para rechazarla."
    INFO_USERACCEPT = "¡Tu oponente ha aceptado!. El partido se debería jugar el %s"
    ROUND= "Ronda %s"
    TEAM_NAME = "Nombre del equipo"
    COACH = "Entrenador"
    LAST_UPDATE = "Últuma actualización el %s"
    LOCAL_TEAM = "Equipo Local"
    VS = "VS"
    VISITOR_TEAM = "Equipo Visitante"
    NEXT_MATCH = "Próximo partido"
    NEAR_MATCH_TITLE= "¡*%s VS %s* está a punto de comenzar!"
    NEAR_MATCH_DESCRIPTION = "Está previsto que el partido empiece a las %s, ¡Id buscando los pompones y a animar!"
    LANGUAGE_UPDATED = "Ok! Pues a hablar la lengua del imperio, 0 dramas."
    DM_SENDED = "Te he enviado la información por mensaje privado :)"

class EU:
    SUCCESS_SERVER_CONFIGURED = "Zerbitzaria era egokian konfiguratu da!"
    SUCCESS_SERVER_RESET = "Zerbitzariaren konfigurazioa berrabiarazi da!"
    SUCCESS_IAM_REGISTER = "Era egokian erregistratu zara!"
    SUCCESS_IAM_UPDATE =  "Zure entrenatzaile izena eguneratu da!"
    SUCCESS_ESTABLISHDATE_UPDATE= "Pariduaren data eguneratu da!"
    SUCCESS_ESTABLISHDATE_REGISTER="¡Partiduaren data berretsi da!"
    SUCCESS_MATCH_ACCEPTED = "Partidua onartu da!"
    NEXTMATCH_TIME_DEFINED = "Partiduaren eguna eta ordua %s berretsi da."
    NEXTMATCH_TIME_DEFINED_USER_NO_ACCEPTED = "Zure aurkaria %s-ean jokatzea proposatu dizu, baina oraindik ez duzu data onartu. Erabili ```bb2!accept``` ordua onartzeko."
    NEXTMATCH_TIME_DEFINED_RIVAL_NO_ACCEPTED = "%s egunean jokatzea proposatu duzu, baina zure aurkaria ez du topaketa onartu."

    NEXTMATCH_TIME_NON_DEFINED = "Oraindik ez duzu topaketaren data zehaztu. Erabili ```bb2!register DD/MM/YYY HH:mm``` hori egiteko."
    NEXTMATCH_GAME_PLAYED = "Txanda hau jadanik jokatu duzu!"
    ERROR_ACCEPT_NOMATCH = "Ez daukazu partidurik onartzeke."
    ERROR_DEFAULT = "Errore bat gertatu da. Saiatu berriz beranduago."
    ERROR_ESTABLISHDATE_INVITED = "Zure aurkaria partiduaren ordua proposatu du. Erabili ```bb2!next``` proposatutako ordua berrikusteko eta ```bb2!accept``` berresteko."
    ERROR_ESTABLISHDATE_MATCHERROR = "Errorea: Ez da hurrengo partidua aurkitu."
    ERROR_SYNTAX_ESTABLISHDATE = "Errorea: Komando baliogabea. Mesedez, erabili ```bb2!register DD/MM/YYYY HH:mm``` partiduaren data zehaztu edo eguneratzeko"
    ERROR_NOT_CONFIGURED="Errorea: Ez dafo lehiaketarik konfiguratuta"
    ERROR_ALREADY_CONFIGURED = "Errorea: Zerbitzaria jadanik konfiguratuta dago. Berrabiarazi konfigurazioa liga berriro hautatzeko."
    ERROR_NOT_ALLOWED = "Errorea: Soilik administraitzaileek egin dezakete ekintza hau"
    ERROR_DATA_NOT_FOUND = "Errorea: Ezin izan dira datuak aurkitu. Gogoratu konfigurazioaren pausak jarraitzea, eta horrela egin badezu, izan kontutan GoblinSpy ordu batzuk eman ditzakela zure datuak lehenengo alfiz eskuratzen."
    ERROR_NOT_SCHEDULE = "Errorea: Ez da lehiaketa honerako egutegirik aurkitu."
    ERROR_SYNTAX_CONFIGURATION = "Errorea: Sintaxis inválida. Por favor, utiliza ```bb2!configure \"league name\" \"tournament name\"```, incluyendo las comillas, para configurar el servidor."
    ERROR_SYNTAX_IAM = "Errorea: Sintaxi desegokia. Mesedez, erabili ```bb2!register {entrenatzaile izena}``` zure bloodbowl kontua discordekin estekatzeko"
    ERROR_NOT_REGISTERED = "Errorea: Oraindik ez zara identifikatu. Mesedez, erabili ```bb2!register {entrenatzaile izena}``` zure bloodbowl kontua discordekin estekatzeko"
    ERROR_ALREADY_REGISTERED = "Errorea: Norbaitek entranitzaile hau bezala izena eman du. Zure entrenatzaile izen bada jarri kontaktuan administratzaile batekin."
    ERROR_INCORRECT_ROUND="Errorea: Txanda '%s' ez da existitzen."
    ERROR_LANGUAGE_INVALID = "Errorea: Autatutako hizkuntza ez da egokia edo ez dago erabilgarri. Erabili ```bb2!help``` informazio gehiagorako."
    ERROR_INVALID_COMMAND="Errorea. Sartutako komandoa ez da egokia. Erabili ```bb2!help``` informazio gehiagorako"

    BOT_THUMBAIL = "https://i.imgur.com/8eptQlM.png"

    HELP_GENERIC_TITLE = "Blood Bowl Kudeatzailea"
    HELP_GENERIC_DESCRIPTION = "Kapitulu bat ikusteko, kapituluaren zenbakia gehitzearekin nahikoa da bb2!help ostean.\nAdibidez: ```bb2!help 2```"
    HELP_GENERIC_FIELDS = [
        ("Kapitulu 1: Konfiguratu zure lehiaketa", "Berrikusi nola konfiguratu eta zure lehenengo pausuak eman Blood Bowl Manager Bot-ekin")
        ,("Kapitulu 2: Blood Bowl Komandoak", "Berrikusi ligaren erabiltzaileentzako aukeran dauden komandoak.")
    ]

    HELP_SETUP_TITLE = "Konfigurazioa - Blood Bowl Kudeatzailea"
    HELP_SETUP_DESCRIPTION = "Jarraitu hurrengo pausuak zure liga Blood Bowl Kudeatsaile Bot-ean konfiguratzeko" 
    HELP_SETUP_FIELDS = [
        ("#1 Baimendu GoblinSpy zure lehiaketaren datuak eskuratzeko.", "Sartu http://www.mordrek.com/goblinSpy/web/activate.html? eta sartu zure lehiaketaren datuak. Ondoren egin klik \"Activate\" botoian.")
        ,("#2 Konfiguratu lehiaketa bot-ean", "Erabili ```bb2!config \"Ligaren izena\" \"Lehiaketaren izena\"```, komilak barne, zure lehiaketa konfiguratzeko.")
        ,("#3 Instalatu emojiak", "Descargatu eta instalatu emoji pakete hau erabiltzaile esperientzia hobea izateko")
    ]

    HELP_COMMAND_TITLE = "Komandoak - Blood Bowl Kudeatsailea"
    HELP_COMMAND_DESCRIPTION = "Erbaili hurrengo komandoak zure partiduak ikusi eta kudeatseko. Baliteke partiduak denbora bat ematea eguneraketan."
    HELP_COMMAND_FIELDS = [
        ("```bb2!teams```", "Lehiaketaren talde guztiak ikusteko"),
        ("```bb2!round <txandaren zenbakia>```", "Hautatutako txandarenb partiduak erakusten ditu. Ez bada txandaren zenbakirik zehasten, jokatzen ari den txandaren datuak erkutsiko ditu."),
        ("```bb2!register <entrenatzaile izena>```", "Estekatu diskord erabiltzaile izena eta entrenatzaile izena, horrela ezaugarri gehigarriak ahalbidetuz."),
        ("```bb2!next```", "Erakutsi zure taldearen hurrengo partidua"),
        ("```bb2!date <DD-MM-YYYY hh:mm>```", "Hurrengo partiduaren data eta ordua zehaztu. Zure aurkaria izena eman badu, abisu bat helduko zaio"),
        ("```bb2!accept```", "Berretsi zure aurkariak proposatutako ordua eta aurkaria abisatu.")
    ]

    INFO_MATCHCREATED = "Zure hurrengo partidua %s ligan %s lehiaketan, %s-ren aurka da.\nzure aurkaria %s-an jolastea proposatzen du. Bueltatu ligaren zerbitzarira eta erabili ```bb2!accept``` ordua berresteko edo ```bb2!decline``` ezetza adierazteko."
    INFO_MATCHUPDATED = "Zure aurkaria lehiaketa %s ligan %s partiduarentzako proposatutako data aldatu du eta orain %s jokatzea proposatzen du. Bueltatu ligaren zerbitzarira eta erabili  ```bb2!accept``` komandoa ordua berresteko edo ```bb2!decline``` ezetza adierazteko."
    INFO_USERACCEPT = "Zure aurkaria onartu du!. Partidua %s jokatuko da."
    ROUND= "Txanda %s"
    TEAM_NAME = "Taldearen izena"
    COACH = "Entrenatzailea"
    LAST_UPDATE = "Azkenego eguneraketa %s-n izan da"
    LOCAL_TEAM = "Etxeko taldea"
    VS = "VS"
    VISITOR_TEAM = "Kanpoko taldea"
    NEXT_MATCH = "Hurrengo partidua"
    NEAR_MATCH_TITLE= "*%s VS %s* Momentu batzuk barru hasiko da!"
    NEAR_MATCH_DESCRIPTION = "Partidua %s-tan hasiko da, bilatu ponpoiak eta animatzera!"
    LANGUAGE_UPDATED = "Ondo! Jainkoa eta lege zarra, aurrera bolie!."
    DM_SENDED = "Mezu pribatu bat bidali dizut informazioarekin :)"

class CAT:
    SUCCESS_SERVER_CONFIGURED = "¡Servidor configurado correctamente!"
    SUCCESS_SERVER_RESET = "¡Se ha reiniciado la configuración del servidor!"
    SUCCESS_IAM_REGISTER = "¡Te has registrado correctamente!"
    SUCCESS_IAM_UPDATE =  "¡Se ha actualizado tu nombre de entrenador!"
    SUCCESS_ESTABLISHDATE_UPDATE= "¡Se ha actualizado la fecha del partido!"
    SUCCESS_ESTABLISHDATE_REGISTER="¡Se ha establecido la fecha del partido!"
    SUCCESS_MATCH_ACCEPTED = "¡Patido aceptado!"
    NEXTMATCH_TIME_DEFINED = "Se ha establecido el día y hora %s para el partido."
    NEXTMATCH_TIME_DEFINED_USER_NO_ACCEPTED = "Tú oponente te ha propuesto jugar el %s, pero aún no has aceptado. Utiliza ```bb2!accept``` para aceptar la hora."
    NEXTMATCH_TIME_DEFINED_RIVAL_NO_ACCEPTED = "Has propuesto jugar el %s, pero tu rival aún no ha aceptado el encuentro."

    NEXTMATCH_TIME_NON_DEFINED = "Aún no habéis definido la fecha del encuentro. Usa ```bb2!register DD/MM/YYY HH:mm``` para hacerlo."
    NEXTMATCH_GAME_PLAYED = "¡Ya has jugado esta ronda!"
    ERROR_ACCEPT_NOMATCH = "No tienes ningún partido pendiente de ser aceptado."
    ERROR_DEFAULT = "Ha ocurrido un error. Vuelve a intentarlo más tarde."
    ERROR_ESTABLISHDATE_INVITED = "Tu rival ya ha propuesto la hora del partido. Utiliza ```bb2!next``` para revisar la hora propuest y ```bb2!accept``` para aceptar."
    ERROR_ESTABLISHDATE_MATCHERROR = "Error: No se ha encontrado el próximo partido."
    ERROR_SYNTAX_ESTABLISHDATE = "Error: Comando inválido. Por favor, utilice ```bb2!register DD/MM/YYYY HH:mm``` para establecer o actualizar la hora del partido"
    ERROR_NOT_CONFIGURED="Error: No hay ningún torneo configurado"
    ERROR_ALREADY_CONFIGURED = "Error: El servidor ya está configurado. Reinicie la configuración antes si desea volver a seleccionar la liga"
    ERROR_NOT_ALLOWED = "Error: Solo los administradores pueden realizar esta acción"
    ERROR_DATA_NOT_FOUND = "Error: No se han encontrado los datos. Recuerda seguir los pasos de configuración y, si ya lo has hecho, ten en cuenta que GoblinSpy puede tardar unas horas en recuperar los datos la primera vez."
    ERROR_NOT_SCHEDULE = "Error: No se ha encontrado ningún calendario para este torneo."
    ERROR_SYNTAX_CONFIGURATION = "Error: Sintaxis inválida. Por favor, utiliza ```bb2!configure \"league name\" \"tournament name\"```, incluyendo las comillas, para configurar el servidor."
    ERROR_SYNTAX_IAM = "Error: Sintaxis inválida. Por favor, utilice ```bb2!register {nombre de entrenador}``` para vincular tu cuenta de BloodBowl a Discord"
    ERROR_NOT_REGISTERED = "Error: Aún no te has identificado. Por favor, utilice ```bb2!register {nombre de entrenador}``` para vincular tu cuenta de BloodBowl a Discord"
    ERROR_ALREADY_REGISTERED = "Error: Alguien se ha registrado ya como este entrenador. Si es tu nombre de entrenador ponte en contacto con un administrador."
    ERROR_INCORRECT_ROUND="Error: La ronda '%s' no existe."
    ERROR_LANGUAGE_INVALID = "Error: El idioma seleccionado no es válido o no está disponible. Utiliza ```bb2!help``` para más información."
    ERROR_INVALID_COMMAND="Error. El comando introducido el inválido. Utiliza ```bb2!help``` para más información"

    BOT_THUMBAIL = "https://i.imgur.com/8eptQlM.png"

    HELP_GENERIC_TITLE = "Blood Bowl Manager"
    HELP_GENERIC_DESCRIPTION = "Para ver un capítulo, sencillamente añade el número del capítulo al final del comando de bb2!help.\nPor ejemplo: ```bb2!help 2```"
    HELP_GENERIC_FIELDS = [
        ("Chapter 1: Configura tu torneo", "Revisa como configurar y dar los primeros pasos en Blood Bowl Manager Bot")
        ,("Chapter 2: Blood Bowl Commands", "Revisa los comandos disponibles para los usuarios de la liga.")
    ]

    HELP_SETUP_TITLE = "Configuración - Blood Bowl Manager"
    HELP_SETUP_DESCRIPTION = "Sigue los siguientes pasos para configurar tu liga en Blood Bowl Manager Bot"
    HELP_SETUP_FIELDS = [
        ("#1 Permite a GoblinSpy recuperar los datos de tu torneo.", "Entra a http://www.mordrek.com/goblinSpy/web/activate.html? e introduce los datos de tu torneo. Después, haz click en el botón de \"Activate\".")
        ,("#2 Configura el torneo en el bot", "Utiliza ```bb2!config \"Nombre de la liga\" \"Nombre del torneo\"```, incluyendo las comillas, para configurar el torneo.")
        ,("#3 Instala los emojis", "Descarga e instala este paquete de emojis para tener una mejor experiencia de usuario")
    ]

    HELP_COMMAND_TITLE = "Comandos - Blood Bowl Manager"
    HELP_COMMAND_DESCRIPTION = "Puedes utilizar los siguientes comandos para ver y controlar tus partidos. Los partidos pueden tardar un poco en actualizarse"
    HELP_COMMAND_FIELDS = [
        ("```bb2!teams```", "Muestra todos los equipos de la competición"),
        ("```bb2!round <round number>```", "Muestra los partidos de la ronda seleccionada. Si no se especifica ninguna, se monstrarán los datos de la ronda actual."),
        ("```bb2!register <coach name>```", "Vincula tu usuario de discord a tu nombre de entrenador, permitiendote acceder a otras características."),
        ("```bb2!next```", "Muestra el siguiente partido de tu equipo"),
        ("```bb2!date <DD-MM-YYYY hh:mm>```", "Indica un día y hora para jugar el siguiente partido. Si tu rival está registrado, le llegará una notificación"),
        ("```bb2!accept```", "Acepta la fecha que ha propuesto tu rival y se le notificará.")
    ]

    INFO_MATCHCREATED = "Tu próximo partido de la liga %s en el torneo %s, es contra %s.\nTu oponente te propone jugar el %s. Vuelve al servidor de la liga y utiliza ```bb2!accept``` para aceptar la hora ```bb2!decline``` para rechazarla."
    INFO_MATCHUPDATED = "Tu oponente ha modificado la fecha propuesta para el partido del torneo %s en la liga %s y ahora propone jugar el %s. Vuelve al servidor de la liga y utiliza ```bb2!accept``` para aceptar la hora ```bb2!decline``` para rechazarla."
    INFO_USERACCEPT = "¡Tu oponente ha aceptado!. El partido se debería jugar el %s"
    ROUND= "Ronda %s"
    TEAM_NAME = "Nombre del equipo"
    COACH = "Entrenador"
    LAST_UPDATE = "Últuma actualización el %s"
    LOCAL_TEAM = "Equipo Local"
    VS = "VS"
    VISITOR_TEAM = "Equipo Visitante"
    NEXT_MATCH = "Próximo partido"
    NEAR_MATCH_TITLE= "¡*%s VS %s* está a punto de comenzar!"
    NEAR_MATCH_DESCRIPTION = "Está previsto que el partido empiece a las %s, ¡Id buscando los pompones y a animar!"
    LANGUAGE_UPDATED = "¿Por qué quieres hablar lenguas muertas?"
    DM_SENDED = "Te he enviado la información por mensaje privado :)"

#!/usr/bin/python3
from discord.ext.commands import CommandNotFound
import os, commands, asyncio
import sqlite3
import goblinSpy, crud, constants.dictionaries as dictionaries
import discord, datetime, constants.texts as texts
from dotenv import load_dotenv
from discord.ext import commands as discord_commands, tasks
import threading 
class Bot:
    def __init__(self):
        # 
        self.client = discord_commands.Bot(os.getenv('DISCORD_PREFIX'))
        self.token = os.getenv('DISCORD_TOKEN')
        self.client.remove_command('help')
        self.index = 0
        self.crud = crud.Crud()
        @self.client.event
        async def on_ready():
            self.schedule_reader.start()

        # Start command definitions
        @self.client.command()
        #Help command
        async def help(ctx):
            await commands.Commands(ctx).help()

        @self.client.command()
        #Command to config a league on server
        async def config(ctx):
            await commands.Commands(ctx).configure()
        @self.client.command()
        #Command to delete the current configuration league
        async def IWantReset(ctx):
            await commands.Commands(ctx).reset()
        @self.client.command()
        async def IWantDeleteUser(ctx):
            await commands.Commands(ctx).user_delete()
        @self.client.command()
        #Command to show the current tournament teams
        async def teams(ctx):
            await commands.Commands(ctx).teams()
        @self.client.command()
        #Command to show the current round or the specified by parameter
        async def round(ctx):
            await commands.Commands(ctx).round()
        @self.client.command()
        async def register(ctx):
            await commands.Commands(ctx).user_register()
        @self.client.command()
        async def next(ctx):
            await commands.Commands(ctx).my_next_match()
        @self.client.command()
        async def date(ctx):
            await commands.Commands(ctx).establish_date_match()
        @self.client.command()
        async def accept(ctx):
            await commands.Commands(ctx).accept_time()
        @self.client.command()
        async def language(ctx):
            await commands.Commands(ctx).change_language()
        @self.client.command()
        async def close(ctx):
            await commands.Commands(ctx).delete_last_bot_message()        
        # Check near matches every 60 seconds.
        @self.client.event
        async def on_command_error(ctx, error):
            if isinstance(error, discord_commands.CommandError): 
                await commands.Commands(ctx).default()
            else:
                pass
    @tasks.loop(seconds=60)
    async def schedule_reader(self):
        checked_time = datetime.datetime.now() + datetime.timedelta(minutes=30)
        bd_matchesjserver = self.crud.recover_match_programmed_time_close(checked_time)
        embed = discord.Embed(
            colour = discord.Colour.red(),
        )
        if bd_matchesjserver:
            for bd_match in bd_matchesjserver:
                #Recovers the channel ID and send a embed on this channel.  
                channel = self.client.get_channel(bd_match.discord_channel_id)
                language = dictionaries.get_language(bd_match.language)
                embed.title = language.NEAR_MATCH_TITLE % (bd_match.local_team, bd_match.visitor_team)
                embed.description = language.NEAR_MATCH_DESCRIPTION % bd_match.proposed_time
                await channel.send(embed=embed)
                self.crud.delete_match_programmed_time(bd_match.match_contest_id)
    
    def run(self):
        self.client.run(self.token)

if __name__ == "__main__":
    load_dotenv()
    bot = Bot().run()


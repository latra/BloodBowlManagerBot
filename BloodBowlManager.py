#!/usr/bin/python3
import os, commands
import sqlite3
import goblinSpy
import discord
from dotenv import load_dotenv
from discord.ext import commands as discord_commands

class Bot:
    def __init__(self):
        # 
        self.client = discord_commands.Bot(os.getenv('DISCORD_PREFIX'))
        self.token = os.getenv('DISCORD_TOKEN')
        self.client.remove_command('help')
        @self.client.event
        async def on_ready():
            print('Bot up!')
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
        async def reset(ctx):
            await commands.Commands(ctx).reset()
        @self.client.command()
        #Command to show the current tournament teams
        async def teams(ctx):
            await commands.Commands(ctx).teams()
        @self.client.command()
        #Command to show the current round or the specified by parameter
        async def round(ctx):
            await commands.Commands(ctx).round()
        @self.client.command()
        async def Iam(ctx):
            await commands.Commands(ctx).user_register()
        @self.client.command()
        async def nextMatch(ctx):
            await commands.Commands(ctx).my_next_match()
        @self.client.command()
        async def IWillPlay(ctx):
            await commands.Commands(ctx).establish_date_match()
        @self.client.command()
        async def acceptMatch(ctx):
            await commands.Commands(ctx).accept_time()

        
    def run(self):
        self.client.run(self.token)

if __name__ == "__main__":
    load_dotenv()
    Bot().run()


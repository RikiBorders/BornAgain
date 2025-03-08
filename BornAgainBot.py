import discord
from discord.ext import commands
from discord.ui import Button, View
from services.song_class import *
from embed_builder import *
import asyncio
import random
from dotenv import load_dotenv
import os

from Bot import Bot

'''
Implementation loosely based on Goose
'''
bot_instance = Bot()
client = bot_instance.getClient()

def bot_booter():
    load_dotenv()
    token = os.getenv("token")
    client.run(token)

'''
BOT COMMANDS

All Goose bot commands can be found below. Data is managed by the bot_instance global var. 
'''

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

if __name__ == "__main__":
    bot_booter()
    
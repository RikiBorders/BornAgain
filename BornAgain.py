import discord
from discord.ext import commands
from discord.ui import Button, View
from dotenv import load_dotenv
import asyncio
import os

from Bot import Bot

'''
Implementation loosely based on Goose
'''
botInstance = Bot()
client = botInstance.getClient()

def bot_booter():
    load_dotenv()
    token = os.getenv("token")
    client.run(token)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.command()
async def rollDice(ctx, *params):
    
    await ctx.send(botInstance.rollDice(params))

if __name__ == "__main__":
    bot_booter()
    
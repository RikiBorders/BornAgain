import discord
from discord.ext import commands
from discord.ui import Button, View
from dotenv import load_dotenv
import asyncio
import os

from Bot import Bot
from clients.GameSpotClient import GameSpotClient


'''
Implementation loosely based on Goose
'''
botInstance = Bot()
client = botInstance.getClient()

def bot_booter():
    load_dotenv()
    key = os.getenv("DISCORD_KEY")
    client.run(key)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.command()
async def rollDice(ctx, *params):
    if params:
        try:
            faces = int(params[0])
            await ctx.send(botInstance.rollDice(faces))
        except ValueError:
            raise ValueError("The number of faces on the dice must be an integer.")
        
@client.command()
async def test(ctx, *params):
    print(botInstance.getGameSpotArticles())
        
if __name__ == "__main__":
    bot_booter()
    
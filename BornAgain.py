import discord
from discord.ext import commands
from discord.ui import Button, View
from dotenv import load_dotenv
import asyncio
import os
import Utils.input_validation_utils  as input_validation_utils

from Bot import Bot
from Utils.discord_task_utils import *
from Constants import DEFAULT_ROLE_NAME

'''
The everlasting legacy of Wiz, Sayori, Tanaka, and Goose.
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
    createTasks(client, botInstance)


@client.event
async def on_member_join(member):
    # Set the default role for new members
    botInstance.set_role(DEFAULT_ROLE_NAME, member)


@client.command()
async def roll_dice(ctx, *params):
    if params:
        try:
            faces = int(params[0])
        except ValueError:
            raise ValueError("The number of faces on the dice must be an integer.")
        
        await ctx.send(botInstance.rollDice(faces))


if os.getenv("STAGE") == "beta":
    @client.command()
    async def test(ctx, *params):
        await ctx.send("Test command executed successfully.")

        
if __name__ == "__main__":
    bot_booter()
    
import discord
from discord.ext import commands
from discord.ui import Button, View
from dotenv import load_dotenv
import asyncio
import os

from Bot import Bot
from Modules.DiscordTaskModule import *
from clients.GameSpotClient import GameSpotClient
from Modules.EmbedBuilder import *
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
    role = discord.utils.get(member.guild.roles, name=DEFAULT_ROLE_NAME)
    if role:
        await member.add_roles(role)
        print(f"Assigned default role {role.name} to new member {member.name}")


@client.command()
async def rollDice(ctx, *params):
    if params:
        try:
            faces = int(params[0])
            await ctx.send(botInstance.rollDice(faces))
        except ValueError:
            raise ValueError("The number of faces on the dice must be an integer.")


# This command is used to trigger test scenarios. This will be inactive in prod.
@client.command()
async def test(ctx, *params):
    # TODO abstract this away into a 5 min coroutine and save results in memory (measure performance first)
    # otherwise, store in a DB. 
    articles = botInstance.getGameSpotArticles()
    artcileEmbed = buildGameSpotArticleEmbed(articles[0])
    await ctx.send(embed=artcileEmbed.embed, view=artcileEmbed.view)


        
if __name__ == "__main__":
    bot_booter()
    
from discord import app_commands
from discord.ext import commands
from discord.ext import commands
from discord.ui import Button, View
from dotenv import load_dotenv
import asyncio
import os

from Bot import Bot
from util.embed_utils import *
from util.discord_task_utils import *
from constant.Constants import DEFAULT_ROLE_NAME

'''
The everlasting legacy of Wiz, Sayori, Tanaka, and Goose.
'''
botInstance = Bot()
client = botInstance.get_client()

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
    if botInstance.has_default_role():
        default_role_name = botInstance.get_default_role()
        await botInstance.set_role(default_role_name, member)

    system_channel_id = member.guild.system_channel.id
    member_count = len([m for m in member.guild.members if not m.bot])
    channel = await client.fetch_channel(system_channel_id)

    await channel.send(
        embed=build_welcome_embed(member_count).to_discord_embed()
    )

@client.tree.command(
        name="help", 
        description="Displays the BornAgain help menu",
        guild=discord.Object(id=367021007690792961) #TODO: save this to the bot state and use it to key into server specific configurations
)
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(
        ephemeral=True,
        embed=build_help_embed().to_discord_embed()
    )

# Test commands available only in the beta environment

# This command needs to be run to register the slash commands with Discord
@client.command()
async def sync_commands(ctx, *params):
    if os.getenv("STAGE") == "beta":
        await client.tree.sync(guild=ctx.guild)
        await ctx.send("Commands synced")

        
if __name__ == "__main__":
    bot_booter()
    
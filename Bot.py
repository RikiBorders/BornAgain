import discord
from discord.ext import commands

class Bot():
    def __init__(self):
        self.client = self.setUpClient()

    def setUpClient():
        intents = discord.Intents.all()
        intents.voice_states = True
        client = commands.Bot(command_prefix='.', intents=intents)
        client.remove_command('help')

        return client
    
    def getClient(self):
        return self.client
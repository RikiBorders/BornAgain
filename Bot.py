import discord
from discord.ext import commands

from BotUtils import BotUtils

class Bot():
    def __init__(self):
        self.client = self.setUpClient()
        print("Bot initialized")

    def setUpClient(self):
        intents = discord.Intents.all()
        intents.voice_states = True
        client = commands.Bot(command_prefix='.', intents=intents)
        client.remove_command('help')

        return client
    
    def getClient(self):
        return self.client
    
    def rollDice(self, params):
        if params:
            try:
                faces = int(params[0])
                return BotUtils.rollDice(self, faces)
            except ValueError:
                raise ValueError("The number of faces on the dice must be an integer.")
    
    
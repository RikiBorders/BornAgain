import discord
from discord.ext import commands

from BotUtils import BotUtils
from adapters.GameSpotClientAdapter import GameSpotClientAdapter


class Bot():
    def __init__(self):
        self.client = self.setUpClient()
        self.gameSpotClientAdapter = GameSpotClientAdapter()
        print("Bot initialized")

    def setUpClient(self):
        intents = discord.Intents.all()
        intents.voice_states = True
        client = commands.Bot(command_prefix='.', intents=intents)
        client.remove_command('help')

        return client
    
    def getClient(self):
        return self.client
    
    def rollDice(self, faces):
        return BotUtils.rollDice(self, faces)
    
    def getGameSpotArticles(self):
        return self.gameSpotClientAdapter.getArticles() 

    
    
import discord
from discord.ext import commands

from BotUtils import BotUtils

class Bot():
    def __init__(self):
        self.client = self.setUpClient()
        self.introTimer = {
            'active': False, 
            'current_time': 0
        }
        
        print("Bot initialized", flush=True)

    def setUpClient(self):
        intents = discord.Intents.all()
        intents.voice_states = True
        client = commands.Bot(command_prefix='.', intents=intents)
        client.remove_command('help')

        return client
    
    def getClient(self):
        return self.client
    
    def roll_dice(self, faces):
        return BotUtils.rollDice(self, faces)
    
    def set_intro_timer(self, status: bool, time_in_seconds: int):
        self.introTimer['active'] = status
        self.introTimer['timer'] = time_in_seconds

    async def set_role(self , role_name: str, member):
        role = discord.utils.get(member.guild.roles, name=role_name)
        if role:
            await member.add_roles(role)
            print(f"Assigned default role {role.name} to new member {member.name}")

    def is_intro_timer_active(self):
        return self.introTimer['active']

    
    
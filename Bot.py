import discord
from discord.ext import commands
import json

from exception.recdord_not_found_exception import RecordNotFoundError
from helper.channel_registry_helper import ChannelRegistryHelper
from client.supabase_client import SupabaseClient

class Bot():
    def __init__(self):
        self.client = self.create_client()
        self.channel_registry_helper = ChannelRegistryHelper()
        self.guild_id = self.set_guild_id()
        self.introTimer = {
            'active': False, 
            'current_time': 0
        }
        self.supabase_client = SupabaseClient()
        self.server_data = self.get_server_data_from_supabase()

        self.register_channels()
        print("Bot initialized", flush=True)

    def register_channels(self):
        
        self.channel_registry_helper.register_channel("command", self.server_data['channels']['command_channel_id']) 
        self.channel_registry_helper.register_channel("welcome", self.server_data['channels']['welcome_channel_id'])

    def create_client(self):
        intents = discord.Intents.all()
        intents.voice_states = True
        client = commands.Bot(command_prefix='.', intents=intents)
        client.remove_command('help')

        return client
    
    def get_client(self):
        return self.client

    def get_channel_by_channel_type(self, channel_type: str) -> discord.TextChannel | discord.VoiceChannel:
        '''
        retrieve a discord channel object by its registered channel type. Can return
        TextChannel or VoiceChannel.
        '''
        channel_id: int = self.channel_registry_helper.get_channel(channel_type)

        if channel_id:
            return self.client.get_channel(channel_id)
        else:
            raise ValueError(f"Channel type not found, or unset: {channel_type}")

    def get_channel_id_from_supabase(self, channel_type: str) -> int:
        response = self.supabase_client.get_channels(self.guild_id)

        # The PostgREST client returns an object with a `data` attribute.
        # `data` is usually a list of rows or a single dict depending on the query.
        data = getattr(response, "data", None)
        if not data:
            return None

        # Normalize to a single row dict
        row = data[0] if isinstance(data, list) else data

        # The `channels` column may already be a dict or a JSON string.
        channels = row.get("channels") if isinstance(row, dict) else None
        if not channels or not isinstance(channels, dict):
            return None

        if isinstance(channels, str):
            try:
                channels = json.loads(channels)
            except json.JSONDecodeError:
                channels = None

        channel_id = channels.get(channel_type)
        return int(channel_id) if channel_id is not None else None
    
    def get_server_data_from_supabase(self) -> dict:
        response = self.supabase_client.get_server_data(self.guild_id)

        data = getattr(response, "data", None)
        if not data:
            raise RecordNotFoundError(f"Server data not found for guild_id {self.guild_id}")

        columns = data[0] if isinstance(data, list) else data
        return columns if isinstance(columns, dict) else {}
    
    def get_default_role(self) -> Optional[int]:
        return self.server_data['default_role']
    
    def has_default_role(self) -> bool:
        default_role = self.server_data['default_role']
        return True if default_role else False

    def is_intro_timer_active(self):
        return self.introTimer['active']

    def set_guild_id(self) -> int:
        # For now, return a hardcoded guild ID. In the future, this could be dynamic.
        return 367021007690792961
    
    def set_intro_timer(self, status: bool, time_in_seconds: int):
        self.introTimer['active'] = status
        self.introTimer['timer'] = time_in_seconds

    async def set_role(self , role_name: str, member):
        role = discord.utils.get(member.guild.roles, name=role_name)
        if role:
            await member.add_roles(role)
            print(f"Assigned default role {role.name} to new member {member.name}")


    
    
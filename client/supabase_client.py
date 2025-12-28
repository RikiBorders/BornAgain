from dotenv import load_dotenv
import os
from supabase import create_client, Client

class SupabaseClient:
    def __init__(self,):
        load_dotenv()
        self.url = os.environ.get("SUPABASE_URL")
        self.key = os.environ.get("SUPABASE_KEY")
        self.password = os.environ.get("SUPABASE_PASSWORD")

        # Initialize connection to Supabase here
        self.client = create_client(self.url, self.key)
        print("Supabase client initialized", flush=True)

    def get_client(self) -> Client:
        return self.client
    
    def get_channels(self, guild_id: int) -> dict:
        response = (
            self.client
            .table("server_configurations")
            .select("channels")
            .eq("guild_id", guild_id)
            .execute()
        )

        return response
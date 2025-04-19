from clients.RequestClient import RequestClient
from dotenv import load_dotenv
import os
# Add the parent directory to sys.path

class GameSpotClient(RequestClient):
    def __init__(self):
        super().__init__()
        load_dotenv()
        self.key = os.getenv("GAMESPOT_KEY")

    def getArticles(self):
        requestUrl = f"https://www.gamespot.com/api/articles/?api_key={self.key}"
        return self.sendRequest(requestUrl)
    
if __name__ == "__main__":
    client = GameSpotClient()
    print(client.getArticles())
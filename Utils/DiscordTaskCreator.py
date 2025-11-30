import asyncio
from Constants import GAMESPOT_COROUTINE_WAIT_TIME_IN_SECONDS

def createTasks(client, botInstance):
    pass

        
# DEPRECATED
async def checkForGameSpotArticles(client, botInstance):
    await client.wait_until_ready()
    
    while not client.is_closed():
        await asyncio.sleep(GAMESPOT_COROUTINE_WAIT_TIME_IN_SECONDS)
from clients.GameSpotClient import GameSpotClient
from Modules.EmbedBuilder import buildGameSpotArticleEmbed
import discord
import asyncio
from Constants import GAMESPOT_COROUTINE_WAIT_TIME_IN_SECONDS

def createTasks(client, botInstance):
    client.loop.create_task(checkForGameSpotArticles(client, botInstance))
    
async def checkForGameSpotArticles(client, botInstance):
    await client.wait_until_ready()
    channel = client.get_channel(954544663933628469)  # Replace with your channel ID. TODO: make this configurable.
    gameSpotClientAdapter = botInstance.gameSpotClientAdapter
    
    while not client.is_closed():
        articles = gameSpotClientAdapter.getArticles()
        if articles:
            for article in articles:
                embed = buildGameSpotArticleEmbed(article)
                await channel.send(embed=embed.embed, view=embed.view)
                break  # Send only the first article. TODO: make this configurable.
            
        await asyncio.sleep(GAMESPOT_COROUTINE_WAIT_TIME_IN_SECONDS)
import asyncio 
import discord 
from discord import Webhook
import aiohttp 

async def anything(url):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(url, session=session)
        embed = discord.Embed(title="This is from a webhook!")
        await webhook.send(embed=embed, username="WebHookMaster")
        
if __name__ == "__main__":
    url = "https://discordapp.com/api/webhooks/1093308698069307463/utJx-XM0aBiidQvZj2Kz60MqSlAgLRfpe8x3qvAEUhpCFdkfqPUG7bY7FaYBBVkhqkP4"

    loop = asyncio.new_event_loop()
    loop.run_until_complete(anything(url))
    loop.close()
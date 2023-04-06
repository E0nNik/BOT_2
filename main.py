import settings
import discord 
from discord.ext import commands
import os
import asyncio
    
logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event 
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
    
#odpowiada za import z cogs
    
    async def load():
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
            #usuwanie .py
                 await bot.load_extension(f'cogs.{filename[:-3]}')

    async def main():
        await load()
        

   
        
    asyncio.run(main())

    bot.run(settings.DISCORD_API_SERCRET, root_logger=True)
        
    

if __name__ == "__main__":
    run()
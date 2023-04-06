import settings
import discord
import random
from discord.ext import commands

logger = settings.logging.getLogger("bot")



       

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    #info do logow
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")


    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("handled error globallyy")   
    #pomoc
    
    @bot.command()
    async def add(ctx, one : int , two : int ):
        await ctx.send(one + two)    


  
    bot.run(settings.DISCORD_API_SERCRET, root_logger=True)
     

if __name__ == "__main__":
    run()
import random
import settings
import discord 
from discord.ext import commands
    
logger = settings.logging.getLogger("bot")
    
def run():
    intents = discord.Intents.default()
    intents.message_content = True
    
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event 
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
    #menu
    @bot.command()
    async def ping(ctx):
        embed = discord.Embed(
            colour=discord.Colour.dark_teal(), 
            description="A tu opis", 
            title="Tu bedzie jakis zajebisty tytul"
        )
        
        embed.set_footer(text="Wpadaj Mordo")
        embed.set_author(name="CryptoStasiak", url="https://www.youtube.com/@cryptostasiak8163")
        
        embed.set_thumbnail(url="https://yt3.ggpht.com/GiBCvnzO8e3_cPclwtRCUqLye86F0_xNOPK0FYeshaths5DO2SLvJq9cBVZ0BL-oNwjt90huIw=s108-c-k-c0x00ffffff-no-rj")
        embed.set_image(url="https://i.ytimg.com/vi/SoqYG_5pQBA/maxresdefault.jpg")
        
        embed.add_field(name="Channel", value="https://www.youtube.com/channel/UCIJe3dIHGq1lIAxCCwx8eyA", inline=False)
        embed.add_field(name="Website", value="https://cryptostasiak.pl/" )
        embed.insert_field_at(1,name="Tree", value="https://www.youtube.com/@cryptostasiak8163")
        
        await ctx.send(embed=embed)
    
        
    bot.run(settings.DISCORD_API_SERCRET, root_logger=True)

if __name__ == "__main__":
    run()
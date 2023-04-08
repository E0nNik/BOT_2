import random
import settings
import discord 
from discord.ext import commands
    


class embed_messages(commands.Cog):

    def __init__(self, bot):
        bot.client = bot  

    #menu
    @commands.command()
    async def wiad(self, ctx):
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

    @commands.command()
    async def hblabla(self, ctx):
        await  ctx.send("Witaj witaj")
    
        
    

async def setup(bot):
    await bot.add_cog(embed_messages(bot))
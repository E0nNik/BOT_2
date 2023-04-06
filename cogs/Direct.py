import settings
import discord 
from discord.ext import commands

class Direct(commands.Cog):

    def __init__(self, bot):
        bot.client = bot

    @commands.command()
    async def hello(self, ctx):
        await  ctx.send("Witaj witaj")
        
    

    
    @commands.command()
    async def siema(self, ctx):
        await ctx.message.author.send("Jebando")

        #Do niku, jeszcze do ogarniecia
        #user = discord.utils.get(bot.guilds[0].members, nick="E0nNik")
        #if user:
            #await user.send("Hello 2")


async def setup(bot):
    await bot.add_cog(Direct(bot))
        
    


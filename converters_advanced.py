import settings
import discord
import random
from discord.ext import commands

logger = settings.logging.getLogger("bot")

class Slapper(commands.Converter):
    use_nicknames = bool

    def __init__(self, *, use_nickcnames) -> None:
        self.use_nicknames = use_nickcnames
        



    async def convert(self, ctx, argument):
        someone = random.choice(ctx.guild.members)
        nicname = ctx.author
        if self.use_nicknames:
            nickname = ctx.author.nick

        return f"{ctx.author} slaps {someone} with {argument}"

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)
    #info do logow
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
    #pomoc
    @bot.command(
            aliases=['p'],
            help="To jest pomoc",
            description="A to opis",
            brief="this is brief"
    )  
    async def ping(ctx):
        """Answer with pong"""
        await ctx.send("pong")
    #say, ale 1 slowo
    @bot.command()
    async def say(ctx, what = "CO JEST KURWA"):
        
        await ctx.send(what)

    #say, ale cale zdania
    @bot.command()
    async def say2(ctx, *what):
        
        await ctx.send(" ".join(what))

    #randomowy wybor
    @bot.command()
    async def choices(ctx, *options):
        await ctx.send(random.choice(options))

    @bot.command()
    async def joined(ctx, who : discord.Member) :
        await ctx.send(who.joined_at)

    @bot.command()
    async def slap(ctx, reason : Slapper(use_nickcnames=True) ) :
        await ctx.send(reason)
       

    bot.run(settings.DISCORD_API_SERCRET, root_logger=True)

if __name__ == "__main__":
    run()
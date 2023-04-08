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
    
    # Dodanie kodu, który przyznaje rolę "adept"
    @bot.event
    async def on_raw_reaction_add(payload):
        # Sprawdzenie, czy reakcja została dodana do wiadomości, którą chcemy monitorować
        if payload.message_id == 1094377391712911500:
            guild = bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            # Sprawdzenie, czy użytkownik nie jest botem
            if not member.bot:
                # Sprawdzenie, czy reakcja jest zgodna z wymaganą reakcją
                if str(payload.emoji) == '👍':
                    role = discord.utils.get(guild.roles, name='Adepcior')
                    await member.add_roles(role)
                    embed = discord.Embed(
            colour=discord.Colour.dark_teal(), 
            description="A tu opis", 
            title="Dziekujemy za zaakceptowanie regulaminu"
        )
        
        embed.set_footer(text="Wpadaj Mordo")
        embed.set_author(name="CryptoStasiak", url="https://www.youtube.com/@cryptostasiak8163")
        
        
        
        embed.add_field(name="Twitter", value="https://twitter.com/CryptoStasiak", inline=False)
        embed.add_field(name="Website", value="https://cryptostasiak.pl/" )
        embed.insert_field_at(1,name="Youtube", value="https://www.youtube.com/@cryptostasiak8163")
        
        await member.send(embed=embed)



    @bot.event
    async def on_raw_reaction_remove(payload):
        # Sprawdzenie, czy reakcja została usunięta z wiadomości, którą chcemy monitorować
        if payload.message_id == 1094377391712911500:
            guild = bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            # Sprawdzenie, czy użytkownik nie jest botem
            if not member.bot:
                # Sprawdzenie, czy użytkownik ma rolę "adept"
                role = discord.utils.get(guild.roles, name='Adepcior')
                if role in member.roles:
                    await member.remove_roles(role)
                    await member.send('Usunięto rolę "adept", ponieważ usunąłeś/aś reakcję z wiadomości.')
    
                    

    
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

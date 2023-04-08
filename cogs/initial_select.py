import settings
import discord 
from discord.ext import commands
import utils 
    
class initial_select(commands.Cog):

    def __init__(self, bot):
        bot.client = bot

class FavouriteGameSelect(discord.ui.Select):
    def __init__(self):
        options = [ 
                   discord.SelectOption(label="Walic koks", value="cs"),
                   discord.SelectOption(label="Palic", value="mc"),
                   discord.SelectOption(label="Pic", value="f"),
        ]
        super().__init__(options=options, placeholder="Co lubisz robic", max_values=2)

    async def callback(self, interaction:discord.Interaction):
        await self.view.respond_to_answer2(interaction, self.values)
class SurveyView(discord.ui.View):
    answer1 = None 
    answer2 = None 
    
    @discord.ui.select(
        placeholder="Wybierz wiek?",
        options=[
            discord.SelectOption(label="16 - 17", value="16"),
            discord.SelectOption(label="18 - 23", value="18"),
            discord.SelectOption(label="24 - 30", value="24")
        ]        
    )
    async def select_age(self, interaction:discord.Interaction, select_item : discord.ui.Select):
        self.answer1 = select_item.values
        self.children[0].disabled= True
        game_select = FavouriteGameSelect()
        self.add_item(game_select)
        await interaction.message.edit(view=self)
        await interaction.response.defer()

    async def respond_to_answer2(self, interaction : discord.Interaction, choices):
        self.answer2 = choices 
        self.children[1].disabled= True
        await interaction.message.edit(view=self)
        await interaction.response.defer()
        self.stop()
    
def run():
    intents = discord.Intents.all()
    
    
    
    @commands.Cog.listener() 
    async def on_ready():
        await utils.load_videocmds(bot)
    
    @commands.command()
    async def survey(self, ctx):
        view = SurveyView()
        await ctx.send(view=view)
        
        await view.wait()
        
        results = {
            "a1": view.answer1,
            "a2": view.answer2,
        }
        
        await ctx.send(f"{results}")
        await ctx.message.author.send("Dzieki mordo za udzial w ankiecie")
        
        
        
    

async def setup(bot):
    await bot.add_cog(initial_select(bot))
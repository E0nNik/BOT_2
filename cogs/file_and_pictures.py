import pathlib
import random
import logging

import requests

import discord
from discord.ext import commands

import settings

logger = logging.getLogger(__name__)


class file_and_pictures(commands.Cog):

    def __init__(self, bot):
        bot.client = bot




def get_random_dog_image_url():
    url = "https://dog.ceo/api/breeds/image/random"
    res = requests.get(url)
    data = res.json()
    if "message" in data:
        return data["message"]
    return None


@commands.command()
async def dog(ctx: commands.Context):
        random_dog_image = get_random_dog_image_url()
        if not random_dog_image:
            await ctx.message.delete(3)
            return

        embed = discord.Embed(title="Random Dog showed up")
        embed.set_image(url=random_dog_image)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(file_and_pictures(bot))

   



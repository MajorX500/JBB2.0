import discord
from discord.ext import commands
import json
from fuzzywuzzy import fuzz, process
from random import choice, shuffle

class Movies(commands.Cog):
    """All movies saved"""
    def __init__(self, bot):
        self.bot = bot

        @commands.command(name='abc',
                description='watched movie list',
                brief='Watched list')

    async def watched(self, ctx):
        embed = discord.Embed(title = "Movies List",
                description='Something very random xD',
                color=0xEE8700)

        with open(bot.MOVIES_PATH) as f:
          data = json.load(f)

        for key in data:
            for value in data[key]:
                embed.add_field(name = value, value = "dsa", inline=False);

        await ctx.send(embed = embed)

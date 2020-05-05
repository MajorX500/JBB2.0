import discord
from discord.ext import commands
import json
from fuzzywuzzy import fuzz, process

class Movies(commands.Cog):
    """All movies saved"""
    def __init__(self, bot):
        self.bot = bot
        self.movies_dict = json.load(open(bot.MOVIES_PATH, 'r', encoding="utf8"))
    
    @commands.command(name='watched',
                     description='watched movie list',
                     brief='Watched list')
    async def watched(self, ctx):
        await ctx.send(self.movies.dict,'watched')

def setup(bot):
    bot.add_cog(Movies(bot))

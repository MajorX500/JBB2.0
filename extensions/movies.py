import discord
from discord.ext import commands
import json
from fuzzywuzzy import fuzz, process
from random import choice, shuffle

class Movies(commands.Cog):
    """All movies saved"""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='watched',
                     description='watched movie list',
                     brief='Watched list')
    async def watched(self, ctx):
        await ctx.send("djsahdisah")

def setup(bot):
    bot.add_cog(Movies(bot))

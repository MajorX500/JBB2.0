import discord
from discord.ext import commands
import json
from fuzzywuzzy import fuzz, process
from random import choice, shuffle

class Minecraft(commands.Cog):
    """Minecraft"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ip',description='watched movie list',brief='Watched list')
    async def pingpong(self, ctx):
        await ctx.send("Server IP : `go2archie.hopto.org`" + "\n" + "Server Admin : mikinho")


def setup(bot):
    bot.add_cog(Minecraft(bot))

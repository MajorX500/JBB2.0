import discord
from discord.ext import commands
import json
from fuzzywuzzy import fuzz, process
from random import choice, shuffle

class Movies(commands.Cog):
    """Movies"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='!watched',description='the not watched movie list',brief='!Watched list')
    async def notwatched(self, ctx):
        embed = discord.Embed(title = "!Watched Movies List :popcorn:", description=' ', color=0x00FFE5)

        with open('./db/movies.json') as f:
            data = json.load(f)
        
        for value in data["next"]:
            embed.add_field(name = value["nome"], value = "Género: " + value["genero"] + "\n" + "Ano: " + value["ano"], inline=False);

        await ctx.send(embed = embed)
    
    @commands.command(name='watched',description='the watched movie list',brief='Watched list') 
    async def watched(self, ctx):
        embed = discord.Embed(title = "Watched Movies List :popcorn:", description=' ', color=0xFF0000)

        with open('./db/movies.json') as f:
            data = json.load(f)
        
        for value in data["finished"]:
            embed.add_field(name = value["nome"], value = "Género: " + value["genero"] + "\n" + "Ano: " + value["ano"], inline=False);

        await ctx.send(embed = embed)
    
    @commands.command(name='add_movie',description='',brief='')
    async def addmovies(self, ctx, nome, genero, ano):
        if ctx.message.author.id == 525678916019421197 or ctx.message.author.id == 472511559529398293:

            with open('./db/movies.json') as f:
                data = json.load(f)
                temp = data['next']

            # python object to be appended
            y = {"nome":nome, 
                "genero": genero, 
                "ano": ano
                } 
            temp.append(y);
            f.close();
    
            with open("./db/movies.json",'w') as f:
                json.dump(data, f, indent=4)

            await ctx.send("Movie " +nome + " " + genero + " " + ano + " added to !watched")
        else:
            await ctx.send("haha admin go brrrr")

    @commands.command(name='check', description='', brief='')
    async def skipmovie(self, ctx):
        if ctx.message.author.id == 525678916019421197 or ctx.message.author.id == 472511559529398293:
            with open('./db/movies.json') as f:
                data = json.load(f)

            new_data = [];
            i = 1;
        
            new_data_next = [];
            for element in data["next"]:
                if i>1:
                    new_data.append(element);
                else:
                    result = element;
                    i=i+1

            for element in data["finished"]:
                new_data_next.append(element);

            new_data_next.append(result);
            data["next"] = new_data;
            data["finished"] = new_data_next;

            with open('./db/movies.json', 'w') as f:
                data = json.dump(data, f)

            await ctx.send('Watched movie')
        else:
            await cxt.send("haha admin go brrrrr")

    @commands.command(name='user', description='', brief='')
    async def getuser(self, ctx):
        await ctx.send(ctx.message.author)

    @commands.command(name='!admin', description='', brief='')
    async def testpermission(self, ctx):
        if ctx.message.author.id == 525678916019421197 or ctx.message.author.id == 472511559529398293 or ctx.message.author.id == 485178269193207848 or ctx.message.author.id == 423956774593363979:
            await ctx.send('YES :)')
        else:
            await ctx.send('NO :(')


def setup(bot):
    bot.add_cog(Movies(bot))

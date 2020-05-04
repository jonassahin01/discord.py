import discord
import json, random, requests, datetime, time, urllib.request, io, os, aiohttp

from typing import Union
from discord.ext import commands
from discord.utils import get
from random import randint

global mm

class misccommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot






    @commands.command(aliases=['пинг'])
    async def ping(self,ctx):
        await ctx.send(f'Ping {round(client.latency * 1000)}ms')

    @commands.command(aliases=['8ball', '8мяч', 'мяч'])
    async def _8ball(self, ctx, *, question):
        responses = [
                "It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                " You may rely on it.",
                " As I see it, yes.",
                "Most likely.",
                " Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                " My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
        await ctx.send(f'Вопрос: {question}\nОтвет: {random.choice(responses)}')

    @commands.command(aliases=['сказать' , 'сказ'])
    async def say(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send("{}" .format(msg))

    @commands.command(aliases=['utube' , 'youtube'])
    async def YT(self,ctx):
        await ctx.send(f'https://studio.youtube.com/channel/UCbXGt-KFvOw1LvEM-T9KV5A')

    @commands.command(aliases=['Kontakte'])
    async def VK(self,ctx):
        await ctx.send(f'https://vk.com/tr_jonas')


    @commands.command()
    async def user(self, ctx, member: discord.Member = None):
        '''Display informations about given user'''
        member = ctx.author if not member else member

        roles = [role for role in member.roles]

        embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

        embed.add_field(name='ID:', value=member.id)
        embed.add_field(name="Name:", value=member.display_name)
        embed.add_field(name='Acount created at:', value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))
        embed.add_field(name="Joined the server:", value=member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))
        embed.add_field(name=f'Roles({len(roles)}):', value=''.join([role.mention for role in roles]))

        await ctx.send(embed=embed)

    @commands.command()
    async def calculate(self, ctx, a:int, b:int):
        await ctx.send(a+b)

    @commands.command()
    async def subtract(self, ctx, a:int, b:int):
        await ctx.send(a-b)

    @commands.command()
    async def multiply(self, ctx, a:int, b:int):
        await ctx.send(a*b)

    @commands.command()
    async def division(self, ctx, a:int, b:int):
        if b==0:
            ans="0"
        else:
            ans=a/b
        await ctx.send(ans)

    @commands.command()
    async def memo(self,ctx, a:str):
        global mm
        mm=a
        await ctx.send("okay")


    @commands.command()
    async def remind(self,ctx):
        await ctx.send(mm)

    @commands.command(name='bigemoji')
    async def get_emoji_url(self, ctx, emoji: Union[discord.Emoji, discord.PartialEmoji, str]):
        """Sends a big version of an emoji and it's URL of available"""
        if isinstance(emoji, (discord.Emoji, discord.PartialEmoji)):
            await ctx.send(str(emoji.url))
        else:
            await ctx.send(emoji)

def setup(bot):
    bot.add_cog(misccommands(bot))

import discord
import random
import json
import asyncio
import os
from discord.ext import commands
from discord.utils import get


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

def setup(bot):
    bot.add_cog(misccommands(bot))



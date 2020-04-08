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
    async def profile(self,ctx, member : discord.Member):
        embeds = discord.Embed(title=member.name)
        embeds.add_field(name="Status", value= member.status)
        embeds.add_field(name="Role", value= member.top_role)
        embeds.add_field(name="ID", value=member.id)
        embeds.add_field(name="Created", value=member.created_at)
        embeds.add_field(name="Joined", value=member.joined_at)
        embeds.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embeds)

def setup(bot):
    bot.add_cog(misccommands(bot))



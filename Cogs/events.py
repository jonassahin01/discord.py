import discord
import random
import json
import asyncio
import os
from discord.ext import commands
from discord.utils import get

class EventsCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_remove(self,ctx, member):
        print(f'{member} покинул сервер.')
        await ctx.send(f'{member}пока, покинул сервер.')

    @commands.Cog.listener()
    async def on_member_join(self,ctx, member):
        print(f'{member} присоединился к серверу.')
        await ctx.send(f'{member}добро пожаловать, присоединился к серверу.')


    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Эта команда не существует.')

    @commands.Cog.listener()
    async def filter_message(self, message, ctx):
        filter = ["Хуй тебе", "ебать тебя", "блять", "Хуй"]

        for word in filter:
            if message.content.count(word) > 0:
                print("A bad word was said")
                await message.channel.purge(limit=1)
                await ctx.send(f'banned {member.mention}, do not swear')

            elif message.content.count(word) > 0:
                await member.kick
                await ctx.send(f'banned {member.mention}, we told you so')

    @commands.Cog.listener()
    async def convert(self, ctx, argument):
        argument = await commands.MemberConverter().convert(ctx, argument)
        permission = argument.guild_permissions.manage_messages

def setup(bot):
    bot.add_cog(EventsCog(bot))

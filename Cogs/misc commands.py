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
                "Это точно.",
                "Это решительно так.",
                "Без сомнения.",
                "Да, безусловно.",
                "Вы можете положиться на него.",
                "Как я понимаю, да.",
                "Более вероятный.",
                "Прогноз хороший.",
                "Да.",
                "Знаки указывают на да.",
                "Ответить туманно, попробуйте еще раз.",
                "Спросите еще раз позже.",
                "Лучше не говорить тебе сейчас.",
                "Не могу предсказать сейчас.",
                "Сконцентрируйся и спроси снова.",
                "Не рассчитывай на это.",
                "Мой ответ - нет.",
                "Мои источники говорят нет.",
                "Перспектива не очень хорошая.",
                "Очень сомнительно."]
        await ctx.send(f'Вопрос: {question}\nОтвет: {random.choice(responses)}')

    @commands.command(aliases=['сказать' , 'сказ'])
    async def say(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send("{}" .format(msg))

def setup(bot):
    bot.add_cog(misccommands(bot))

#https://www.youtube.com/channel/UCT6NBRtmiuSSIYUKxuCOsOw?view_as=subscriber
#https://vk.com/raizbag

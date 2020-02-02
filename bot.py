import asyncio
import random
from asyncio import queues
import discord
import json
import shutil
import os
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('/help'))
    print('bot is ready')




extensions = ['Cogs.administrator', 'Cogs.events','Cogs.misc commands', 'Cogs.Music']

if __name__ == '__main__':
    for extension in extensions:
        client.load_extension(extension)








client.run('NjcyNjk1MTE3NzczMTQ0MDY2.XjPOcg.kNDxqs-i7PftE_5mj6m2YffMyd8')
#https://discordapp.com/api/oauth2/authorize?client_id=672695117773144066&permissions=8&scope=bot
#NjcyNjk1MTE3NzczMTQ0MDY2.XjPOcg.kNDxqs-i7PftE_5mj6m2YffMyd8

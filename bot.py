import asyncio
import random
from asyncio import queues
import discord
import youtube_dl
import json
import shutil
import os
from discord.ext import commands
from discord.utils import get


client = commands.Bot(command_prefix = '/')
client.remove_command('help')
client.fetch_offline_members = True


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('/help'))
    print('bot is ready')




extensions = ['Cogs.administrator', 'Cogs.events','Cogs.misc commands', 'Cogs.Music', 'Cogs.Activity']

if __name__ == '__main__':
    for extension in extensions:
        client.load_extension(extension)








client.run('NjU0MjQ4MzAxNDY5ODkyNjIx.Xq1Uuw.Gid-8C8f_HJiHMl14SR7ykDaNPI')


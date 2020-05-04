import asyncio
from asyncio import queues
import discord
import youtube_dl
import shutil
import os
from discord.ext import commands
from discord.utils import get

class DiscordDisco(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_contect=True)
    async def join(self, ctx):
        global voice
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        await ctx.channel.send(f'Joined {channel}')

    @commands.command(pass_contect=True)
    async def leave(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.disconnect()
            await ctx.channel.send(f'Left {channel}')


    @commands.command(aliases=['p', 'pla'])
    async def play(self, ctx, url: str):

        def check_queue():
            Queue_infile = os.path.isdir('./Queue')
            if Queue_infile is True:
                filedir = os.path.abspath(os.path.realpath('Queue'))
                length = len(os.listdir(filedir))
                still_q = length - 1
                try:
                    first_file = os.listdir(filedir)[0]
                except:
                    print('No more queued sond(s)\r\n')
                    queues.clear()
                    return
                main_location = os.path.dirname(os.path.realpath(__file__))
                song_path = os.path.abspath(os.path.realpath('Queue') + '\\' + first_file)
                if length != 0:
                    print('Song done, playing next queued\n')
                    print(f'Songs still in queue: {still_q}')
                    if song_there:
                        os.remove('song.mp3')
                    shutil.move(song_path, main_location)
                    for file in os.listdir('./'):
                        if file.endswith('.mp3'):
                            os.rename(file, 'song.mp3')

                    voice.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: check_queue())
                    voice.source = discord.PCMVolumeTransformer(voice.source)
                    voice.source.volume = 0.07

                else:
                    queues.clear()
                    return
            else:
                queues.clear()
                print('No Songs were queued befor ending of the last Song\n')

        song_there = os.path.isfile('song.mp3')
        try:
            if song_there:
                os.remove('song.mp3')
                queues.clear()
                print('Remove old song file')
        except PermissionError:
            print('Trying to delete Song file')
            await ctx.channel.send('ERROR: Music playing')
            return

        Queue_infile = os.path.isdir('./Queue')
        try:
            Queue_folder = './Queue'
            if Queue_infile is True:
                print('Remove old Queue Folder')
                shutil.rmtree(Queue_folder)
        except:
            print('No old Queue folder')

        await ctx.channel.send('Getting everything Ready now')

        voice = get(self.bot.voice_clients, guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'quit': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print('Downloading audio now\n')
            ydl.download([url])

        for file in os.listdir('./'):
            if file.endswith('.mp3'):
                name = file
                print(f'Renamed File: {file}\n')
                os.rename(file, 'song.mp3')

        voice.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: check_queue())
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.07

        nname = name.rsplit('-', 2)
        await ctx.channel.send(f'Playing: {name[0]}')
        print('playing\n')

    @commands.command(aliases=['pa', 'pau'])
    async def pause(self, ctx):

        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_playing():
            print('Music paused')
            voice.pause()
            await ctx.channel.send('Music paused')
        else:
            print('Music not playing - failed pause')
            await ctx.channel.send('Music not playing - failed pause')

    @commands.command(aliases=['r', 'res'])
    async def resume(self, ctx):

        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_pause():
            print('Music paused')
            voice.resume()
            await ctx.channel.send('Resumed Music')
        else:
            print('Music is not paused')
            await ctx.channel.send('Music is not paused')

    @commands.command(aliases=['s', 'ski'])
    async def skip(self, ctx):

        voice = get(self.bot.voice_clients, guild=ctx.guild)

        queues.clear()

        if voice and voice.is_playing():
            print('Music skipped')
            voice.stop()
            await ctx.channel.send('Music skipped')
        else:
            print('Music not playing - failed skipped')
            await ctx.channel.send('Music not playing - failed skipped')

    @commands.command(aliases=['q', 'que'])
    async def queue(self, ctx, url: str):
        queues = {}
        Queue_infile = os.path.isdir('./Queue')
        if Queue_infile is False:
            os.mkdir('Queue')

        filedir = os.path.abspath(os.path.realpath('Queue'))
        q_num = len(os.listdir(filedir))
        q_num += 1
        add_queue = True
        while add_queue:
            if q_num in queues:
                q_num += 1
            else:
                add_queue = False
                queues[q_num] = q_num

        queue_path = os.path.abspath(os.path.realpath('Queue') + f'\song{q_num}.%(ext)s')

        ydl_opts = {
            'format': 'bestaudio/best',
            'quit': True,
            'outtmpl': queue_path,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print('Downloading Audio nowß\n')
            ydl.download([url])

        await ctx.channel.send('Adding song ' + str(q_num) + ' to the queue')
        print('Song Added')


def setup(bot):
    bot.add_cog(DiscordDisco(bot))

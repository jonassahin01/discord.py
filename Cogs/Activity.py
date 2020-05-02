import discord
from discord.ext import commands

import json
import asyncio

class Activity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.loop.create_task(self.save_users()) #background task in cog

        with open('users.json', 'r') as f:
            self.users = json.load(f)

    async def save_users(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            with open('users.json', 'w') as f:
                json.dump(self.users, f, indent=4)

            await asyncio.sleep(5)

    async def lvl_up(self, author_id):
        cur_xp = self.users[author_id]['exp']
        cur_lvl = self.users[author_id]['level']

        if cur_xp >= round((4*(cur_lvl ** 3)) / 5):
            self.users[author_id]['level'] += 1
            return True
        else:
            return False

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        author_id = str(message.author.id)

        if not author_id in self.users:
            self.users[author_id] = {}
            self.users[author_id]['level'] = 1
            self.users[author_id]['exp'] = 0

        self.users[author_id]['exp'] += 1

        if await self.lvl_up(author_id):
            print(f"{message.author} has leveled up to level {self.users[author_id]['level']}")

    @commands.command()
    async def level(self, ctx, member: discord.Member = None):
        '''Displays informations about user level'''
        member = ctx.author if not member else member
        member_id = str(member.id)

        if not member_id in self.users:
            await ctx.send("There isn't any user")
        else:
            embed = discord.Embed(color=discord.Color.green(), timestamp=ctx.message.created_at)

            embed.set_author(name=f"Level - {member.name}", icon_url=self.bot.user.avatar_url)
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name="Level", value=self.users[member_id]['level'])
            embed.add_field(name="XP", value=f"{self.users[member_id]['exp']}/{round((4*(self.users[member_id]['level'] ** 3)) / 5)}")

            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Activity(bot))

import discord
import random
import json
import asyncio
import os
from discord.ext import commands
from discord.utils import get


class AdministratorCommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot



    @commands.command(aliases=['мягкийбан'])
    @commands.has_permissions(ban_members=True)
    async def softban(self, ctx, member : discord.Member, *, reason=None):
        if not member:
            return await ctx.send("Вы должны указать пользователя")

        try:
            await member.ban(reason=None)
            await member.unban()
            await ctx.send(f'{member.mention} Has been banned & unbanned')
        except discord.Forbidden:
            return await ctx.send("forbidden")

    @commands.command(aliases=['Чисто','чистый'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount : int): #(ctx, amount : int):
        await ctx.channel.purge(limit=amount)

    @commands.command(aliases=['удар'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'ногами{member.mention}')


    @commands.command(aliases=['запрет','бан'])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'запрещенный {member.mention}')

    @commands.command(aliases=['унбан'])
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return


    @commands.command(aliases=['немой'])
    @commands.has_permissions(ban_members=True)
    async def mute(self, ctx, member:discord.Member):
        guild = ctx.guild

        for role in guild.roles:
            if role.name == "Muted":
                await member.add_roles(role)
                await ctx.send("{} пользователь {} был немой" .format(member.mention,ctx.author.mention))
                return

                overwrite = discord.PermissionOverwrite(send_messages=False)
                newRole = await guild.create_role(name="Muted")

                for channel in guild.text_channels:
                    await channel.set_permissions(newRole,overwrite=overwrite)

                await member.add_roles(newRole)
                await ctx.send("{}  пользователь {} был немой" .format(member.mention,ctx.author.mention))

    @commands.command(aliases=['уннемой'])
    @commands.has_permissions(ban_members=True)
    async def unmute(self, ctx, member:discord.Member):
        guild = ctx.guild

        for role in guild.roles:
            if role.name == "Muted":
                await member.remove_roles(role)
                await ctx.send("{} пользователь был уннемой" .format(member.mention))
            return

def setup(bot):
    bot.add_cog(AdministratorCommands(bot))

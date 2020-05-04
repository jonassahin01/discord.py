import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def help(self,ctx):
        embed = discord.Embed(title="Discord Bot", description="Commands", color=0xeee657)
        embed.add_field(name="ping" , value="checks connection to server", )
        embed.add_field(name="8ball" , value="ask a question", )
        embed.add_field(name="choice" , value="choose between text", )
        embed.add_field(name="roll" , value="dices", )
        embed.add_field(name="randnum" , value="between 1 & 10 default", )
        embed.add_field(name="bigemoji" , value="large emoji", )
        embed.add_field(name="say" , value="bot will say it for you", )
        embed.add_field(name="user" , value="contains profile information", )
        embed.add_field(name="calculate" , value="+", )
        embed.add_field(name="subtract" , value="-", )
        embed.add_field(name="multiply" , value="*", )
        embed.add_field(name="division" , value="/", )
        embed.add_field(name="memo" , value="remind me later", )
        embed.add_field(name="remind" , value="remind me now", )
        embed.add_field(name="level" , value="tells you level", )
        embed.add_field(name="clear" , value="clears chat msg", )
        embed.add_field(name="kick" , value="kicks member", )
        embed.add_field(name="ban" , value="bans member", )
        embed.add_field(name="unban" , value="unbans member", )
        embed.add_field(name="mute" , value="mutes member", )
        embed.add_field(name="unmute" , value="unmutes member", )
        embed.add_field(name="join" , value="bot joins to voice", )
        embed.add_field(name="leave" , value="bot leaves voice", )
        embed.add_field(name="play" , value="plays a song", )
        embed.add_field(name="pause" , value="pauses song", )
        embed.add_field(name="resume" , value="resume song", )
        embed.add_field(name="skip" , value="skips song", )
        embed.add_field(name="queue" , value="queues a song", )

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))

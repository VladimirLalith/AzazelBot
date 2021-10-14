import discord
from discord.ext import commands



'''Module for moderator commands.'''


class Mod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def kick(self,ctx, userName: discord.User,reason=None):
        await userName.kick(reason=reason)
        await ctx.send(f'`{userName}` has been kicked by `{ctx.author}`.<a:peepsadsip:893715149934985216>')

    @commands.command()
    async def ban(self,ctx,userName:discord.User,reason=None):
        await userName.ban(reason=reason)
        await ctx.send(f'`{userName}` has been banned by `{ctx.author}`.<a:peepban:893715118548979762>')    

    @commands.command()
    async def unban(self,ctx,userName:discord.User,reason=None):
        await ctx.guild.unban(userName,reason=reason)
        await ctx.send(f'`{userName}` has been unbanned by `{ctx.author}`.<:peepyeaboi:893715233401602078>')

def setup(bot):
    bot.add_cog(Mod(bot))
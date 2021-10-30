import discord
from discord.ext import commands



'''Module for moderator commands.'''


class Mod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def kick(self,ctx, userName: discord.User,reason=None):
        '''Kicks a user.(Only can be done if you have perms.)'''
        await userName.kick(reason=reason)
        await ctx.send(f'`{userName}` has been kicked by `{ctx.author}`.<a:peepsadsip:893715149934985216>')

    @commands.command()
    async def ban(self,ctx,userName:discord.User,reason=None):
        '''Bans a user.(No perms, no banning.)'''
        await userName.ban(reason=reason)
        await ctx.send(f'`{userName}` has been banned by `{ctx.author}`.<a:peepban:893715118548979762>')    

    @commands.command()
    async def unban(self,ctx,userName:discord.User,reason=None):
        '''Unbans a user.(Why ban in the first place?)'''
        await ctx.guild.unban(userName,reason=reason)
        await ctx.send(f'`{userName}` has been unbanned by `{ctx.author}`.<:peepyeaboi:893715233401602078>')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self,ctx, member: discord.Member):
        '''Mutes a user.'''
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        guild = ctx.guild
        if role not in guild.roles:
            perms = discord.Permissions(send_messages=False, speak=False)
            await guild.create_role(name="Muted", permissions=perms)
            await member.add_roles(role)
            await ctx.send(f"`Successfully created Muted role and assigned it to` {member}.")
        else:
            await member.add_roles(role) 
            await ctx.send(f"`Successfully muted :`({member})")

    @commands.command()
    @commands.has_permissions(kick_members=True)        
    async def unmute(self,ctx,member:discord.Member):
        '''Unmutes a user'''
        role = discord.utils.get(ctx.guild.roles,name='Unmuted')
        guild = ctx.guild
        if role not in guild.roles:
            perms = discord.Permissions(send_messages=True,speak=True)
            await guild.create_role(name='Unmuted',permissions=perms)
            await member.add_roles(role)
            await ctx.send(f'`Successfully created Unmuted role and assigned it to` {member}.')
        else:
            await member.add_roles(role)
            await ctx.send(f'`Successfully umuted :`({member})')    


def setup(bot):
    bot.add_cog(Mod(bot))
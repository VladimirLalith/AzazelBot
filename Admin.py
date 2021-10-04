from logging import exception
from typing import Optional
import discord

from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.core import command

from discord.ext.commands.flags import F


intent = discord.Intents.default


class Admin(commands.Cog):
    def __init__(self, bot):
            self.bot = bot

    

    @commands.command()
    async def dmbot(self,ctx):
        """Dm the bot(just a fun command)."""
        embed = discord.Embed(
            title='DmBot',
            description='What up chump?:expressionless:',
            color= discord.Color.dark_gold()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def info(self,ctx, member = discord.Member):
        """Gives info of the bot."""
        embed = discord.Embed(
            title = 'BotInfo',
            description = 'Azazel is a bot made for doing fun/cool stuff, for now its just a newbie but gradually it will increase its potential.',
            
        )
        
        

        embed.set_footer(text='For more help pls run a.help <command>. Do the similar for categories a.help <category>')
        
        embed.set_thumbnail(url='https://images-ext-1.discordapp.net/external/fKAZoYv-XNws-mQQsPFxMldJp9OZ2QFb33FRmoQOaZY/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/880341079218589706/adbf57cf21a882d09b549ecb58d224a8.webp?width=300&height=300')
        embed.set_author(name='Azazel',icon_url='https://images-ext-1.discordapp.net/external/fKAZoYv-XNws-mQQsPFxMldJp9OZ2QFb33FRmoQOaZY/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/880341079218589706/adbf57cf21a882d09b549ecb58d224a8.webp?width=300&height=300')
        
        embed.add_field(name='BotOwner/BotDeveloper:computer:',value='`ᐯ ᒪ ᗩ ᗪ I#5472`:chicken:',inline=False)
        embed.add_field(name='BotPrefix',value='`a.`',inline=False)
        view = discord.ui.View()
        view.add_item(discord.ui.Button(label = 'Support Server', url = f'https://discord.gg/FEwkNHzt6g', emoji = f'<a:pandacool:893714777661136916>'))
        view.add_item(discord.ui.Button(label='Invite Link',url=f'https://discord.com/api/oauth2/authorize?client_id=880341079218589706&permissions=8&scope=bot',emoji=f'<:prayage:893715245292462080>'))
        
        
        await ctx.send(embed=embed,view=view)  
              
               





    @commands.command(aliases = ['ui'])
    async def userinfo(self,ctx,member:discord.Member):
        """Gives info of an user."""
        roles = [role for role in member.roles[1:]]
        embed = discord.Embed(
            title='UserInfo',
            color=member.color,timestamp=ctx.message.created_at)
        embed.set_author(name=f'User Info - {member}'),
        embed.set_thumbnail(url=member.avatar),
        embed.set_footer(text=f'Requested by - {ctx.author}',
        icon_url = ctx.author.avatar)

        embed.add_field(name='ID:',value=member.id,inline=False)
        embed.add_field(name='Name:',value=member.display_name,inline=False)
        embed.add_field(name='Created at:',value=member.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"),inline=False)
        embed.add_field(name='Joined at:',value=member.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"),inline=False)
        embed.add_field(name=f"Roles ({len(member.roles) - 1})", value='• '.join([role.mention for role in roles]), inline=False)
        embed.add_field(name=f"Highest Role", value = f"{member.top_role.mention}")
        embed.add_field(name='Bot?',value=member.bot,inline=False)

        await ctx.send(embed=embed)            



    @commands.command(aliases = ['servinfo','si'])
    async def serverinfo(self,ctx):
        '''Gives info of an server.'''
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)

    
        

        owner = str(ctx.guild.owner)
        id = int(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = int(ctx.guild.member_count)

        icon = str(ctx.guild.icon)
        
        embed = discord.Embed(
            title=name + " Server Information",
            description=description,
            color=discord.Color.dark_gold()
            )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=False)
        embed.add_field(name="Server ID", value=id, inline=False)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=False)

        await ctx.send(embed=embed)

    @commands.command(aliases=['src'])
    async def source(self,ctx):
        """Gives the source code of the bot."""
        embed=discord.Embed(
            title='Source',
            description='Code of the bot.(Dont copy the code anyways its garbage.)',
            color=discord.Color.dark_gold()
        )    
        view=discord.ui.View()
        view.add_item(discord.ui.Button(label='Source',url=f'https://github.com/VladimirLalith/AzazelBot',emoji=f'<:pepe_sweat:889902767030796289>'))

        await ctx.send(embed=embed,view=view)

def setup(bot): # a extension must have a setup function
	bot.add_cog(Admin(bot))         
from logging import exception
import os
from typing import Optional
import discord
import inspect
from discord import client
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
    async def dm(self,ctx,member:discord.Member,*,message):
        author=ctx.author
        await member.send(f"`Message from {author}`:\n`{message}` ")
        await ctx.send('`Message has been sent`<:WinCheck:898572324490604605>')            

    @commands.command()
    async def info(self,ctx, member = discord.Member):
        """Gives info of the bot."""
        embed = discord.Embed(
            title = 'BotInfo',
            description = 'Azazel is a bot made for simple Moderation tasks / Fun stuff / Emojis / Etc..., for now its just a newbie but gradually it will increase its potential.',
            
        )
        
        

        embed.set_footer(text='For more help pls run a|help <command>. Do the similar for categories, a|help <category>')
        
        embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/880341079218589706/a28882a4b22b7b4b03a0e860966d406d.png?size=1024')
        embed.set_author(name='Azazel',icon_url='https://cdn.discordapp.com/avatars/880341079218589706/a28882a4b22b7b4b03a0e860966d406d.png?size=1024')
        
        embed.add_field(name='BotOwner/BotDeveloper:computer:',value='`ᐯ ᒪ ᗩ ᗪ I#5472`:chicken:',inline=False)
        embed.add_field(name='BotPrefix',value='`a?`',inline=False)
        embed.add_field(name='BotLanguage',value=f'<:WinPython:898614277018124308>')
        embed.add_field(name="Analytics:",value=f"**Servers:** {len([g.id for g in self.bot.guilds])} servers\n**Users:** {len([g.id for g in self.bot.users])}", inline = True)
        embed.add_field(name="On Discord Since:",value=f"<t:{round(ctx.me.created_at.timestamp())}:D>",inline=True)        
        view = discord.ui.View()
        view.add_item(discord.ui.Button(label = 'Support Server', url = f'https://discord.gg/6vPmAh4xUM', emoji = f'<:ehe:894097825514790983>'))
        view.add_item(discord.ui.Button(label='Invite Link',url=f'https://discord.com/api/oauth2/authorize?client_id=880341079218589706&permissions=8&scope=bot',
            emoji=f'<:prayage:893715245292462080>'))
        view.add_item(discord.ui.Button(label='Source',url=f'https://github.com/VladimirLalith/AzazelBot',emoji=f'<:github:898810801605980220>'))
        
        await ctx.send(embed=embed,view=view)  
              
    @commands.command(aliases  = ['src'])
    async def source(self, ctx, *, command: str = None):
        """Displays my full source code or for a specific command.
        To display the source code of a subcommand you can separate it by
        periods, e.g. tag.create for a create subcommand of the tag command
        or by spaces.
        """
        view = discord.ui.View()
        source_url = 'https://github.com/VladimirLalith/AzazelBot'
        #Github link to the source code repo
        branch = 'main'
        #The branch which the current repo uses
        emoji = "<:github:889018277815279676>"
        #Make sure to replace the emoji with one that your bot is in, incase it isn't in Woodlands

        if command is None:
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.link, url = source_url, label = "Source", emoji = emoji))
            return await ctx.send("`Repository`", view = view)
        
        obj = self.bot.get_command(command.replace('.', ' '))

        if command == 'help':
            src = type(self.bot.help_command)
            module = src.__module__
            filename = inspect.getsourcefile(src)
        else:
            if obj is None:
                return await ctx.send(f'`Could not find command`: {command}')


            # since we found the command we're looking for, presumably anyway, let's
            # try to access the code itself
            src = obj.callback.__code__
            module = obj.callback.__module__
            filename = src.co_filename

        
        if not module.startswith('discord') or command == 'help':
            # not a built-in command
            location = os.path.relpath(filename).replace('\\', '/').split("Program Files")[-1]
        else:
            location = module.replace('.', '/') + '.py'
        final_url = f'{source_url}/blob/{branch}/{location}'.replace(" ","%20")
        view.add_item(discord.ui.Button(style=discord.ButtonStyle.link, url = final_url, label = "Source", emoji = emoji))
        await ctx.send(f"`Source for`: `{obj.qualified_name}`", view = view)               





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

    @commands.command(aliases=['av','dp','pfp'])
    async def avatar(self, ctx , member:discord.Member):
        """Gives the avatar/dp of a user."""
        avatar = member.avatar.with_static_format('png') if member.avatar else member.default_avatar.with_static_format('png')
        embed = discord.Embed(
            title='Avatar',
            color= member.color,
         
        )    
        embed.set_author(name=f'User Avatar - {member}'),
        embed.set_image(url=member.avatar),
        embed.set_footer(text=f'Requested by - {ctx.author}', icon_url= avatar)
        view = discord.ui.View()
        view.add_item(discord.ui.Button(label = 'Avatar Link', url = member.avatar.url))
        await ctx.send(embed=embed,view=view)          



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

        


def setup(bot): # a extension must have a setup function
	bot.add_cog(Admin(bot))         
import discord
from discord.ext import commands


class Support(commands.Cog):
    def __init__(self, bot):
            self.bot = bot

class Select(discord.ui.Select):
   
    def __init__(self):


        super().__init__(placeholder="Choose here.",  
        options=[
            discord.SelectOption(label="Main Page",emoji='<:WinArrow:898572481156247602>'),
            discord.SelectOption(label="Utility",emoji='<:WinArrow:898572481156247602>'),
            discord.SelectOption(label='Mod',emoji='<:WinArrow:898572481156247602>'),
            discord.SelectOption(label='Game',emoji='<:WinArrow:898572481156247602>'),
            discord.SelectOption(label='Fun',emoji='<:WinArrow:898572481156247602>'),
            discord.SelectOption(label='Admin',emoji='<:WinArrow:898572481156247602>'),
            discord.SelectOption(label='Emojis',emoji='<:WinArrow:898572481156247602>')
                ]
                        )


    
    async def callback(self, interaction: discord.Interaction):
        emb = discord.Embed(
            title= 'AzazelBot Commands',
            description='For more information of a command please run a?help [command] & for categories please run a?help [category]',
            color=discord.Color.dark_gray()
        )
        emb.set_author(name='AzazelBot',icon_url='https://cdn.discordapp.com/avatars/880341079218589706/a28882a4b22b7b4b03a0e860966d406d.png?size=1024')
        emb.set_thumbnail(url='https://cdn.discordapp.com/avatars/880341079218589706/a28882a4b22b7b4b03a0e860966d406d.png?size=1024')
        emb.add_field(name='<:CheckList:879961726865522688>**Admin**',value='Administrator Commands')
        emb.add_field(name='<:Moderator:877796954011222047>**Mod**',value='Moderation Commands')
        emb.add_field(name='**Fun**',value='Make Fun!')
        emb.add_field(name='<:Utils:877796922876919808>**Utility**',value='Utility Commands')
        emb.add_field(name='<:games:873863717585059970>**Game**',value='Just a few games')
        emb.add_field(name='<a:pandawwshake:894526903829012521>**Emojis**',value='Best commands this bot has')
        emb.set_footer(text='Thank you for using AzazelBot. Hope you enjoyed it!')       
        emb1 = discord.Embed(
            title='Utility Commands',
            description='These commands are for Utility purpose',
            color=discord.Color.dark_gray()
        )
        emb1.add_field(name='test',value='Returns test',inline=False)
        emb1.add_field(name='ping',value='Returns ping',inline=False)
        emb1.add_field(name='choose',value='Chooses between multiple choices',inline=False)
        emb1.add_field(name='repeat',value='Repeats a word',inline=False)
        emb1.add_field(name='nickname',value='Sets a nickname for a user',inline=False)
        emb1.add_field(name='clear',value='Clears messages',inline=False)
        emb2 = discord.Embed(
            title='Mod Commands',
            description='These commands are used to do moderations in the server',
            color=discord.Color.dark_gray()
        )
        emb2.add_field(name='kick',value='To kick a user',inline=False)
        emb2.add_field(name='ban',value='To ban a user',inline=False)
        emb2.add_field(name='unban',value='To unban a user',inline=False)
        emb2.add_field(name="mute",value='To mute a user',inline=False)
        emb2.add_field(name='unmute',value='To unmute a user',inline=False)
        emb3 = discord.Embed(
            title='Game',
            description='These commands are for playing games',
            color=discord.Color.dark_gray()
        )
        emb3.add_field(name='guessthenumber',value='Guess the number and win!',inline=False)
        emb3.add_field(name='rockpaperscissors',value='Play rock,paper,scissors!',inline=False)
        emb4 = discord.Embed(
            title='Admin Commands',
            description='These are administrator commands',
            color=discord.Color.dark_gray()
        )
        emb4.add_field(name='dmbot',value='Just a fun command',inline=False)
        emb4.add_field(name='dm',value='Send a message to a user',inline=False)
        emb4.add_field(name='info',value='Gives information about the bot',inline=False)
        emb4.add_field(name='source',value='Displays code for a particular command',inline=False)
        emb4.add_field(name='userinfo',value='Gives info of an user',inline=False)
        emb4.add_field(name='serverinfo',value='Gives info of a server',inline=False)
        emb4.add_field(name='avatar',value='Returns the avatar of an user',inline=False)
        emb5 = discord.Embed(
            title='Expression Commands',
            description='These commands are used for expressions',
            color=discord.Color.dark_gray()
        )
        emb5.add_field(name='botcool',value='Is the bot cool?',inline=False)
        emb5.add_field(name='roll',value='Roll the dice!',inline=False)
        emb5.add_field(name='coinflip',value='Flip the coin!',inline=False)
        emb6 = discord.Embed(
            title='Emojis',
            description="These commands give emojis",
            color=discord.Color.dark_gray()
        )
        emb6.add_field(name='emojilaugh',value='Gives a laughing emoji')
        if self.values[0] == 'Utility':
            await interaction.message.edit(embed=emb1)
        elif self.values[0] == 'Mod':
            await interaction.message.edit(embed=emb2) 
        elif self.values[0] == "Main Page":
            await interaction.message.edit(embed=emb)  
        elif self.values[0] == 'Game':
            await interaction.message.edit(embed=emb3)
        elif self.values[0] == 'Admin':
            await interaction.message.edit(embed=emb4) 
        elif self.values[0] == 'Fun':
            await interaction.message.edit(embed=emb5)       
            


    @commands.command(aliases=['helper','aid'])
    async def support(ctx):

        emb = discord.Embed(
            title= 'AzazelBot Commands',
            description='For more information of a command please run a?help [command] & for categories please run a?help [category]',
            color=discord.Color.dark_gray()
        )
        emb.set_author(name='AzazelBot',icon_url='https://cdn.discordapp.com/avatars/880341079218589706/a28882a4b22b7b4b03a0e860966d406d.png?size=1024')
        emb.set_thumbnail(url='https://cdn.discordapp.com/avatars/880341079218589706/a28882a4b22b7b4b03a0e860966d406d.png?size=1024')
        emb.add_field(name='<:CheckList:879961726865522688>**Admin**',value='Administrator Commands')
        emb.add_field(name='<:Moderator:877796954011222047>**Mod**',value='Moderation Commands')
        emb.add_field(name='**Fun**',value='Make Fun!')
        emb.add_field(name='<:Utils:877796922876919808>**Utility**',value='Utility Commands')
        emb.add_field(name='<:games:873863717585059970>**Game**',value='Just a few games')
        emb.add_field(name='<a:pandawwshake:894526903829012521>**Emojis**',value='Best commands this bot has')
        emb.set_footer(text='Thank you for using AzazelBot. Hope you enjoyed it!')   
        view = discord.ui.View()
        view.add_item(Select())

        await ctx.send('<:HelpMenu:873859534651809832>`Help Page`',embed=emb,view=view) 

def setup(bot):
    bot.add_cog(Support(bot))        
import asyncio
import time
import discord
from discord import message
from discord import player
from discord.colour import Color
from discord.components import  SelectOption
from discord.embeds import Embed
from discord.ext import commands
from discord.types.components import _SelectMenuOptional
from discord import Intents
import json




intent = Intents().all()


TOKEN = 'ODgwMzQxMDc5MjE4NTg5NzA2.YSc3hQ.W45LAe9ha6ss82EyBfrqgjrtUDY'

  


client = commands.Bot(command_prefix=commands.when_mentioned_or('a|'))

extensions=['Admin','Mod','Mathematics','Fun','Utility','Game','ErrorHandler','Expressions','Emojis']

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded.[{}]'.format(extension,error))



channelids = set()

channelids = [
            {"809770965143257118",
            "890196700109631568",
            "890451733044670467"  
            }

]



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='a|help; NoobBot'),status=discord.Status.idle)
    print('Bot is ready.')

        
          

@client.event
async def on_member_join(member):
    await client.get_channel(channelids).send(f'{member} has joined the server.Welcome!<:335_eth_smile:826038399143510036>')
    

@client.event
async def on_member_remove(member):
    await client.get_channel(channelids).send(f'{member} has left the server.Goodbye!<:pepe_exit:810165976913018910>')



@client.event
async def on_message(message):
    mention = f'<@!{753081438693228625}>'
    mention1 = f'<@!{880341079218589706}>'
    if mention in message.content:
        await message.add_reaction(f'<a:peaceout:865247515422883880>')
    if mention1 in message.content:
        await message.channel.send(' `a.help` run करो.<a:triggered:893715398028050472>')  
    else:
        await client.process_commands(message)
        
  



@client.command()
async def dm(ctx,member:discord.Member,*,message):
  author=ctx.author
  await member.send(f"message from {author}:\n{message} ")
  await ctx.send('Message has been sent')     


@client.command()
async def pages(ctx):
    """Shows pages which can be turned front/back."""
    contents = ["This is page 1!", "This is page 2!", "This is page 3!", "This is page 4!"]
    pages = 4
    cur_page = 1
    message = await ctx.send(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
    # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            # example

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            await message.delete()
            break
            # ending the loop if user doesn't react after x seconds
    

class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=discord.Color.dark_gold(), description='')
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)

        
client.help_command = MyHelpCommand()



@client.command(aliases=['sd'])
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send('I am gonna shutdown.<a:pandasnap:893715060822786048>')
    await client.close()


word='discord'
user_guesses= list()

@client.command(aliases=['hm'])
async def hangman(ctx,guess:str):
            progress_word=''
            guess= guess.lower()

            #if len(user_guesses) == 4:
                #await ctx.send(f'```You couldnt find the correct answer.```<a:pandasnap:893715060822786048> `ANSWER`: {word}.')
            
                 
            for c in word.lower():
            
                if guess==c or c in user_guesses:
                    progress_word+=c
                else:
                    progress_word+='\_.'
            user_guesses.append(guess)
            
            

            if guess==word:
                    await ctx.send('Damn!, you won.<a:pandaclap:893714731330838549>')    
                    
            else:
                    await ctx.send('`Progress`:  %s'% progress_word)

          

class MyHelpCommand(commands.MinimalHelpCommand):

    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page)
            await destination.send(embed=emby)    

class MyCog(commands.Cog):
    def __init__(self, bot):
        self._original_help_command = bot.help_command
        bot.help_command = MyHelpCommand()
        bot.help_command.cog = self

    def cog_unload(self):
        self.bot.help_command = self._original_help_command

client.help_command= MyHelpCommand()        

import discord
from discord.ext import commands


class Dropdown(discord.ui.Select):
    def __init__(self):

        # Set the options that will be presented inside the dropdown
        options = [
            discord.SelectOption(label='Red', description='Your favourite colour is red', emoji='🟥'),
            discord.SelectOption(label='Green', description='Your favourite colour is green', emoji='🟩'),
            discord.SelectOption(label='Blue', description='Your favourite colour is blue', emoji='🟦')
        ]

        super().__init__(placeholder='Choose your favourite colour...', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'***Your favourite colour is ***:  `{self.values[0]}`', ephemeral=True)


class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()  
        

        # Adds the dropdown to our view object.
        self.add_item(Dropdown())

 
        

@client.command()
async def color(ctx):
    """Sends a message with our dropdown containing colours"""

    # Create the view containing our dropdown
    view = DropdownView()

    # Sending a message containing our view
    await ctx.send('Pick your favourite colour:', view=view)

       


client.run(TOKEN)
    
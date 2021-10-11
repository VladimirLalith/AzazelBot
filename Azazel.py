import asyncio
import discord
from discord import message
from discord.colour import Color
from discord.components import  SelectOption
from discord.ext import commands
from discord.types.components import _SelectMenuOptional
from discord import Intents
import json




intent = Intents().all()


TOKEN = 'ODgwMzQxMDc5MjE4NTg5NzA2.YSc3hQ.W45LAe9ha6ss82EyBfrqgjrtUDY'

  


client = commands.Bot(command_prefix='a|')

extensions=['Admin','Mathematics','Fun','Utility','Game','ErrorHandler','Expressions','Emojis']

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
        await message.add_reaction(f'<a:peepwalk:893715193744470027>')
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

class MySelect(discord.ui.Select):
    def __init__(self):

        
        options = [
            discord.SelectOption(
                emoji='\N{CHEESE WEDGE}',
                label='Cheese',
                description='A delicious block of cheese',
            ),
            discord.SelectOption(
                emoji='\N{LEAFY GREEN}',
                label='Lettuce',
                description='The freshest lettuce in the market',
            ),
            discord.SelectOption(
                emoji='\N{CUCUMBER}',
                label='Cucumber',
                description='A rather scrumptious cucumber',
            ),
            discord.SelectOption(
                emoji='\N{ONION}',
                label='Onion',
                description='An eye watering onion',
            ),
            discord.SelectOption(
                emoji='\N{GARLIC}',
                label='Garlic',
                description='Delicious',
            ),
            discord.SelectOption(
                emoji='\N{CARROT}',
                label='Carrot',
                description='The cutest carrots',
            ),
            discord.SelectOption(
                emoji='\N{TOMATO}',
                label='Tomato',
                description='The perfect mix of acidity and sweetness',
            ),
        ]
        super().__init__(placeholder='Select a meal', max_values=4, min_values=2, options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f'You have selected {", ".join(self.values)}.', ephemeral=True
        )

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

          

    
            
            

             


client.run(TOKEN)
    
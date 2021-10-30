import asyncio
import time
import discord
from discord import message
from discord import player
from discord import channel
from discord import user
from discord import embeds
from discord import mentions
from discord import guild
from discord import client
from discord.colour import Color
from discord.components import  C, SelectOption
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands import context
from discord.ext.commands.flags import F
from discord.types.components import _SelectMenuOptional
from discord import Intents
import json
import os
import random

from discord.ui import view

os.chdir('C:\\Users\\Dell\\Microsoft VS Code')


intent = Intents().all()


TOKEN = 'ODgwMzQxMDc5MjE4NTg5NzA2.YSc3hQ.pWosyQxL9AiRncbJw_Ol-bSuCuI'

  


client = commands.Bot(command_prefix=commands.when_mentioned_or("a?"),help_command=None)

extensions=['Admin','Mod','Mathematics','Fun','Utility','Game','ErrorHandler','Emojis','Owner','Support']

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded.[{}]'.format(extension,error))








@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='a?support/@A𝚣𝚊𝚣𝚎𝚕𝙱𝚘𝚝 support;NoobBot'),status=discord.Status.do_not_disturb)
    print('Bot is ready.')

        
          





@client.event
async def on_message(message):
    mention = '<@!753081438693228625>'
    for member in message.mentions:
    #look if the member ID is equal to your ID (343113425158668289)
        if 753081438693228625 == member.id:
            await message.add_reaction(f'<a:peaceout:865247515422883880>')
    if  message.content in ['<@!880341079218589706>','<@880341079218589706>']:
        await message.channel.send(' `a.help` run करो.<a:triggered:893715398028050472>')  
    await client.process_commands(message) 


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
        ctx = self.get_destination()
        e = discord.Embed(color=discord.Color.dark_gray(), description='')
        for page in self.paginator.pages:
            e.description += page
        await ctx.send(embed=e)
        

    async def send_error_message(self, error):
        embed = discord.Embed(title="Error", description=error,color=discord.Color.dark_gray())
        channel = self.get_destination()
        await channel.send(embed=embed)   





         
client.help_command = MyHelpCommand()










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
        emb.add_field(name='<a:WinBabyPat:898589341171978280>**Fun**',value='Make Fun!')
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
        emb6.add_field(name='emojilaugh',value='Gives a laughing emoji',inline=False)
        emb6.add_field(name='emojithink',value='Gives a thinking emoji',inline=False)
        emb6.add_field(name='emojioops',value='Gives a oops emoji',inline=False)
        emb6.add_field(name='emojisadcry',value='Gives a sad/crying emoji',inline=False)
        emb6.add_field(name='emojiok',value='Gives an okay emoji',inline=False)
        emb6.add_field(name='emojiexit',value='Gives an exiting emoji',inline=False)
        emb6.add_field(name='emojino',value='Gives a no emoji',inline=False)
        emb6.add_field(name='emojipain',value='Gives a pain emoji',inline=False)
        emb6.add_field(name='emojihmmno',value='Gives a hmmno emoji',inline=False)
        emb6.add_field(name='emojipray',value='Gives a praying emoji',inline=False)
        emb6.add_field(name='emojiworry',value='Gives a worrying emoji',inline=False)
        emb6.add_field(name='emojilesgo',value='Gives a lesgo emoji',inline=False)
        emb6.add_field(name='emojibruh',value='Gives a bruh emoji',inline=False)
        emb6.add_field(name='emojispace',value='Gives a space emoji',inline=False)
        emb6.add_field(name='emojify',value='Emojifies letters and numbers(Limited text)',inline=False)
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
        elif self.values[0] == 'Emojis':
            await interaction.message.edit(embed=emb6)         
            


@client.command(aliases=['helper','aid'])
async def support(ctx):

    emb = discord.Embed(
        title= 'AzazelBot Commands',
        description='For more information of a command please run `a?help [command]` & for categories please run `a?help [category]`',
        color=discord.Color.dark_gray()
    )
    emb.set_author(name='AzazelBot',icon_url='https://cdn.discordapp.com/avatars/880341079218589706/a28882a4b22b7b4b03a0e860966d406d.png?size=1024')
    emb.set_thumbnail(url='https://cdn.discordapp.com/avatars/880341079218589706/a28882a4b22b7b4b03a0e860966d406d.png?size=1024')
    emb.add_field(name='<:CheckList:879961726865522688>**Admin**',value='Administrator Commands')
    emb.add_field(name='<:Moderator:877796954011222047>**Mod**',value='Moderation Commands')
    emb.add_field(name='<a:WinBabyPat:898589341171978280>**Fun**',value='Make Fun!')
    emb.add_field(name='<:Utils:877796922876919808>**Utility**',value='Utility Commands')
    emb.add_field(name='<:games:873863717585059970>**Game**',value='Just a few games')
    emb.add_field(name='<a:pandawwshake:894526903829012521>**Emojis**',value='Best commands this bot has')
    emb.set_footer(text='Thank you for using AzazelBot. Hope you enjoyed it!')   
    view = discord.ui.View()
    view.add_item(Select())

    await ctx.send('<:HelpMenu:873859534651809832>`Help Page`',embed=emb,view=view)  




@client.command(aliases=['bal'])
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title=f'{ctx.author} Balance',color = discord.Color.red())
    em.add_field(name="Wallet Balance", value=wallet_amt)
    em.add_field(name='Bank Balance',value=bank_amt)
    await ctx.send(embed= em)

@client.command()
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(1001)

    await ctx.send(f'{ctx.author} Got {earnings}🪙!!')

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json",'w') as f:
        json.dump(users,f)


@client.command(aliases=['wd'])
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[1]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,'bank')
    await ctx.send(f'{ctx.author}, You withdrew {amount}🪙')


@client.command(aliases=['dep'])
async def deposit(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,'bank')
    await ctx.send(f'{ctx.author}, You deposited {amount} 🪙')


@client.command(aliases=['share','give'])
async def send(ctx,member : discord.Member,amount = None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)
    if amount == 'all':
        amount = bal[0]

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,-1*amount,'bank')
    await update_bank(member,amount,'bank')
    await ctx.send(f'{ctx.author} gave {member} {amount}🪙')


@client.command(aliases=['rb'])
async def rob(ctx,member : discord.Member):
    await open_account(ctx.author)
    await open_account(member)
    bal = await update_bank(member)


    if bal[0]<100:
        await ctx.send('`It is useless to rob him :(`')
        return

    earning = random.randrange(0,bal[0])

    await update_bank(ctx.author,earning)
    await update_bank(member,-1*earning)
    await ctx.send(f'{ctx.author} robbed: {member} and got {earning} 🪙')


@client.command()
async def slots(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("`Please enter the amount`")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('`You do not have sufficient balance`')
        return
    if amount < 0:
        await ctx.send('`Amount must be positive!`')
        return
    final = []
    for i in range(3):
        a = random.choice(['X','O','Q'])

        final.append(a)

    await ctx.send(str(final))

    if final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
        await update_bank(ctx.author,2*amount)
        await ctx.send(f'`You won` :) {ctx.author}')
    else:
        await update_bank(ctx.author,-1*amount)
        await ctx.send(f'`You lose` :( {ctx.author}')







@client.command(aliases = ["lb"])
async def leaderboard(ctx,x=10):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = str(user.id)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)    

    em = discord.Embed(title = f"Top {x} Richest People in AzazelEconomy:" , description = "This is decided on the basis of raw money in the bank and wallet.",color = discord.Color.dark_gray())
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        user = client.get_user(id_)
        name = user
        em.add_field(name = f"{index}. {name}" , value = f"{amt} 🪙",  inline = False)
        em.set_thumbnail(url=ctx.guild.icon)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)


async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open('mainbank.json','w') as f:
        json.dump(users,f)

    return True


async def get_bank_data():
    with open('mainbank.json','r') as f:
        users = json.load(f)

    return users


async def update_bank(user,change=0,mode = 'wallet'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open('mainbank.json','w') as f:
        json.dump(users,f)
    bal = users[str(user.id)]['wallet'],users[str(user.id)]['bank']
    return bal











client.run(TOKEN)
    
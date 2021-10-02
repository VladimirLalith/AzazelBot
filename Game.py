from inspect import EndOfBlock
import discord
import random
import asyncio
from discord import message
from datetime import time
from discord import client
from discord.ext import commands
from discord import Intents
from discord.ext.commands import bot

intent = Intents().all()

class Game(commands.Cog):
    def __init__(self, bot):
            self.bot = bot    
    
    @commands.command(aliases=['gn'])
    async def guessno(self, ctx):
        number = random.randint(0, 50)
        for i in range(0,5):
            await ctx.send('Guess the no. between 0-50')
            response = await self.bot.wait_for('message')
            guess = int(response.content)
            if guess > number:
                await ctx.send('Your no. was bigger than the actual one, `Pls try Again`')
            elif guess < number:
                await ctx.send('Your no. was smaller than the actual one, `Pls try Again`')
            elif guess == number:
                await ctx.send('Correct, u have successfully found the no. `YOU WON`:trophy:')
                return
        await ctx.send('`GAME OVER.` Hope u enjoyed the game.')

    
    @commands.command()
    async def rps(self,ctx):
        rpsGame = ['rock', 'paper', 'scissors']
        await ctx.send(f"`Rock`, `paper`, or `scissors`? Choose wisely...")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame

        user_choice = (await self.bot.wait_for('message', check=check)).content

        comp_choice = random.choice(rpsGame)
        if user_choice == 'rock':
            if comp_choice == 'rock':
                await ctx.send(f'Well, that was weird. We tied.\nYour choice: `{user_choice}`\nMy choice: `{comp_choice}`')
            elif comp_choice == 'paper':
                await ctx.send(f'Nice try, but I won that time!!\nYour choice: `{user_choice}`\nMy choice: `{comp_choice}`')
            elif comp_choice == 'scissors':
                await ctx.send(f"Aw, you beat me. It won't happen again!\nYour choice: `{user_choice}`\nMy choice: `{comp_choice}`")

        elif user_choice == 'paper':
            if comp_choice == 'rock':
                await ctx.send(f'The pen beats the sword? More like the paper beats the rock!!\nYour choice: `{user_choice}`\nMy choice: `{comp_choice}`')
            elif comp_choice == 'paper':
                await ctx.send(f'Oh, wacky. We just tied. I call a rematch!!\nYour choice: `{user_choice}`\nMy choice: `{comp_choice}`')
            elif comp_choice == 'scissors':
                await ctx.send(f"Aw man, better luck nxt time now im the winner!!:sunglasses:.\nYour choice: `{user_choice}`\nMy choice: `{comp_choice}`")

        elif user_choice == 'scissors':
            if comp_choice == 'rock':
                await ctx.send(f'HAHA!! I JUST CRUSHED YOU!! I rock!!\nYour choice: `{user_choice}`\nMy choice: `{comp_choice}`')
            elif comp_choice == 'paper':
                await ctx.send(f'Bruh. >: |\nYour choice: `{user_choice}`\nMy choice: `{comp_choice}`')
            elif comp_choice == 'scissors':
                await ctx.send(f"Oh well, we tied.\nYour choice: `{user_choice}`\nMy choice: `{comp_choice}`")




def setup(bot):
    bot.add_cog(Game(bot))
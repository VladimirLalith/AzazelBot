from discord import client
from discord.ext import commands
import discord
from discord import Intents

intent = Intents().all()

class Mathematics(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

        

    @commands.command()
    async def add(self,ctx, numOne: int, numTwo: int):
        """Adds two numbers"""
        await ctx.send(numOne + numTwo)

    @commands.command()
    async def sub(self,ctx, numOne: int, numTwo: int):
        """Subtracts two numbers"""
        await ctx.send(numOne - numTwo)

    @commands.command()
    async def mul(self,ctx, numOne: int, numTwo: int):
        """Multiplies two numbers"""
        await ctx.send(numOne * numTwo)

    @commands.command()
    async def div(self,ctx, numOne: int, numTwo: int):
        """Divides two numbers"""
        await ctx.send(numOne / numTwo)

    @commands.command()
    async def pow(self,ctx, numOne: int, numTwo: int):
        """Returns exponent a number"""
        await ctx.send(numOne ** numTwo)

def setup(bot): # a extension must have a setup function
	bot.add_cog(Mathematics(bot))

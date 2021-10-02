from discord.ext import commands
import discord
import random
from discord import Intents


intent = Intents().all()


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases =['botc'])
    async def botcool(self,ctx):
           
                """Is the bot cool?"""
                embed = discord.Embed(
                        title='BotCool?',
                        description='Ofcourse bruh, its awesome too.:spy:'

                )
                embed.set_thumbnail(url=f'https://www.redwolf.in/image/cache/catalog/stickers/thug-life-glasses-sticker-india-700x700.jpg')
                await ctx.send(embed=embed)        

    
    @commands.command()
    async def roll(self,ctx, dice: str):
        
            """Rolls a dice:game_die: in NdN format.Ex: a.roll 1d6"""
            try:
                rolls, limit = map(int, dice.split('d'))
            except Exception:
                await ctx.send('Format has to be in NdN!')
                return

            result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
            await ctx.send(result)
            
    @commands.command(aliases=['cf'])

    async def coinflip(self,ctx):
        """Flips the coin and gives result."""
        action= random.randint(0, 1)
        if(action == 0):
            flip= "Tails"
        elif(action == 1):
            flip= "Heads"

        
        embed= discord.Embed(title=f"{ctx.author} has flipped the coin!", description=f"`{flip}` it is!")
        await ctx.send(embed=embed)

    

def setup(bot):
    bot.add_cog(Fun(bot))
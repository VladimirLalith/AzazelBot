import discord
from discord.ext import commands


class Expressions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hug(self, ctx):
        embed = discord.Embed(
            title = 'Hug',
            description = 'You hugged Azazel',
            color = discord.Color.dark_gold()
        
        )
        embed.set_footer(text='Note from Azazel: Thx!!')
        await ctx.send(embed=embed)
   

    @commands.command()
    async def die(self, ctx):
        embed = discord.Embed(
            title = 'Die',
            description = 'You have successfully died:skull:. May God bless u for ur efforts.',
            color = discord.Color.dark_gold()
        
        )
        embed.set_footer(text='Meawhile God: Seriously??')
        await ctx.send(embed=embed)
   
    @commands.command()
    async def kill(self, ctx, member: discord.Member):

        
        embed = discord.Embed(
            title = 'Kill',
            description = f'You have successfully killed:dagger: {member.mention}. May {member.mention} Rest In Peace:coffin:',
            color = discord.Color.dark_gold()
        
        )
        
        embed.set_thumbnail(url=f'https://st.depositphotos.com/3263255/4351/i/600/depositphotos_43517485-stock-photo-gravestone.jpg')
        embed.set_footer(text=f'Note from {member} : Wtf bruh, why me?')
        await ctx.send(embed=embed)


        
        
    @commands.command()
    async def bruh(self,ctx):
        async with ctx.typing():

            embed = discord.Embed(
            title = 'Bruh',
            description='Horrible Life',
            color = discord.Color.dark_gold()
        
        )
        embed.set_thumbnail(url=f'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJw5PSqkK_19xW7oQ8vK_eRcBOkQ4lYauJpw&usqp=CAU')
        await ctx.send(embed=embed)       


    

    @commands.command()
    async def wth(self,ctx):
        async with ctx.typing():
            embed = discord.Embed(
                        title = 'Wth',
                        description='Life is Messed to the Core',
                        color = discord.Color.dark_gold()
                    
                    )
            embed.set_thumbnail(url=f'https://static1.makeuseofimages.com/wordpress/wp-content/uploads/2019/11/01-Confused-Nick-Young-Meme.png?q=50&fit=crop&w=670&dpr=1.5')
            await ctx.send(embed=embed)                    


def setup(bot):
    bot.add_cog(Expressions(bot))
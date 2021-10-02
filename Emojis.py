from discord.ext import commands



class Emojis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(aliases=['el'])
    async def emojilaugh(self,ctx):
        """Gives a laughing emoji."""
        await ctx.send(f'<:dogKek:811904709165318164>') 

    @commands.command(aliases=['et'])
    async def emojithink(self,ctx):
        """Gives a thinking emoji."""
        await ctx.send(f'<:Hmmm:810165982060478494>')    

    @commands.command(aliases=['eo'])
    async def emojioops(self,ctx):
        """Gives an oops emoji."""
        await ctx.send(f'<:oop:810165984086327366>')    

    @commands.command(aliases=['es','ec'])
    async def emojisadcry(self,ctx):
        """Gives a sad/crying emoji."""
        await ctx.send(f'<:catcrii:881867368358363146>')

    @commands.command(aliases=['eok'])    
    async def emojiok(self,ctx):
        """Gives an okay emoji."""
        await ctx.send(f'<:FrogOk:855867885788069908>')

    @commands.command(aliases=['ex'])
    async def emojiexit(self,ctx):
        """Gives an exiting emoji."""
        await ctx.send(f"<:pepe_exit:810165976913018910>")

    @commands.command(aliases=['esw'])
    async def emojisweat(self,ctx):
        """Gives a sweating emoji."""
        await ctx.send(f'<:pepe_sweat:889902767030796289>')  

    @commands.command(aliases=['eno'])
    async def emojino(self,ctx):
        """Gives a no emoji."""
        await ctx.send(f'<:pepe_no:889902703998795806>')     

    @commands.command(aliases=['ep'])
    async def emojipain(self,ctx):
        """Gives a pain emoji."""
        await ctx.send(f'<:linuspain:885124579729735721>')  

    @commands.command(aliases=['ehn'])
    async def emojihmmno(self,ctx):
        """Gives a hmmnope."""
        await ctx.send(f'<:hmmnope:891160212445229086>')    

    @commands.command(aliases=['epr'])
    async def emojipray(self,ctx):
        """Gives praying emoji."""
        await ctx.send(f'<:prayage:892415231203110992>')    

    @commands.command(aliases=['eg'])
    async def emojigun(self,ctx):
        """Gives gun emoji."""
        await ctx.send(f'<:pepe_gun:892426023470235678>')       

    @commands.command(aliases=['em'])
    async def emojify(self,ctx,*,text):
        """Emojifies letters nd numbers(Limit is there)."""
        emojis =  []
        for s in text.lower():
            if s.isdecimal():
                num2emo = {'0':'zero', '1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
                emojis.append(f':{num2emo.get(s)}:')
            elif s.isalpha():
                emojis.append(f':regional_indicator_{s}:')
                
            else:
                emojis.append(s)
        await ctx.send(''.join(emojis))                

def setup(bot):
    bot.add_cog(Emojis(bot))          


from logging import error
from discord import message
from discord.ext import commands
from discord.ext.commands.errors import MissingPermissions



class Emojis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(aliases=['el'])
    async def emojilaugh(self,ctx):
        """Gives a laughing emoji."""
        await ctx.send(f'<:dogKek:811904709165318164>') 
        try:  
            msg = ctx.message
            await msg.delete()
        except:
            pass  


    @commands.command(aliases=['et'])
    async def emojithink(self,ctx):
        """Gives a thinking emoji."""
        await ctx.send(f'<a:froghmm:893714493740294224>') 
        try:  
            msg = ctx.message
            await msg.delete()
        except:
            pass   
     

    @commands.command(aliases=['eo'])
    async def emojioops(self,ctx):
        """Gives an oops emoji."""
        await ctx.send(f'<:oop:810165984086327366>') 
        try:  
            msg = ctx.message
            await msg.delete()
        except:
            pass     


    @commands.command(aliases=['es','ec'])
    async def emojisadcry(self,ctx):
        """Gives a sad/crying emoji."""
        await ctx.send(f'<a:peepsadsip:893715149934985216>')
        try:  
            msg = ctx.message
            await msg.delete()
        except:
            pass  


    @commands.command(aliases=['eok'])    
    async def emojiok(self,ctx):
        """Gives an okay emoji."""
        await ctx.send(f'<:FrogOk:855867885788069908>')
        try:  
            msg = ctx.message
            await msg.delete()
        except:
            pass  


    @commands.command(aliases=['ex'])
    async def emojiexit(self,ctx):
        """Gives an exiting emoji."""
        await ctx.send(f"<a:walkaway:810185069519700028>")
        try:  
            msg = ctx.message
            await msg.delete()
        except:
            pass  
 

    @commands.command(aliases=['esw'])
    async def emojisweat(self,ctx):
        """Gives a sweating emoji."""
        await ctx.send(f'<:pepe_sweat:889902767030796289>')  
        try:  
            msg = ctx.message
            await msg.delete()
        except:
            pass  


    @commands.command(aliases=['eno'])
    async def emojino(self,ctx):
        """Gives a no emoji."""
        await ctx.send(f'<:pepe_no:889902703998795806>')
        try:  
            msg = ctx.message
            await msg.delete()
        except:
            pass     
 

    @commands.command(aliases=['ep'])
    async def emojipain(self,ctx):
        """Gives a pain emoji."""
        await ctx.send(f'<:lttpain:893714668663734284>')  
        try:  
            msg = ctx.message
            await msg.delete()
        except:
            pass  


    @commands.command(aliases=['ehn'])
    async def emojihmmno(self,ctx):
        """Gives a hmmnope."""
        await ctx.send(f'<:peepxtremhmm:893715203882123275>')   
        try:  
            msg = ctx.message
            await msg.delete()
        except:
            pass  


    @commands.command(aliases=['epr'])
    async def emojipray(self,ctx):
        """Gives praying emoji."""
        await ctx.send(f'<:prayage:893715245292462080>')   
        try:  
            msg = ctx.message
            await msg.delete()
        except:
            pass   


    @commands.command(aliases=['ew'])
    async def emojiworry(self,ctx):
        """Gives a worried emoji.""" 
        await ctx.send(f'<a:frogworryrun:893714543245672468>')
        try:  
            msg = ctx.message
            await msg.delete()
        except:
            pass  


    @commands.command(aliases=['elg'])
    async def emojilesgo(self,ctx):
        """Gives a lesgo emoji."""
        await ctx.send(f'<:pandalesgo:893714821231542273>') 
        try:  
            msg = ctx.message
            await msg.delete()
        except:
            pass  
      

    @commands.command(aliases=['eb'])
    async def emojibruh(self,ctx):
        """Gives a bruh emoji.""" 
        await ctx.send(f'<:lttbruh:893714586669285386> ') 
        try:  
            msg = ctx.message
            await msg.delete()
        except:
            pass   
 

    @commands.command(aliases=['esp'])
    async def emojispace(self,ctx):
        """Gives a going through space emote."""
        await ctx.send(f'<a:peepspace:893715167332925512>') 
        try:  
            msg = ctx.message
            await msg.delete()
        except:
            pass  

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
        try:  
            msg = ctx.message
            await msg.delete()
        except:
            pass    


              

def setup(bot):
    bot.add_cog(Emojis(bot))          


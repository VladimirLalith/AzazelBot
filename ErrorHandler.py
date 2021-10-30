import discord
import traceback
from discord.ext import commands
import logging

logger = logging.getLogger('AzazelLog')

class CommandErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        logger = logging.getLogger('Azazellog')
        logger.setLevel(logging.DEBUG)
        logger.info("Error Handler Logged in")
        self.logger = logger

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """The event triggered when an error is raised while invoking a command.
        Parameters
        ------------
        ctx: commands.Context
            The context used for command invocation.
        error: commands.CommandError
            The Exception raised.
        """

        # This prevents any commands with local handlers being handled here in on_command_error.
        if hasattr(ctx.command, 'on_error'):
            return

        # This prevents any cogs with an overwritten cog_command_error being handled here.
        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = (commands.CommandNotFound, )

        # Allows us to check for original exceptions raised and sent to CommandInvokeError.
        # If nothing is found. We keep the exception passed to on_command_error.
        error = getattr(error, 'original', error)

        # Anything in ignored will return and prevent anything happening.
        if isinstance(error, ignored):
            return

        if isinstance(error, commands.DisabledCommand):
            await ctx.send(f'`{ctx.command} has been disabled.`')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(f'`{ctx.command} can not be used in Private Messages.`')
            except discord.HTTPException:
                pass

        # For this error example we check to see where it came from...
        elif isinstance(error, commands.BadArgument):
            await ctx.send('`I could not find that member. Please try again.`')
        
        elif isinstance(error, commands.MissingPermissions):
            if ctx.command.qualified_name == "embedrandom": # -> you can use if blocks inside to give specific errors for different commands
                await ctx.send("`I'm missing embed permissions`")

        else:
            # All other Errors not returned come here. And we can just print the default TraceBack.
            traceback_error = ''.join(traceback.format_exception(type(error), error, error.__traceback__))
            self.logger.error(f"Ignoring exception in command {ctx.command}:\nCommand Used - {ctx.message.content}\n{error}\n{traceback_error}")
            embed = discord.Embed(title="Command Error!",description=f"`This error has been forwarded to the bot developer and will be fixed soon.\nDo not spam errored commands, doing so will get you blacklisted.`",colour=discord.Colour.dark_gray())
            embed.add_field(name = "**Error:**", value= f"```py\n{error}```")
            try:
                #we try to send an embed
                await ctx.send(embed=embed)
            except:
                #if we're unable to send an embed then we send it as a message
                await ctx.send(f"**{embed.title}**\n{embed.description}\n\n**{embed.fields[0].name}**\n{embed.fields[0].value}")

    """Below is an example of a Local Error Handler for our command 'say' """




    async def sayerror(self, ctx, error):
        """A local Error Handler for our command 'say'.
        This will only listen for errors in 'say'.
        The global on_command_error will still be invoked after.
        """

        # Check if our required argument inp is missing.
        #commands.MissingRequiredArgument -> this is the error type
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'inp':
                await ctx.send("You forgot to give me input to repeat!")
                return
        traceback_error = ''.join(traceback.format_exception(type(error), error, error.__traceback__))
        self.logger.error(f"Ignoring exception in command {ctx.command}:\nCommand Used - {ctx.message.content}\n{error}\n{traceback_error}")

    
    async def cog_command_error(self, ctx, error):
        """ 
        This is an example a cog sepcific error handler
        This works same as the other Error handlers and 
        manages all th errors in that specific cog it is in only
        """
        traceback_error = ''.join(traceback.format_exception(type(error), error, error.__traceback__))
        self.logger.error(f"Ignoring exception in command {ctx.command}:\nCommand Used - {ctx.message.content}\n{error}\n{traceback_error}")

    async def send_error(bot: commands.Bot, ctx, error):
        embed = discord.Embed(title = "Command Error!", description = f"This error has been forwarded to the bot developer and will be fixed soon.\nIn the meanwhile please refrain from trying to recreate this error unnecessarily.\n\n```py\n{error}```", colour = discord.Colour(0x2F3136))
        embed.set_footer(text = "Spamming errored commands will get you blacklisted!", icon_url = ctx.author.avatar or ctx.author.default_avatar)
        await ctx.reply(embed = embed)

        # Log in Error Logs
        traceback_error = ''.join(traceback.format_exception(type(error), error, error.__traceback__))
        logger.error(f"{traceback_error}")

        # Now Log in Error Channel
        embed.description = f"{ctx.message.content}"

        embed.add_field(name = "Author:", value = f"{ctx.author.mention}\n (`{ctx.author.id}`)")
        if ctx.guild:
            embed.add_field(name = "Channel:", value = f"{ctx.channel.mention}\n (`{ctx.channel.id}`)")
            embed.add_field(name = "Guild:", value = f"**{ctx.guild}**\n (`{ctx.guild.id}`)")
        else:
            embed.add_field(name = "Dm Channel:", value = f"<#{ctx.channel.id}>\n (`{ctx.channel.id}`)")
        embed.add_field(name = "Message ID:", value = f"`{ctx.message.id}`")
        embed.add_field(name = "\u200b", value = f"**[\U0001f517 Jump to Error]({ctx.message.jump_url})**")

        # Split Error if it's longer than 1900k Charecter to fit discord limits
        split_error, final_error = "", []
        for line in traceback_error.split('\n'):
            if len(split_error + line) < 1900:
                split_error += f"\n{line}"

            else:
                final_error.append(split_error)
                split_error = ""
        final_error.append(split_error)

        error_channel = bot.get_channel(bot.config["errorchannel"])
        await error_channel.send(embed = embed)
        for e in final_error:
            await error_channel.send(f"```py\n{e}```")



def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
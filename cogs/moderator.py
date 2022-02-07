import discord
from discord.ext import commands

class Moderator(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def on_command_error(ctx, error):
        pass

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, limit:int):
        await ctx.channel.purge(limit=limit)
        await ctx.message.delete()

    @purge.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify the amount of messages you   want to clear. Usage: ?purge <number>')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('**You do not have manage_messages permssion!**')
    


def setup(client):
    client.add_cog(Moderator(client))
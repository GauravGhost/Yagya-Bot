import discord
from discord.ext import commands
wordsss = ['yagya']
class Greetings(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def hello(self,ctx):
        await ctx.reply("what! stfu")

    @commands.command()
    async def say(self, ctx,*, message):
        async with ctx.typing():
            await ctx.send(message)
            await ctx.message.delete()
        
    



def setup(client):
    client.add_cog(Greetings(client))

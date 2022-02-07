import discord
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Avatar command 
    @commands.command()
    async def avatar(self, ctx, *, member: discord.Member=None):
        '- Get the use profile picture'
        if not member:
            member = ctx.message.author
        userAvatar = member.avatar_url
        embed=discord.Embed(title=member, color=0xf50f0f)
        embed.set_image(url=userAvatar)
        embed.set_footer(text="requested by {0}".format(ctx.message.author))
        await ctx.send(embed=embed)
        


def setup(client):
    client.add_cog(Fun(client))
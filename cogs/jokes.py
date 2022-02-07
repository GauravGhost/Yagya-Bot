import discord
from discord.ext import commands
import requests
import json

class Jokes(commands.Cog):

    def __init__(self, client):
        self.client = client


    def get_jokes():
        response = requests.get('https://jokeapi.dev/joke/Any')
        jokeapi = json.loads(response.text)
        if jokeapi['type'] == 'single':
            return ("Yagya - " + jokeapi['joke'])
        elif jokeapi['type'] == 'twopart':
            return ("Yagya - " + jokeapi['setup'] + "\n" + "Luca - " +jokeapi['delivery'])

    @commands.command()
    async def joke(self, ctx):
        joke = Jokes.get_jokes()
        await ctx.send(joke)


def setup(client):
    client.add_cog(Jokes(client))
import os
import discord
from discord.ext import commands
import random
import dataYagya
from keep_alive import keep_alive
yagya_key = os.environ['TOKEN']

client = commands.Bot(command_prefix = '?')

initial_extensions = []

for filenames in os.listdir('./cogs'):
    if filenames.endswith('.py'):
        initial_extensions.append("cogs."+ filenames[:-3])

if __name__== '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)


@client.event
async def on_ready():
    print('we have logged as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content

    if any(word in msg for word in dataYagya.name):
        await message.channel.send(random.choice(dataYagya.name_action))
    await client.process_commands(message)


keep_alive()
client.run(yagya_key)

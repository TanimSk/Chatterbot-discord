import discord
import time
import interact
import random
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["API_KEY"]
intents = discord.Intents.all()
client = discord.Client(intents=intents)


talk = interact.Interact()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    # not reply to itself
    if message.author.id == client.user.id:
        return

    time.sleep(random.randint(2, 5))
    output = talk.talk(str(message.content))
    print(message.content)
    await message.channel.send(output)


client.run(TOKEN)




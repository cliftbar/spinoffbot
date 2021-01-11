import json
from typing import Dict

from discord import Client, Message

from spinoff import SpinoffBot


client: Client = Client()
spinoff: SpinoffBot = SpinoffBot(client)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return

    if message.content.startswith("!spinoff"):
        await spinoff.spinoff_channel(message)

with open("discord.json") as discord_fi:
    discord_conf: Dict = json.load(discord_fi)
client.run(discord_conf["bot_key"])

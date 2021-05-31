import discord
import os
from dotenv import load_dotenv


client=discord.Client()

TOKEN = 'ODQ4OTIxNjA5Mjc5NjM1NDY2.YLTp2w.YhVWxmZzhi3TTfKEHB6XiiNgydw'
day = "<testDay>"
time = "<testTime>"

@client.event
async def on_message(message):
    global day
    global time
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hello World!")
    if message.content == '$private':
        await message.author.send("Hello in private bro")
    if message.content.startswith('penis'):
        await message.channel.send("ben likes cock in the ass")
    if message.content.lower().startswith('when is the raid'):
        raidTime = "The raid is on " + day + " at " + time
        print(raidTime)
        await message.channel.send(raidTime)
    if message.content.startswith("!day"):
        words = message.content.split()
        day = words[1]
    if message.content.startswith("!time"):
        words = message.content.split()
        time = words[1]


@client.event
async def on_connect():
    print("Bot connected to the server!")
    channel = client.get_channel(848933122664824854)
    #await channel.send("just connected to bot channel")




client.run(TOKEN)

import discord
from discord.ext import commands
from discord import User
import os
from dotenv import load_dotenv
from discord import Spotify


bot = commands.Bot(command_prefix = "!")
load_dotenv()

TOKEN = os.getenv('TOKEN')
print(TOKEN)
day = "<testDay>"
time = "<testTime>"

userIdList = ["<@421765919350718465>", "<@480042900403650561>", "<@512656405916942338>",
 "<@643474698243538958>", "<@278593504500776960>", "<@327862828344279041>"]
userList = ['ben', 'billy', 'tom', 'will', 'jack', 'lewis']

@bot.command()
async def commands(ctx):
    await ctx.send("!day 'the day' - sets the day of the raid")
    await ctx.send("!time 'the time' - sets the time of the raid")
    await ctx.send("!ping 'all' or 'name, name etc...' - pings members about the raid")

@bot.command()
async def day(ctx, newDay):
    global day
    day = newDay

@bot.command()
async def time(ctx, newTime):
    global time
    time = newTime

@bot.command()
async def tom(ctx):
    await ctx.send("get your light up " + userIdList[2])

@bot.command()
async def ping(ctx, *args):
    global day
    global time
    print(day)
    print(time)
    people = []
    newIdList = []
    #code to ping certain people
    print(args)
    for person in args:
        if person == 'all':
            for id in userIdList:
                await ctx.send("raid on " + day + " at " + time + "! " + id)
            return
        people.append(person)
    for i in range(0, len(people)):
        newIdList.append(userIdList[userList.index(people[i])])

    for id in newIdList:
        await ctx.send("raid on " + day + " at " + time + "! " + id)


@bot.command()
async def raid(ctx):
    global day
    global time
    await ctx.send("raid on " + day + " at " + time + "!")


    # ben = "<@421765919350718465>"
    # billy = "<@480042900403650561>"
    # tom = "<@512656405916942338>"
    # will = "<@643474698243538958>"
    # jack = "<@278593504500776960>"
    # lewis = "<@327862828344279041>"
    # await ctx.send("raid on " + day + " at " + time + "! " + ben)
    # await ctx.send("raid on " + day + " at " + time + "! " + billy)
    # await ctx.send("raid on " + day + " at " + time + "! " + tom)
    # await ctx.send("raid on " + day + " at " + time + "! " + will)
    # await ctx.send("raid on " + day + " at " + time + "! " + jack)
    # await ctx.send("raid on " + day + " at " + time + "! " + lewis)
    # for id in userIdList:
    #     await ctx.send("raid on " + day + " at " + time + "! " + id)



@bot.event
async def on_connect():
    print("Bot connected to the server!")
    #await channel.send("just connected to bot channel")


bot.run(TOKEN)

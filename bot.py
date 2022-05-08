from ast import alias
import json
import discord
from discord.ext import commands

with open('./config/config.json') as config:
    data = json.load(config)
TOKEN = data['token']   

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command(aliases=['rules'])
async def rule(ctx, *, number):
    f = open("rules.txt", "r")
    rules = f.readlines()

    await ctx.send(rules[int(number)-1])

@client.command(aliases=['cls','delete'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit = amount)

@client.command(aliases=['meet','meetup'])
async def meet_ups(ctx):
    f = open("meetings.txt", "r")
    meet = f.readlines()
    for m in meet:
        await ctx.send(m)


client.run(TOKEN)
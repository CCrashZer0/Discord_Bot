from ast import alias
import json
import discord
from discord.ext import commands

with open('./config/config.json') as config:
    data = json.load(config)
TOKEN = data['token']   

client = commands.Bot(command_prefix="!")

f = open("rules.txt", "r")
rules = f.readlines()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command(aliases=['rules'])
async def rule(ctx, *, number):
    await ctx.send(rules[int(number)-1])

@client.command(aliases=['cls'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit = amount)

    
client.run(TOKEN)
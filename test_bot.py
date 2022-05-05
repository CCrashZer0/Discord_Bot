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

@client.command(aliases=['info'])
async def on_message(ctx):

    channel = client.get_channel(965306655678033981)
    print(f'{client.user} has responded to a message')                                  # This needs to be updated and used for logging
    msg = 'Hello {0.author.mention}.\n ACE678 is held on the second Wednesday of each month at 6pm.\n Come join us at the Marietta Square Market. \n https://mariettasquaremarket.com/'
    await channel.send(msg)


    
client.run(TOKEN)
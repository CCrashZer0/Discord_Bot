import json
import discord
from ast import alias
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

@client.command(aliases=['cmd',])
async def help_menu(ctx):
    cmds = ['!rules: Will provied you with a list of the channels rules. Example !rules 1 will give you the first rule.',
                '!delete: Will delete the previouse message, if you provide a number it will delete that many messages. Exampel !delete 3',
                '!meet: Provides you with a list of all the local meetings.'
                ]
    for c in cmds:
        await ctx.send(c)


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
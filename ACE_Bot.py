import json
import discord
from discord.ext import commands

with open('./config/config.json') as config:
    data = json.load(config)
TOKEN = data['token']                   # Enter your access token

client = discord.Client()
channel_id = client.get_user(965306655678033981)

@client.event

# @client.command()
async def listeners(ctx):
    if ctx.channel.id == 965306655678033981:
        # in the chosen channel so proceed to work correctly
        if message.content.startswith('info'):
            print(f'{client.user} has responded to a message')                                  # This needs to be updated and used for logging
            await message.channel.send("Test Received", reference=message)
            msg = 'Hello {0.author.mention}.\n ACE678 is held on the second Wednesday of each month at 6pm.\n Come join us at the Marietta Square Market. \n https://mariettasquaremarket.com/'.format(message)
            await message.channel.send(msg)
 
    else:
        # not in the chosen channel! don't work
        await ctx.send("wrong channel, bub")

# async def on_message(message):

#     # we do not want the bot to reply to itself
#     if message.author == client.user:
#         return

#     if message.content.startswith('info'):
#         print(f'{client.user} has responded to a message')                                  # This needs to be updated and used for logging
#         await message.channel.send("Test Received", reference=message)
#         msg = 'Hello {0.author.mention}.\n ACE678 is held on the second Wednesday of each month at 6pm.\n Come join us at the Marietta Square Market. \n https://mariettasquaremarket.com/'.format(message)
#         await message.channel.send(msg)
#         # await client.send_message(message.channel, msg)

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



client.run(TOKEN)



# bot = commands.Bot(command_prefix='$')
# channel = bot.get_channel(965306655678033981)
# async def test(ctx, arg):
#     await ctx.send(arg)

#     if (message.channel.id == channel): 
#         await message.channel.send('message goes here')

    # else:
    # # handle your else here, such as null, or log it to ur terminal

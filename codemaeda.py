# These are the dependecies.
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import platform

# Here you can modify the bot's prefix and description and whether it sends help in direct messages or not.
client = Bot(description="Komaeda Bot!!!", command_prefix="k!", pm_help=True)


@client.event
async def on_ready():
    print('Logged in as ' + client.user.name + ' (ID:' + client.user.id + ') | Connected to ' + str(
        len(client.servers)) + ' servers | Connected to ' + str(len(set(client.get_all_members()))) + ' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__,
                                                                               platform.python_version()))
    print('--------')
    print('Use this link to invite {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
    return await client.change_presence(
        game=discord.Game(name='Komaeda Time'))  # This is buggy, let us know if it doesn't work.


# This is a basic example of a call and response command. You tell it do "this" and it does it.


@client.command(pass_context=True)
async def ping(*args):
    await client.say(":ping_pong: Pong!")
    await asyncio.sleep(3)


@client.command(pass_context=True)
async def hello(*args):
    await client.say("Hello!!")
    await asyncio.sleep(3)


@client.command()
async def invite():
    await client.say("https://discordapp.com/oauth2/authorize?&client_id=407649458210340864&scope=bot&permissions=0")
    await asyncio.sleep(3)


@client.command()
async def join():
    await client.say("https://discord.gg/9rqbZek")
    await asyncio.sleep(3)


@client.command()
async def hope():
    await client.say("I love hope!!!")
    await asyncio.sleep(3)


@client.command()
async def members():
    await client.say(str(len(set(client.get_all_members()))) + ' users are experiencing Komaeda Time!')
    await asyncio.sleep(3)


client.run('NDA3NjQ5NDU4MjEwMzQwODY0.DV6_7g.gIQ8r4QAWfmoBdBqTFixqrYOkFU')

# Basic Bot was created by Habchy#1665
# Please join this Discord server if you need help: https://discord.gg/FNNNgqb
# The help command is currently set to be not be Direct Messaged.
# If you would like to change that, change "pm_help = False" to "pm_help = True" on line 

import asyncio
import platform
import random
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import string
from string import punctuation

# Here you can modify the bot's prefix and description and whether it sends help in direct messages or not.
client = Bot(description="It's Komaeda Time!", command_prefix="k!", pm_help=True)
startup_extensions = ["Music"]
bot = commands.Bot("k?")

new_punctuation = punctuation.replace('+', '')


def strip_punctuation(s):
    return ''.join(c for c in s if c not in new_punctuation)


# A collection of things Komaeda knows

basic_commands = ['ping', 'hello', 'piss', 'vore', 'toes', 'hope', 'server', 'invite', 'dad']
advanced_commands = ['say: repeats what you type afterwards', 'sayd: same as say but also deletes your message', 'members: shows how many members are online', 'swear: gives a random swear',
                     'd20: gives a random value between 1 and 20, good for roleplaying tabletop games', 'hewwo: returns a hewwo version of your input', 'birthday: returns a birthday message for your input']
'''update command list with all new commands'''

swears = ["Fuck", "Fuck you", "Shit", "Piss off", "Dickhead", "Asshole", "Bitch", "Son of a bitch", "Bastard",
          "Damn", "Cunt", "Bollocks", "Hell", "Chode", "Cuck", "My monster cock", "Mickey mouse's huge cock",
          "Dinosaur pussy", "Fuckin weed", "Smoke some fuckin weed"]


@client.event
async def on_message(message):
    if message.content.lower().startswith('k!say'):
        if message.content.lower().startswith('k!sayd'):
            await client.delete_message(message)
            asyncio.sleep(1)
        await client.send_message(message.channel, message.content[6:])
        await asyncio.sleep(3)
    elif message.content.lower().startswith('k!toes'):
            await client.send_message(message.channel, 'I really love sucking toes!!!')  # Another nastie joke
            await asyncio.sleep(3)
    elif str(message.author) == 'garfy#8888' and str(message.content) == "pwease don't tawk about toes :( toes awe gwoss":
        await client.delete_message(message)
        await asyncio.sleep(3)
    elif 'komaeda' in message.content.lower() or 'nagito' in message.content.lower():
        if str(message.author) == 'KomaedaBot#9510':
            pass
        else:

            await client.add_reaction(message, '❤')
            await client.send_message(message.channel, 'I love you, ' + str(message.author.display_name) + '.')
            if 'feet' in message.content.lower() or 'toes' in message.content.lower():
                if str(message.author) == 'KomaedaBot#9510':
                    pass
                else:
                    await client.add_reaction(message, '👀')
                    await client.add_reaction(message, '🇹')
                    await client.add_reaction(message, '🇴')
                    await client.add_reaction(message, '🇪')
                    await client.add_reaction(message, '🇸')
                    await asyncio.sleep(3)
    elif 'feet' in message.content.lower():
        if str(message.author) == 'KomaedaBot#9510':
            pass
        else:
            await client.add_reaction(message, '👀')
            await client.add_reaction(message, '🇹')
            await client.add_reaction(message, '🇴')
            await client.add_reaction(message, '🇪')
            await client.add_reaction(message, '🇸')
            await asyncio.sleep(3)
    elif 'toe' in message.content.lower():
        if str(message.author) == 'garfy#8888' or str(message.author) == 'KomaedaBot#9510':
            pass
        else:
            await client.add_reaction(message, '👀')
            await client.add_reaction(message, '🇹')
            await client.add_reaction(message, '🇴')
            await client.add_reaction(message, '🇪')
            await client.add_reaction(message, '🇸')
            await asyncio.sleep(3)
    elif message.content.lower().startswith('k!ping'):
        await client.send_message(message.channel, ":ping_pong: Pong!")  # A ping function, a basic test
        await asyncio.sleep(3)
    elif message.content.lower().startswith('k!hello'):
        await client.send_message(message.channel, "Hello!!")  # A fun hello!!! everyone likes feeling friendly
        await asyncio.sleep(3)
    elif message.content.lower().startswith('k!invite'):
        await client.send_message(message.channel, "https://discordapp.com/oauth2/authorize?client_id=407649458210340864&scope=bot&permissions=1341652161")  # Allows you to invite the bot to a server
        await asyncio.sleep(3)
    elif message.content.lower().startswith('k!server'):
        await client.send_message(message.channel, "https://discord.gg/9rqbZek")  # A link to the bot development server
        await asyncio.sleep(3)
    elif message.content.lower().startswith('k!hope'):
        await client.send_message(message.channel, "I love hope!!!")  # Komaeda really loves hope in the game
        await asyncio.sleep(3)
    elif message.content.lower().startswith('k!members'):
        await client.send_message(message.channel, str(len(set(client.get_all_members()))) + ' users are experiencing Komaeda Time!')  # Gives a number of people connected to Komaeda currently
        await asyncio.sleep(3)
    elif message.content.lower().startswith('k!piss'):
        await client.send_message(message.channel, "Widdle Cumaeda needs your piss to thrive")  # A nastie joke
        await asyncio.sleep(3)
    elif message.content.lower().startswith('k!dad'):
        await client.send_message(message.channel, "I love my daddy @Creamaeda#2228")  # A link to the creator of the bot
        await asyncio.sleep(3)

    elif message.content.lower().startswith('k!vore'):
        await client.send_message(message.channel, 'I just wanna get swallowed')  # 3rd nastie joke
        await asyncio.sleep(3)
    elif message.content.lower().startswith('k!swear'):
        await client.send_message(message.channel, random.choice(swears))  # My first experience with a randomized output
        await asyncio.sleep(3)
    elif message.content.lower().startswith('k!d20'):
        await client.send_message(message.channel, 'Komaeda rolls a ' + '**' + str(random.randint(1, 20)) + '**')
        await asyncio.sleep(3)

        await asyncio.sleep(3)
    elif message.content.lower().startswith('k!commands'):
        await client.send_message(message.channel,
                                  '```' + str(basic_commands[0:]) + '``` ```' + str(advanced_commands[0]) + '``` ```' + str(advanced_commands[1]) + '``` ```' + str(advanced_commands[2]) + '``` ```' + str(advanced_commands[3]) + '``` ```' + str(
                                      advanced_commands[4]) + '``` ```' + str(advanced_commands[5]) + '``` ```' + str(
                                      advanced_commands[6]) + '```')
        await asyncio.sleep(3)
    elif message.content.lower().startswith('k!birthday'):
        await client.send_message(message.channel, 'http://itsyourbirthday.today/#' + strip_punctuation(str(message.content)[11:].lower().replace(' ', '+')))
        await asyncio.sleep(3)
    elif message.content.lower().startswith('k!hewwo'):
        await client.send_message(message.channel, str(message.content)[7:].replace('l', 'w').replace('r', 'w') + ' UwU')
        await asyncio.sleep(3)
    elif message.content.lower().startswith('k!'):
        await client.send_message(message.channel, "I don't know that one, sorry.  ¯\_(ツ)_/¯")
        await asyncio.sleep(3)
    else:
        await bot.process_commands(message)


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
    return await client.change_presence(game=discord.Game(name="It's komaeda time! / k!"))


class Main_Commands:
    def __init__(self, bot):
        self.bot = bot


@client.command()
async def add(x, y):
    await client.say("The sum of " + str(int(x)) + " and " + str(int(y)) + " is " + str(int(x) + int(y)))
    await asyncio.sleep(3)


"""get this to work later lmao im not dealing with that"""

if __name__ == "__Main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('failed to load extension {}\n{}'.format(extension, exc))

client.run('NDA3NjQ5NDU4MjEwMzQwODY0.DV6_7g.gIQ8r4QAWfmoBdBqTFixqrYOkFU')


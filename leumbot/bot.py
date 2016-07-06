import random

import discord
from discord.ext import commands
from config import Config


description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix=None)

def build_bot(config='dev'):
    """
    Build leumbot using a config template
    Args:
        config: config as a string

    Returns:
        the leumbot
    """
    # load our config
    our_config = configs.get(config)()
    bot.command_prefix = "{0} ".format(our_config.bot_name)
    bot.description = our_config.description

    bot.run(our_config.oauth_token)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command
async def rip
	await client.send_file('meimei-and-chill', 'sa_rip.png')
	await bot.say('Ya, RIP')

@bot.command
async def smith
	await client.send.file('meimei-and-chill', 'sa_smith.png')
	
@bot.command()
async def jordanstory():
    """100% True stories about Jordan Judson from Tacoma, WA"""
    file = open('jordanstories.txt', 'r')
    stories = file.read().splitlines()
    story = random.choice(stories)
    await bot.say(story)

@bot.command()
async def add(*args):
    """Adds two numbers together."""
    await bot.say(sum([int(x) for x in args]))

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')


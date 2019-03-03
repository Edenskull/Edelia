import discord

from PyLogger.pylogger import pylogger
from plugins.config import CONFIGURATION
from discord.ext.commands import Bot
from discord import Game


BOT_PREFIX = ("$")
EXTENSIONS = [
    "plugins.eight_ball",
    "plugins.clan",
    "plugins.wallprint",
    "plugins.life",
    "plugins.coinflip"
]
TOKEN = CONFIGURATION.bot_token

# Setup bot prefix and the server id
edelia = Bot(command_prefix=BOT_PREFIX)


@edelia.event
async def on_ready():
    print(discord.__version__)
    print('Logged in as')
    print(edelia.user.name)
    print(edelia.user.id)
    print('------')
    await edelia.change_presence(game=Game(name="IA Become Humans"))


@edelia.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.CommandNotFound):
        return


if __name__ == '__main__':
    for extension in EXTENSIONS:
        edelia.load_extension(extension)
    edelia.run(TOKEN)


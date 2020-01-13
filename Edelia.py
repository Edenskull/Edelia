import discord
import os

from discord.ext import commands
from discord import Game
from config import Config


def _prefix_callable():
	base = [Config.get_option('PREFIX')]
	return base


edelia = commands.Bot(
	command_prefix=_prefix_callable(),
	description=Config.get_option("DESCRIPTION"),
	help_command=None,
	owner_id=Config.get_option("BOT_OWNER")
)


@edelia.event
async def on_ready():
	print(discord.__version__)
	print('Logged in as')
	print(edelia.user.name)
	print(edelia.user.id)
	print('------')
	await edelia.change_presence(activity=Game(name="IA Become Humans"))


@edelia.command(
	hidden=True
)
@commands.is_owner()
async def load(ctx, *, cog: str):
	await ctx.message.delete()
	await ctx.send("Loading {cog} Module ....".format(cog="cogs." + cog), delete_after=3)
	try:
		edelia.load_extension("cogs." + cog)
		await ctx.send("{cog} loaded successfully.".format(cog=cog), delete_after=3)
	except Exception as e:
		await ctx.send("Cannot load extension", delete_after=5)


@edelia.command(
	hidden=True
)
@commands.is_owner()
async def reload(ctx):
	await ctx.message.delete()
	await ctx.send("Reloading all the extensions", delete_after=3)
	print("Reloading all the extensions")
	for file in os.listdir("cogs"):
		if file.endswith('.py'):
			edelia.reload_extension('cogs.{}'.format(file.replace('.py', '')))
			print("{} Extension Loaded".format(file.replace('.py', '')))
	await ctx.send("Everything is reloaded.", delete_after=3)


@edelia.command(
	name="changeprefix",
	hidden=True
)
@commands.is_owner()
async def change_prefix(ctx, *, prefix: str):
	await ctx.message.delete()
	await ctx.send("Changing the prefix of the bot", delete_after=3)
	print("Changing prefix of the bot")
	current_conf = Config.get_config()
	previous_prefix = current_conf['PREFIX']
	current_conf['PREFIX'] = prefix
	Config.update_config(current_conf)
	print("Prefix changed")
	edelia.command_prefix = prefix
	await ctx.send("Have changed the prefix from {} to {}".format(
		previous_prefix,
		prefix
	), delete_after=3)


def edelia_init():
	for file in os.listdir("cogs"):
		if file.endswith('.py'):
			edelia.load_extension('cogs.{}'.format(file.replace('.py', '')))
			print("{} Extension Loaded".format(file.replace('.py', '')))
	edelia.run(Config.get_option("BOT_TOKEN"))


if __name__ == '__main__':
	edelia_init()

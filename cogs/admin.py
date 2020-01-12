import discord

from discord.ext import commands


class Admin(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(
		name='life',
		aliases=['ping'],
		description='Check the health of the bot'
	)
	@commands.has_any_role('Admin', 'Moderateur')
	async def life(self, ctx):
		await ctx.message.delete()
		embed = discord.Embed(title="Edelia Life Health", colour=discord.Colour(0xbd10e0))
		embed.set_thumbnail(url=self.bot.user.avatar_url)
		embed.set_author(name="Edelia", icon_url=self.bot.user.avatar_url)
		embed.add_field(
			name="---------------------",
			value=":heart: {} ms".format(
				int(self.bot.latency * 1000)
			)
		)
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Admin(bot))

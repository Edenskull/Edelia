import discord
import requests

from discord.ext import commands
from config import Config


class Weather(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(
		description="Send the weather in a specific city"
	)
	async def weather(self, ctx, *, city: str):
		await ctx.message.delete()
		data = requests.get(
			"https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(
				city,
				Config.get_option('WEATHER_API_KEY')
			)
		).json()
		embed = discord.Embed(title="Weather in {} : {}".format(
			city,
			data['weather'][0]['main']
		), colour=discord.Colour(0xffa500))
		embed.set_thumbnail(url="https://openweathermap.org/img/wn/{}@2x.png".format(
			data['weather'][0]['icon'])
		)
		embed.set_author(name="Edelia", icon_url=self.bot.user.avatar_url)
		embed.add_field(
			name="---------------------",
			value="{}°C and {}% humidity.".format(
				int(data['main']['temp']),
				data['main']['humidity']
			)
		)
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Weather(bot))

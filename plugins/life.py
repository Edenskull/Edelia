import discord

from discord.ext import commands


class Life:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='life',
        aliases=['ping'],
        description="Permet de savoir le ping du bot.",
        brief="Simple ping",
        pass_context=True
    )
    async def life(self, context):
        reponse = await self.bot.say("Pong!")
        embed = discord.Embed(title="Edelia Life Health", colour=discord.Colour(0xbd10e0))
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_author(name="Edelia", icon_url=self.bot.user.avatar_url)
        embed.add_field(
            name="---------------------", value=":heart: {} ms".format(
                int((reponse.timestamp - context.message.timestamp).total_seconds() * 1000)
            )
        )
        await self.bot.delete_message(reponse)
        await self.bot.say(embed=embed)


def setup(bot):
    bot.add_cog(Life(bot))

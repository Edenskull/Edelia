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
        await self.bot.say(
            "Je tourne a {} ms.".format(
                (reponse.timestamp - context.message.timestamp).total_seconds() * 1000.00
            )
        )


def setup(bot):
    bot.add_cog(Life(bot))

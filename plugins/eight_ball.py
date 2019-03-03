import discord
import random

from discord.ext import commands


class EightBall:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='8ball',
        description="Répond aux questions par oui ou non",
        brief="What did it think",
        pass_context=True
    )
    async def eight_ball(self, context):
        possible_responses = [
            'C\'est peut être possible',
            'Visiblement il se pourrait que peut être',
            'C\'est difficile à dire',
            'Surement'
        ]
        await self.bot.say(random.choice(possible_responses) + ", " + context.message.author.mention)


def setup(bot):
    bot.add_cog(EightBall(bot))

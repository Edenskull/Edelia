import discord
import random

from discord.ext import commands


class CoinFlip:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='coinflip',
        description="Petit jeu de pile ou face",
        brief="Lucky ?",
        pass_context=True
    )
    async def coinflip(self, context, choice):
        member = context.message.author
        possible_value = [
            'pile',
            'face'
        ]
        bot_choice = random.choice(possible_value).lower()
        if choice.lower() not in possible_value:
            await self.bot.say("{}, tu ne m\'as pas donné de choix valide. $help pour t\'aider".format(member.mention))
            return
        if choice.lower() == bot_choice:
            await self.bot.say("{}, tu as gagné {}.".format(bot_choice, member.mention))
        else:
            await self.bot.say("{}, tu as perdu {}.".format(bot_choice, member.mention))

    @coinflip.error
    async def coinflip_error(self, context, error: commands.errors.MissingRequiredArgument):
        await self.bot.say("Tu as oublié de me donner un choix.")


def setup(bot):
    bot.add_cog(CoinFlip(bot))

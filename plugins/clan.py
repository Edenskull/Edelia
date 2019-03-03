import discord

from discord.ext import commands
from plugins.config import CONFIGURATION


class Clan:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='clan',
        description="Permet de choisir son clan parmis ceux disponibles",
        brief="Selection de clan",
        pass_context=True
    )
    async def clan(self, context, clan):
        server = self.bot.get_server(CONFIGURATION.discord_server)
        member = context.message.author
        first_role = member.roles[1]
        admin_role = discord.utils.find(lambda r: r.name == "Admin", server.roles)
        if first_role.position < 1:
            await self.bot.say(
                "{}, Tu n\'est pas encore vérifié un {} va faire le necessaire dès que possible.".format(
                    member.mention,
                    admin_role.mention
                )
            )
            return
        if not member.bot:
            if clan.lower() in ["darkness", "tenebre"]:
                role_target = discord.utils.find(lambda r: r.name.lower() == "darkness", server.roles)
                role_remove = discord.utils.find(lambda r: r.name.lower() == "lightness", server.roles)
            elif clan.lower() in ["lightness", "lumiere"]:
                role_target = discord.utils.find(lambda r: r.name.lower() == "lightness", server.roles)
                role_remove = discord.utils.find(lambda r: r.name.lower() == "darkness", server.roles)
            else:
                await self.bot.say("Ce Clan n\'éxiste pas. $help pour plus d\'information sur comment utiliser cette commande.")
                return
            if role_target is not None or role_remove is not None:
                if role_target in member.roles:
                    await self.bot.say("{}, Tu es déjà dans ce clan.".format(member.mention))
                else:
                    await self.bot.remove_roles(member, role_remove)
                    await self.bot.add_roles(member, role_target)
                    await self.bot.say("{}, Tu es maintenant dans le clan {}.".format(member.mention, role_target.mention))
                return
        else:
            return

    @clan.error
    async def clan_error(self, context, error: commands.errors.MissingRequiredArgument):
        await self.bot.say("Tu as oublié de me donner un clan.")


def setup(bot):
    bot.add_cog(Clan(bot))

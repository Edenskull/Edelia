import discord

from discord.ext import commands
from googleapiclient.discovery import build
from google.oauth2 import service_account
from random import choice
from plugins.config import CONFIGURATION


SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'src/service_account.json'

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
scoped_credentials = credentials.with_scopes(SCOPES)
DRIVE = build('drive', 'v3', credentials=scoped_credentials)


class WallPrint:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='wallprint',
        description="Affiche un image aléatoire sortie du drive https://drive.google.com/drive/folders/0B2bTxNYUyJood202N3dRSDNCdG8",
        brief="Image aléatoire",
        pass_context=True
    )
    async def wallprint(self, context):
        server = self.bot.get_server(CONFIGURATION.discord_server)
        member = context.message.author
        try:
            first_role = member.roles[1]
        except IndexError:
            first_role = member.roles[0]
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
            response = DRIVE.files().list(
                q="'{}' in parents".format(CONFIGURATION.drive_id),
                spaces='drive',
                pageSize=1000,
                fields='files(webContentLink)'
            ).execute()
            liste_photo = response.get('files', [])
            unique = choice(liste_photo)['webContentLink']
            await self.bot.say(unique)


def setup(bot):
    bot.add_cog(WallPrint(bot))

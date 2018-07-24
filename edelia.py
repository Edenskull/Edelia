import logging
import asyncio
import discord
import time
from discord import Game
from random import choice, randint

from discord.ext import commands
from plugins.wallprint import randomwall
from plugins.config import token, chann_dem, server_id
from plugins.diablo import diabloacc
from plugins.urbandict import search
from plugins.twitch import twicth
from plugins._8ball import get_8ball

#Logging Setup

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log',
                              encoding='utf-8',
                              mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

edelia = commands.Bot(command_prefix='$')
server = edelia.get_server(id=server_id)


@edelia.command(name='wallpaper',
                description='Return a random wallpaper',
                brief='Surprise Kawaii',
                aliases=['wall', 'drive'])
async def wallpaper():
    img = randomwall()
    url = 'http://drive.google.com/uc?export=view&id=' + img[0]
    msg = "From : {} / {}".format(img[1],
                                  url)
    await edelia.say(msg)


@edelia.command(name='diablo',
                description='Return BattleNet Diablo profile informations',
                brief='Diablo Profile',
                aliases=['diablo3'],
                pass_context=True)
async def diablo(ctx, arg):
    status, req = diabloacc(arg)
    if status == 200:
        author = ctx.message.author.name
        avatar = ctx.message.author.avatar_url
        embed = discord.Embed(title="Diablo Account Informations",
                              colour=discord.Colour(0xff0000))
        embed.set_thumbnail(
            url="http://i2.wp.com/www.controlcommandescape.com/wp-content/uploads/2014/03/D3Icon.png?resize=1024%2C1024")
        embed.set_author(name=author,
                         icon_url=avatar)
        embed.set_footer(text="Diablo API",
                         icon_url="https://vignette.wikia.nocookie.net/diablo/images/a/a4/Diablo_III_icon.png/revision/latest?cb=20140316104004")
        embed.add_field(name="***{} / Paragon : {}***".format(req[0],
                                                              req[1]),
                        value="**Monster Kills : {}**\n**Elite Kills : {}**\n".format(req[3]['monsters'],
                                                                                      req[3]['elites']),
                        inline=False)
        embed.add_field(name="***Hero List***",
                        value="-",
                        inline=False)
        for hero in req[2]:
            if hero['gender'] == 0:
                genre = '<:boy:470699867048771585>'
            else:
                genre = '<:girl:470699831698915329>'
            embed.add_field(name="{} / Level : {}".format(hero['name'],
                                                          hero['level']),
                            value="**Class : {}**\n**Seasonal : {}**\n**Genre : {}**".format(hero['class'],
                                                                                             hero['seasonal'],
                                                                                             genre),
                            inline=True)
        await edelia.say(embed=embed)
    else:
        await edelia.say(
            "Sorry not found! <:what:470733005057425438>"
        )


@diablo.error
async def diablo_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        await edelia.say(
            'You need to do the same as **"$diablo <Battle Tag>"** to get me look for your account'
        )


@edelia.command(name='streamer',
                description='Ask Admins to be in streamers group',
                brief='Become Streamer',
                aliases=['addstreamer'],
                pass_context=True)
async def streamer(ctx, arg):
    author = ctx.message.author
    url = arg
    await edelia.send_message(edelia.get_channel(chann_dem),
                              "The user {} ask to be a streamer. His Channel : {}".format(author.mention,
                                                                                          url)
                              )
    await edelia.delete_message(ctx.message)


@streamer.error
async def streamer_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        await edelia.say(
            'You need to do the same as **"$streamer <URL stream>"** to allow admins to add it to <@159985870458322944>'
        )


@edelia.command(name='twitch',
                description='Show User given view count',
                brief='Show Twitch User',
                aliases=['twitchtv'],
                pass_context=True)
async def twitch(ctx, arg):
    data = twicth(arg)
    if data != 404:
        embed = discord.Embed(title="{}'s Profile ({})".format(data['display_name'],
                                                               data['login']),
                              colour=discord.Colour(0x990099),
                              url="https://twitch.tv/{}".format(data['login']),
                              description="{}\n**View Count :** {}".format(data['description'],
                                                                           data['view_count']))
        embed.set_thumbnail(url=data['profile_image_url'])
        embed.set_footer(text="Twitch",
                         icon_url="https://cdn.discordapp.com/attachments/470975678402265090/470976264707112980/GlitchIcon_Purple_24px.png")
        await edelia.say(embed=embed)
    else:
        await edelia.say(
            "Ano ne ... This user doesn't exist <:omaewa:470735969709064192>"
        )


@twitch.error
async def twitch_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        await edelia.say(
            'You need to do the same as **"$twitch <Username>"** to let me search for your profile'
        )


@edelia.command(name='donate',
                description='Help Fluffyneko to become rich',
                brief='Donate',
                aliases=['flouze', 'money', 'donation'])
async def donate():
    embed = discord.Embed(title="Donation",
                          colour=discord.Colour(0x0066ff))
    embed.set_image(url="https://pbs.twimg.com/profile_images/1014219302495375360/dIgZhxTm_400x400.jpg")
    embed.set_thumbnail(
        url="https://pbs.twimg.com/profile_images/1017078560102678530/UguviZhT_400x400.jpg")
    embed.set_footer(text="Streamlabs",
                     icon_url="https://pbs.twimg.com/profile_images/1017078560102678530/UguviZhT_400x400.jpg")
    embed.add_field(name="Donate Here :",
                    value="https://streamlabs.com/imfluffyneko")
    await edelia.say(embed=embed)


@edelia.command(name='word',
                description='Dynamic Dictionnary use to get definitions of words',
                brief='Word Dictionnary',
                aliases=['larousse', 'robert', 'def'],
                pass_context=True)
async def word(ctx, *args):
    defin = ""
    urban = search(args)
    if urban != 404:
        defin += "Definition **{}**: {}\n".format(urban['word'],
                                                  urban['definition'])
        await edelia.say(defin)
    else:
        await edelia.say(
            "404 Error....Bzzz Bzzzzz <:blushed:470736726587867137>"
        )


@word.error
async def word_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        await edelia.say(
            'You need to do the same as **"$word <word>"** to let me show you the definition'
        )


@edelia.command(name='coinflip',
                description='Simple CoinFlip Game with Edelia',
                brief='Coinflip Game',
                aliases=['piece', 'pileouface'],
                pass_context=True)
async def coinflip(ctx, arg):
    choose = [['recto', 'pile'], ['verso', 'face']]
    botc = choice(choose)
    if arg in botc:
        await edelia.say(
            "{} you win".format(arg)
        )
    else:
        form = " (".join(botc) + ")"
        msg = "{} you lose".format(form)
        await edelia.say(msg)


@coinflip.error
async def coinflip_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        await edelia.say(
            'You need to do the same as **"$coinflip <pile,recto|face,verso>"** to play with me'
        )


@edelia.command(name='roll',
                description='Simple dice roll',
                brief='Dice Roll',
                aliases=['dice', 'diceroll'],
                pass_context=True)
async def roll(ctx, arg="", arg2=""):
    if arg != "duel":
        author = ctx.message.author
        dice = randint(1, 6)
        mess = await edelia.say(
            "{0.mention} Dice Roll".format(author)
        )
        await edelia.edit_message(message=mess,
                                  new_content="{0.mention} Dice Roll .".format(author))
        asyncio.sleep(1)
        await edelia.edit_message(message=mess,
                                  new_content="{0.mention} Dice Roll . .".format(author))
        asyncio.sleep(1)
        await edelia.edit_message(message=mess,
                                  new_content="{0.mention} Dice Roll . . .".format(author))
        asyncio.sleep(1)
        await edelia.edit_message(message=mess,
                                  new_content="{0.mention} Dice Roll . . . {1}".format(author,
                                                                                       dice))
    else:
        if arg2 != "":
            message = ctx.message
            author = ctx.message.author
            dice = randint(1, 6)
            member = ctx.message.mentions
            member = member[0]
            phrase = await edelia.say(
                "{0.mention} Dice Roll . . . {1} now it\'s up to now {2.mention} say something to roll".format(author,
                                                                                                               dice,
                                                                                                               member)
            )
            response = await edelia.wait_for_message(timeout=7,
                                                     author=member)
            if response is not None:
                dice2 = randint(1, 6)
                if dice2 > dice:
                    await edelia.say(
                        "{0.mention} Dice Roll . . . {1}, get owned {2.mention}".format(member,
                                                                               dice2,
                                                                               author)
                    )
                else:
                    await edelia.say(
                        "{0.mention} Dice Roll . . . {1}, it seems that you got beaten, gg {2.mention}".format(member,
                                                                                                      dice2,
                                                                                                      author)
                    )
            else:
                await edelia.delete_message(message=message)
                await edelia.delete_message(message=phrase)
        else:
            await edelia.say(
                'You need to do the same as **"$dice duel <@user>"** to play with him'
            )


@edelia.command(name='eightball',
                description='Talk with edelia about things she will answer by yes or no',
                brief='Talk to Edelia',
                aliases=['8ball'],
                pass_context=True)
async def eightball(ctx, *args):
    reponse = get_8ball(" ".join(args))
    if reponse != 404:
        await edelia.say(
            reponse
        )
    else:
        await edelia.say(
            "I\'m Broken . . . . . . . . . . . . . . . . . . . . . . . . Program Restart @"
        )


@edelia.command(name='ping',
                description='Simple ping test for Edelia',
                brief='Pong',
                aliases=['health', 'edelia'],
                pass_context=True)
async def ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await edelia.send_typing(channel)
    t2 = time.perf_counter()
    await edelia.say(
        "Ping : {}ms".format(round((t2-t1)*1000))
    )


@edelia.event
async def on_ready():
    print(discord.__version__)
    print('Logged in as')
    print(edelia.user.name)
    print(edelia.user.id)
    print('------')
    await edelia.change_presence(game=Game(name="IA Become Humans"))

edelia.run(token)


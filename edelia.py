# Libraries import
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

# Logging setup in debug mode
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log',
                              encoding='utf-8',
                              mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Setup bot prefix and the server id
edelia = commands.Bot(command_prefix='$')
server = edelia.get_server(id=server_id)


# Wallpaper command used for prompt wallpaper from google drive
@edelia.command(name='wallpaper',
                description='Return a random wallpaper',
                brief='Surprise Kawaii',
                aliases=['wall', 'drive'])
async def wallpaper():
    img = randomwall()  # Call of the function from wallprint plugin
    url = 'http://drive.google.com/uc?export=view&id=' + img[0]
    msg = "From : {} / {}".format(img[1],
                                  url)
    await edelia.say(msg)


# Diablo command used for prompt diablo specific profile with characters
@edelia.command(name='diablo',
                description='Return BattleNet Diablo profile informations',
                brief='Diablo Profile',
                aliases=['diablo3'],
                pass_context=True)
async def diablo(ctx, arg):
    status, req = diabloacc(arg)  # Call of the function from diablo plugin
    if status == 200:  # This test if the user has been found
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
                genre = '<:boy:470699867048771585>'  # Those are specific emote from our server
            else:
                genre = '<:girl:470699831698915329>'  # You can retrieve this code typing \:emote: in discord
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
            # <:what:470733005057425438> is a specific emote from our server
        )


# This is the throwing function for diablo command used when the user type $diablo without args
@diablo.error
async def diablo_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):  # This test if the command error is missing args
        await edelia.say(
            'You need to do the same as **"$diablo <Battle Tag>"** to get me look for your account'
        )


# Streamer command used for ask admins to grant you the streamer status
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


# This is the throwing function for streamer command used when the user type $streamer without args
@streamer.error
async def streamer_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        await edelia.say(
            'You need to do the same as **"$streamer <URL stream>"** to allow admins to add it to <@159985870458322944>'
            # <@159985870458322944> is the mention mee6 you can get it by typing \@mee6 in discord
        )


# Twitch command used for prompt specific twitch profile
@edelia.command(name='twitch',
                description='Show User given view count',
                brief='Show Twitch User',
                aliases=['twitchtv'],
                pass_context=True)
async def twitch(ctx, arg):
    data = twicth(arg)  # Call of the function from twitch plugin
    if data != 404:  # This test if the user has been found
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
            # <:omaewa:470735969709064192> is a specific emote from our server
        )


v
@twitch.error
async def twitch_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        await edelia.say(
            'You need to do the same as **"$twitch <Username>"** to let me search for your profile'
        )


# Donate command used for prompt the donation page of imfluffyneko
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


# Word command used for prompt definition of a specific word
@edelia.command(name='word',
                description='Dynamic Dictionnary use to get definitions of words',
                brief='Word Dictionnary',
                aliases=['larousse', 'robert', 'def'],
                pass_context=True)
async def word(ctx, *args):
    defin = ""  # We init defin to be sure it is empty
    urban = search(args)  # Call of the function from urbandict plugin
    if urban != 404:  # This test is the word has been found
        defin += "Definition **{}**: {}\n".format(urban['word'],
                                                  urban['definition'])
        await edelia.say(defin)
    else:
        await edelia.say(
            "404 Error....Bzzz Bzzzzz <:blushed:470736726587867137>"
            # <:blushed:470736726587867137> is a specific emote from our server
        )


# This is the throwing function for word command used when the user type $word without args
@word.error
async def word_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        await edelia.say(
            'You need to do the same as **"$word <word>"** to let me show you the definition'
        )


# Coinflip command used for play against Edelia at toss heads or tails
@edelia.command(name='coinflip',
                description='Simple CoinFlip Game with Edelia',
                brief='Coinflip Game',
                aliases=['piece', 'pileouface'],
                pass_context=True)
async def coinflip(ctx, arg):
    choose = [['recto', 'pile', 'heads'], ['verso', 'face', 'tails']]  # "Dictionary for the word heads or tails
    botc = choice(choose)  # Random choice in the dictionary
    if arg in botc:  # Test if the argument is in the random choice
        await edelia.say(
            "{} you win".format(arg)
        )
    else:
        form = "(" + ", ".join(botc) + ")"
        msg = "{} you lose".format(form)
        await edelia.say(msg)


# This is the throwing function for coinflip command used when the user type $coinflip without args
@coinflip.error
async def coinflip_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        await edelia.say(
            'You need to do the same as **"$coinflip <pile,recto|face,verso>"** to play with me'
        )


# Roll command used for play against Edelia or duel someone at dice toss
@edelia.command(name='roll',
                description='Simple dice roll',
                brief='Dice Roll',
                aliases=['dice', 'diceroll'],
                pass_context=True)
async def roll(ctx, arg="", arg2=""):  # Here we setup two args for the duel part
    if arg != "duel":  # This test if the first arg isn't duel (means simple dice roll
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
        # We made this to make it a bit animated
    else:  # Then if it's duel
        if arg2 != "":  # This test if the user has typed the person to duel
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
            # Here we wait for the duel person to answer something
            if response is not None:
                dice2 = randint(1, 6)
                if dice2 > dice:  # This test if the caller win or not
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
            else:  # If he waited to long we delete messages
                await edelia.delete_message(message=message)
                await edelia.delete_message(message=phrase)
        else:
            await edelia.say(
                'You need to do the same as **"$dice duel <@user>"** to play with him'
            )


# Eightball command used for ask a question to Edelia she will respond by typical yes or no phrase
@edelia.command(name='eightball',
                description='Talk with edelia about things she will answer by yes or no',
                brief='Talk to Edelia',
                aliases=['8ball'],
                pass_context=True)
async def eightball(ctx, *args):
    reponse = get_8ball(" ".join(args))  # Call of the function from _8ball plugin
    if reponse != 404:  # This test if the GET has been working
        await edelia.say(
            reponse  # If the GET works fine the reponse should be in plain text here
        )
    else:
        await edelia.say(
            "I\'m Broken . . . . . . . . . . . . . . . . . . . . . . . . Program Restart @"  # Great joke
        )


# Ping command used for prompt Edelia Health in ms
@edelia.command(name='ping',
                description='Simple ping test for Edelia',
                brief='Pong',
                aliases=['health', 'edelia'],
                pass_context=True)
async def ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()  # First time count
    await edelia.send_typing(channel)  # Then we send a bot action to the server like typing
    t2 = time.perf_counter()  # second time count
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
    await edelia.change_presence(game=Game(name="IA Become Humans"))  # This is set to change the game the bot is playing

edelia.run(token)


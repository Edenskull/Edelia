# Edelia
Bot Discord For The NekoTwitch Server
## Bot Commands
You will be able to use Edelia with the prefix **$** before every command 

Command | Aliases | Description
------- | ------- | -----------
[coinflip](#Coinflip) | piece, pileouface | Coinflip Game
[diablo](#Diablo) | diablo3 | Diablo Profile
[donate](#Donate) | flouze, money, donation | Donate Page
[eightball](#Eightball) | 8ball | Ask Edelia
[help](#Help) | None | Help Edelia Bot
[ping](#Ping) | None | Ping Command
[roll](#Roll) | dice, diceroll | Dice Roll Game
[streamer](#Streamer) | addstreamer | Become Streamer
[twitch](#Twitch) | twitchtv | Show Twitch User
[wallpaper](#Wallpaper) | wall, drive | Random Wallpaper
[word](#Word) | larousse, robert, def | Word Definition

## Detailed Commands
### Coinflip
#### Usage
$coinflip <pile,recto|face,verso>  
Edelia will choose between recto or verso and congrats you if you win.
#### Response
Edelia will respond in the same chat as the call one.
### Diablo
#### Usage
$diablo <BattleTag#ID> *BattleTag#ID* like EdenSkull#2368   
Edelia will retrieve your diablo account information and embed it in discord.
#### Response
Edelia will respond in the same chat as the call one.
### Donate
#### Usage
$donate  
Edelia will embed the donation page from nekotwitch into discord chat.
#### Response
Edelia will respond in the same chat as the call one.
### Eightball
#### Usage
$eightball \<Question>  
Edelia will respond to your questions like a 8ball magic.
#### Response
Edelia will respond in the same chat as the call one.
### Help
#### Usage
$help  
Edelia will provide you the help page to use her.
#### Response
Edelia will respond in the same chat as the call one.
### Ping
#### Usage
$ping  
Edelia will return her ping to discord in ms.
#### Response
Edelia will respond in the same chat as the call one.
### Roll
#### Usage
$roll  
Edelia will roll a dice for you and prompt the result

$roll duel <@User> *@User* is a mentioned user  
Edelia will roll a dice for you and prompt the result then ask the duelist to talk to roll another dice for him and compare the results.
#### Response
Edelia will respond in the same chat as the call one. If the duelist don't answer, Edelia will delete the messages.
### Streamer
#### Usage
$streamer \<URL> *URL* is the link to your stream page  
Edelia will ask admins to add author in streamer group.
#### Response
Edelia will respond in a specific channel given in the config.json file. 
### Twitch
#### Usage
$twitch <Login> *Login* is the login that you use to connect twitch  
Edelia will retrieve some of you twitch data and parse them into discord.
#### Response
Edelia will respond in the same chat as the call one.
### Wallpaper
#### Usage
$wallpaper  
Edelia will retrieve a random wallpaper from the given drive folder id and print it with a description.
#### Response
Edelia will respond in the same chat as the call one.
### Word
#### Usage
$word <Word> *Word* is a simple word or composed word  
Edelia will find the definition of the given word and give it to you.
#### Response
Edelia will respond in the same chat as the call one.



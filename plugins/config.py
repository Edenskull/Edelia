import json

with open('src\config.json') as f:
    global driveid, token, diablokey, twitchid, twitchsecr
    data = json.load(f)
    driveid = data['drive_id']
    token = data['bot_token']
    diablokey = data['diablo_key']
    twitchid = data['twitch_client']
    twitchsecr = data['twitch_secret']
    chann_dem = data['channel_demande']
    server_id = data['discord_id']
    # Here we just retrieve all our config token, key etc....

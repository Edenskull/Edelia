import json
import requests

from plugins.config import twitchid, twitchsecr
from urllib.parse import quote

def twicth(user):
    result = requests.post(
        'https://id.twitch.tv/oauth2/token?client_id={}&client_secret={}&grant_type=client_credentials'.format(twitchid,
                                                                                                               twitchsecr)
    )
    result = result.json()
    token = result['access_token']
    headers = {"Authorization": "Bearer {}".format(token)}
    result = requests.get('https://api.twitch.tv/helix/users?login={}'.format(quote(user)), headers=headers)
    data = result.json()
    print(result.status_code)
    if result.status_code == 200:
        if data['data']:
            return data['data'][0]
        else:
            return 404
    else:
        return 404

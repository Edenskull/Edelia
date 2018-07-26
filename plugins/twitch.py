import json
import requests

from plugins.config import twitchid, twitchsecr
from urllib.parse import quote

def twicth(user):
    result = requests.post(
        'https://id.twitch.tv/oauth2/token?client_id={}&client_secret={}&grant_type=client_credentials'.format(twitchid,
                                                                                                               twitchsecr)
    )  # This is the POST request to retrieve an access_token
    result = result.json()
    token = result['access_token']
    headers = {"Authorization": "Bearer {}".format(token)}  # We set the payload for the GET request
    result = requests.get('https://api.twitch.tv/helix/users?login={}'.format(quote(user)), headers=headers)
    data = result.json()
    if result.status_code == 200:  # The API return empty data when not found to we test it on two check
        if data['data']:
            return data['data'][0]
        else:
            return 404
    else:
        return 404

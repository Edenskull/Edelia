import json
import requests

from plugins.config import diablokey
from urllib.parse import quote

def diabloacc(btag):
    values = []
    response = requests.get(
        'https://eu.api.battle.net/d3/profile/{}/?locale=fr_FR&apikey={}'.format(quote(btag), diablokey)
    )  # this is the GET request to the BattleNet API
    if response.status_code == 200:  # This test if the request has been working
        data = response.json()  # We parse it in json
        values.append(data['battleTag'])  # Then we append all the values in an array
        values.append(data['paragonLevel'])
        values.append(data['heroes'])
        values.append(data['kills'])
        values.append(data['guildName'])
        return 200, values  # Here we return the status and the array
    elif response.status_code == 404:
        return 404, ""

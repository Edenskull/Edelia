import json
import requests

from plugins.config import diablokey
from urllib.parse import quote

def diabloacc(btag):
    values = []
    response = requests.get(
        'https://eu.api.battle.net/d3/profile/{}/?locale=fr_FR&apikey={}'.format(quote(btag), diablokey)
    )

    if response.status_code == 200:
        data = response.json()
        values.append(data['battleTag'])
        values.append(data['paragonLevel'])
        values.append(data['heroes'])
        values.append(data['kills'])
        values.append(data['guildName'])
        return 200, values
    elif response.status_code == 404:
        return 404, ""

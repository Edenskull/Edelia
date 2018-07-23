import json
import requests
from urllib.parse import quote

def search(tab):
    temp = ""
    query = " ".join(tab)
    data = requests.get('http://api.urbandictionary.com/v0/define?term={}'.format(quote(query)))
    result = data.json()
    if data.status_code == 200:
        if result['list']:
            temp = result['list'][0]
            return temp
        else:
            return 404
    else:
        return 404

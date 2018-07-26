import json
import requests
from urllib.parse import quote


def search(tab):
    temp = ""  # We init temp to be sure it is empty
    query = " ".join(tab)  # We join those args with space because we can convert to URL after
    data = requests.get('http://api.urbandictionary.com/v0/define?term={}'.format(quote(query)))  # Quote convert to URL
    result = data.json()
    if data.status_code == 200:  # This test if the request has been working
        if result['list']:  # The request return empty result if not found then we two check
            temp = result['list'][0]
            return temp
        else:
            return 404
    else:
        return 404

import requests
from urllib.parse import quote
import json


def get_8ball(question):
    data = requests.get('https://8ball.delegator.com/magic/JSON/{}'.format(quote(question)))
    if data.status_code == 200:
        answer = data.json()
        return answer['magic']['answer']
    else:
        return 404

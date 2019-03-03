from json import load


class Config:
    def __init__(self):
        with open('src/config.json', 'r') as config:
            configstr = load(config)
        self.bot_token = configstr['bot_token']
        self.discord_server = configstr['discord_id']
        self.drive_id = configstr['drive_id']


CONFIGURATION = Config()

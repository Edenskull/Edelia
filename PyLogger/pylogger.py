import logging

filename = "log/{}.log".format("Edelia")

pylogger = logging.getLogger('discord')
pylogger.setLevel(logging.DEBUG)

handler = logging.FileHandler(filename, 'w', 'utf-8')
formatter = logging.Formatter(
    fmt='[%(asctime)s][%(levelname)s] : [%(filename)s][%(funcName)s] : %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S"
)

handler.setFormatter(formatter)
pylogger.addHandler(handler)

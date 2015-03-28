import json


class Config(object):

    def __init__(self):
        with open("Data/config.json") as f:
            data = json.load(f)
            self.__data = data["config"]

    def get(self, key):
        return self.__data[key]
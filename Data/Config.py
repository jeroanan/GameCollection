import json
import os


class Config(object):

    def __init__(self):
        with open("Data/config.json") as f:
            data = json.load(f)
            self.__data = data["config"]

    def get(self, key):
        return self.__data[key]

    def get_mongo_url(self):
        # get mongo url from env
        mongo_url = os.getenv("MONGO_URL", "")
        if not mongo_url:
            raise ValueError("MONGO_URL environment variable not set")
        return mongo_url

    def get_mongo_port(self):
        mongo_port = int(os.getenv("MONGO_PORT", ""))
        if not mongo_port:
            raise ValueError("MONGO_PORT environment variable not set")
        return mongo_port
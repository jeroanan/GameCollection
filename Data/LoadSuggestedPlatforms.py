import json
from Platform import Platform


class LoadSuggestedPlatforms(object):
    def __init__(self):
        with open("Data/SuggestedPlatforms.json") as f:
            data = json.load(f)
            self.__data = data["platforms"]

    def get(self):
        platforms = []
        for item in self.__data:
            platform = Platform()
            platform.name = item["name"]
            platform.description = item["description"]
            platforms.append(platform)
        return platforms

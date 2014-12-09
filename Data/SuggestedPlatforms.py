from Platform import Platform


class SuggestedPlatforms(object):

    def __init__(self):
        self.__data = [
            {
                "Name": "Nintendo Entertainment System",
                "Description": "Nintendo NES"
            },
            {
                "Name": "Sega Megadrive",
                "Description": "Sega Megadrive/Genesis"
            }
        ]

    def get(self):
        for item in self.__data:
            platform = Platform()
            platform.name = item["Name"]
            platform.description = item["Description"]
            yield platform

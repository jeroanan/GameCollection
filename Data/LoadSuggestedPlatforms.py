from Data.DataLoad import DataLoad
from Platform import Platform


class LoadSuggestedPlatforms(DataLoad):
    def __init__(self):
        super().__init__("Data/SuggestedPlatforms.json", "platforms")

    def get(self):
        platforms = []
        for item in self.data:
            platform = Platform()
            platform.name = item["name"]
            platform.description = item["description"]
            platforms.append(platform)
        return platforms

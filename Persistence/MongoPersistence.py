from bson import ObjectId
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import sys
from Persistence.Mappers.ResultToGameMapper import ResultToGameMapper
from Persistence.Mappers.ResultToHardwareMapper import ResultToHardwareMapper
from Persistence.Mappers.ResultToPlatformMapper import ResultToPlatformMapper


class MongoPersistence(object):

    def __init__(self):
        self.__client = None
        self.__init_mongo_client()
        self.__db = self.__client.GamesCollection

    def __init_mongo_client(self):
        try:
            self.__client = MongoClient()
        except ConnectionFailure:
            print("No instance of MongoDB detected. Did you forget to start it?")
            sys.exit(-1)

    def __del__(self):
        if self.__client is not None:
            self.__client.close()

    def add_game(self, game):
        self.__db.games.insert(game.__dict__)

    def get_all_games(self):
        return map((ResultToGameMapper()).map, self.__db.games.find())

    def get_game(self, game_id):
        cursor = self.__db.games.find_one({"_id": ObjectId(game_id)})
        return (ResultToGameMapper()).map(cursor)

    def get_platforms(self):
        return map(ResultToPlatformMapper().map, self.__db.platforms.find())

    def get_platform(self, platform_id):
        mongo_result = self.__db.platforms.find_one({"_id": ObjectId(platform_id)})
        return ResultToPlatformMapper().map(mongo_result)

    def add_platform(self, platform):
        self.__db.platforms.insert(platform.__dict__)

    def update_platform(self, platform):
        self.__db.platforms.update({"_id": ObjectId(platform.id)}, {"$set": platform.__dict__}, upsert=False)

    def delete_platform(self, platform):
        self.__db.platforms.remove({"_id": ObjectId(platform.id)})

    def update_game(self, game):
        self.__db.games.update({"_id": ObjectId(game.id)}, {"$set": game.__dict__}, upsert=False)

    def delete_game(self, game):
        self.__db.games.remove({"_id": ObjectId(game.id)})

    def get_hardware_list(self):
        return map((ResultToHardwareMapper()).map, self.__db.hardware.find())

    def get_hardware_details(self, platform_id):
        h = self.__db.hardware.find_one({"_id": ObjectId(platform_id)})
        return ResultToHardwareMapper().map(h)

    def save_hardware(self, hardware):
        self.__db.hardware.insert(hardware.__dict__)

    def update_hardware(self, hardware):
        pass

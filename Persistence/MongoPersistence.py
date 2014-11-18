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
        games = self.__db.games
        games.insert(game.__dict__)

    def get_all_games(self):
        return map((ResultToGameMapper()).map, self.__db.games.find())

    def get_game(self, game_id):
        games = self.__db.games
        cursor = games.find_one({"_id": ObjectId(game_id)})
        mapper = ResultToGameMapper()
        return mapper.map(cursor)

    def get_platforms(self):
        return map(ResultToPlatformMapper().map, self.__db.platforms.find())

    def add_platform(self, platform):
        platforms = self.__db.platforms
        platforms.insert(platform.__dict__)

    def update_game(self, game):
        games = self.__db.games
        games.update({"_id": ObjectId(game.id)}, {"$set": game.__dict__}, upsert=False)

    def delete_game(self, game):
        games = self.__db.games
        games.remove({"_id": ObjectId(game.id)})

    def get_hardware_list(self):
        h = self.__db.hardware
        hardware = h.find()
        mapper = ResultToHardwareMapper()
        ret_val = []
        for item in hardware:
            ret_val.append(mapper.map(item))
        return ret_val

    def save_hardware(self, hardware):
        h = self.__db.hardware
        h.insert(hardware.__dict__)

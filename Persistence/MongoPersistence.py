import sys

from bson import ObjectId
from pymongo import MongoClient
import pymongo
from pymongo.errors import ConnectionFailure

from AbstractPersistence import AbstractPersistence
from Persistence.Mappers.ResultToGameMapper import ResultToGameMapper
from Persistence.Mappers.ResultToGenreMapper import ResultToGenreMapper
from Persistence.Mappers.ResultToHardwareMapper import ResultToHardwareMapper
from Persistence.Mappers.ResultToPlatformMapper import ResultToPlatformMapper
from Persistence.Mappers.SortFieldMapper import SortFieldMapper


class MongoPersistence(AbstractPersistence):

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

    def get_all_games(self, sort_field, number_of_games=999999, sort_order="ASC"):
        sorder = pymongo.ASCENDING
        if sort_order is not None and sort_order.upper() == "DESC":
            sorder = pymongo.DESCENDING

        mapped_sort_field = SortFieldMapper().map(sort_field)
        return map((ResultToGameMapper()).map, self.__db.games.find(limit=number_of_games).sort(mapped_sort_field,
                                                                                                sorder))

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
        self.__db.hardware.update({"_id": ObjectId(hardware.id)}, {"$set": hardware.__dict__}, upsert=False)

    def delete_hardware(self, hardware_id):
        self.__db.hardware.remove({"_id": ObjectId(hardware_id)})

    def get_genres(self):
        return map(ResultToGenreMapper().map, self.__db.genres.find())

    def add_genre(self, genre):
        self.__db.genres.insert(genre.__dict__)

    def get_genre_details(self, genre_id):
        g = self.__db.genres.find_one({"_id": ObjectId(genre_id)})
        return ResultToGenreMapper().map(g)

    def update_genre(self, genre):
        pass

    def delete_genre(self, genre_id):
        pass
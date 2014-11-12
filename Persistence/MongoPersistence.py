from pymongo import MongoClient
from Game import Game
from Platform import Platform


class MongoPersistence(object):

    def __init__(self):
        self.__client = MongoClient()
        self.__db = self.__client.GamesCollection

    def __del__(self):
        self.__client.close()

    def add_game(self, game):
        games = self.__db.games
        games.insert(game.__dict__)

    def get_all_games(self):
        games = self.__db.games
        cursor = games.find()
        out_games = []
        for g in cursor:
            game = self.__map_mongo_result_to_game(g)
            out_games.append(game)
        return out_games

    def __map_mongo_result_to_game(self, result):
        game = Game()
        game.id = result["_id"]
        game.title = result["_Game__title"]
        game.platform = result["_Game__platform"]
        game.num_copies = result["_Game__num_copies"]
        game.num_boxed = result["_Game__num_boxed"]
        game.num_manuals = result["_Game__num_manuals"]
        return game

    def get_platforms(self):
        platforms = self.__db.platforms
        cursor = platforms.find()
        out_platforms = []
        for p in cursor:
            platform = self.__map_mongo_result_to_platform(p)
            out_platforms.append(platform)
        return out_platforms

    def __map_mongo_result_to_platform(self, p):
        platform = Platform()
        platform.id = p["_id"]
        platform.name = p["_Platform__name"]
        platform.description = p["_Platform__description"]
        return platform

    def add_platform(self, platform):
        platforms = self.__db.platforms
        platforms.insert(platform.__dict__)
from Game import Game
from Persistence.Exceptions.GameNotFoundException import GameNotFoundException


class ResultToGameMapper(object):

    def map(self, mongo_result):
        if mongo_result is None:
            raise GameNotFoundException
        game = Game()
        game.id = mongo_result["_id"]
        game.title = mongo_result["_Game__title"]
        game.platform = mongo_result["_Game__platform"]
        game.num_copies = mongo_result["_Game__num_copies"]
        game.num_boxed = mongo_result["_Game__num_boxed"]
        game.num_manuals = mongo_result["_Game__num_manuals"]
        game = self.__map_games_notes(game, mongo_result)
        game = self.__map_game_date_purhcased(game, mongo_result)
        game.approximate_date_purchased = mongo_result.get("_Game__approximate_date_purchased", False)
        return game

    def __map_games_notes(self, game, mongo_result):
        notes_key = "_Game__notes"
        if notes_key in mongo_result:
            game.notes = mongo_result[notes_key]
        return game

    def __map_game_date_purhcased(self, game, mongo_result):
        date_purchased_key = "_Game__date_purchased"
        if date_purchased_key in mongo_result:
            game.date_purchased = mongo_result[date_purchased_key]
        return game
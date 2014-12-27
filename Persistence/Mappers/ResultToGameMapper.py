from Game import Game


class ResultToGameMapper(object):

    def map(self, mongo_result):
        game = Game()
        game.id = mongo_result["_id"]
        game.title = mongo_result["_Game__title"]
        game.platform = mongo_result["_Game__platform"]
        game.num_copies = mongo_result["_Game__num_copies"]
        game.num_boxed = mongo_result["_Game__num_boxed"]
        game.num_manuals = mongo_result["_Game__num_manuals"]

        if "_Game__notes" in mongo_result:
            game.notes = mongo_result["_Game__notes"]

        return game
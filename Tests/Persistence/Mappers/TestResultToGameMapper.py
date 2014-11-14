import unittest
from Game import Game
from Persistence.Mappers.ResultToGameMapper import ResultToGameMapper


class TestResultToGameMapper(unittest.TestCase):
    def test_map_returns_game(self):
        mongo_result = {"_id": "id", "_Game__title": "title", "_Game__platform": "platform", "_Game__num_copies": "0",
                        "_Game__num_boxed": "0", "_Game__num_manuals": "0"}
        target = ResultToGameMapper()
        game = target.map(mongo_result)
        self.assertIsInstance(game, Game)


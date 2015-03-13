import unittest
from Game import Game
from Persistence.Mappers.ResultToGameMapper import ResultToGameMapper


class TestResultToGameMapper(unittest.TestCase):

    def setUp(self):
        self.__target = ResultToGameMapper()
        self.__mongo_result = {"_id": "id", "_Game__title": "title", "_Game__platform": "platform",
                               "_Game__num_copies": "0", "_Game__num_boxed": "0", "_Game__num_manuals": "0"}

    def test_map_returns_game(self):
        game = self.__target.map(self.__mongo_result)
        self.assertIsInstance(game, Game)

    def test_map_maps_notes(self):
        notes = "my notes"
        self.__mongo_result["_Game__notes"] = notes
        game = self.__target.map(self.__mongo_result)
        self.assertEqual(notes, game.notes)

    def test_map_date_purchased(self):
        date_purchased = "1/1/1990"
        self.__mongo_result["_Game__date_purchased"] = date_purchased
        game = self.__target.map(self.__mongo_result)
        self.assertEqual(date_purchased, game.date_purchased)

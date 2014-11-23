import unittest
from unittest.mock import Mock
from Game import Game
from Interactors.AddGameInteractor import AddGameInteractor
from Persistence.MongoPersistence import MongoPersistence


class AddGameValueTest(unittest.TestCase):

    def setUp(self):
        self.__persistence = Mock(MongoPersistence)
        self.target = AddGameInteractor()
        self.target.persistence = self.__persistence

    def get_game(self, game_id="", title="", platform="", num_copies=0, num_boxed=0, num_manuals=0):
        game = Game()
        game.id = game_id
        game.title = title
        game.platform = platform
        game.num_copies = num_copies
        game.num_boxed = num_boxed
        game.num_manuals = num_manuals
        return game
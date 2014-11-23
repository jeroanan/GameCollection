import unittest
from unittest.mock import Mock

from Game import Game
from Interactors.Interactor import Interactor
from Interactors.AddGameInteractor import AddGameInteractor
from Persistence.MongoPersistence import MongoPersistence


class TestAddGameInteractor(unittest.TestCase):

    def setUp(self):
        self.__persistence = Mock(MongoPersistence)
        self.__target = AddGameInteractor()
        self.__target.persistence = self.__persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        game = self.__get_game(title="Title", platform="Platform")
        self.__target.execute(game)
        self.assertTrue(self.__persistence.add_game.called)

    def test_execute_with_null_game_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def __get_game(self, game_id="", title="", platform="", num_copies=0, num_boxed=0):
        game = Game()
        game.id = game_id
        game.title = title
        game.platform = platform
        game.num_copies = num_copies
        game.num_boxed = num_boxed
        return game
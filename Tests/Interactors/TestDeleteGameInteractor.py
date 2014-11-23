import unittest
from unittest.mock import Mock

from Game import Game
from Interactors.DeleteGameInteractor import DeleteGameInteractor
from Interactors.Interactor import Interactor
from Persistence.MongoPersistence import MongoPersistence


class TestDeleteGameInteractor(unittest.TestCase):

    def setUp(self):
        self.__persistence = Mock(MongoPersistence)
        self.__target = DeleteGameInteractor()
        self.__target.persistence = self.__persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        game = self.__get_game("1337")
        self.__target.execute(game)
        self.assertTrue(self.__persistence.delete_game.called)

    def test_execute_with_none_game_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_with_none_id_raises_value_error(self):
        self.__assert_invalid_game_id(None)

    def test_execute_with_empty_id_raises_value_error(self):
        self.__assert_invalid_game_id("")

    def test_execute_with_whitespace_id_raises_value_error(self):
        self.__assert_invalid_game_id(" ")

    def __assert_invalid_game_id(self, game_id):
        game = self.__get_game(game_id)
        self.assertRaises(ValueError, self.__target.execute, game)

    def __get_game(self, game_id):
        game = Game()
        game.id = game_id
        return game

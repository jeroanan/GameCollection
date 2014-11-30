import unittest
from unittest.mock import Mock
from Game import Game
from Interactors.Interactor import Interactor
from Interactors.UpdateGameInteractor import UpdateGameInteractor
from Persistence.MongoPersistence import MongoPersistence


class TestUpdateGameInteractor(unittest.TestCase):

    def setUp(self):
        self.__target = UpdateGameInteractor()
        self.__persistence = Mock(MongoPersistence)
        self.__target.persistence = self.__persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        self.__target.execute(self.__get_game())
        self.assertTrue(self.__persistence.update_game.called)

    def test_execute_with_null_game_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_with_none_game_title_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_game(title=None))

    def test_execute_with_empty_game_title_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_game(title=""))

    def test_execute_with_whitespace_game_title_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_game(title=" "))

    def test_execute_with_none_platform_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_game(platform=None))

    def test_execute_with_empty_platform_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_game(platform=""))

    def test_execute_with_whitespace_platform_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_game(platform=" "))

    def test_execute_with_none_num_copies_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_game(num_copies=None))

    def test_execute_with_string_num_copies_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_game(num_copies="wrong"))

    def test_execute_with_none_num_boxed_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_game(num_boxed=None))

    def test_execute_with_string_num_boxed_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_game(num_boxed="wrong"))

    def test_execute_with_none_num_manuals_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_game(num_manuals=None))

    def test_execute_with_string_num_manuals_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_game(num_manuals="wrong"))

    def __get_game(self, title="title", platform="platform", num_copies=0, num_boxed=0, num_manuals=0):
        game = Game()
        game.title = title
        game.platform = platform
        game.num_copies = num_copies
        game.num_boxed = num_boxed
        game.num_manuals = num_manuals
        return game
import unittest
from unittest.mock import Mock
from Interactors.GetGameInteractor import GetGameInteractor
from Interactors.Interactor import Interactor
from Persistence.MongoPersistence import MongoPersistence


class TestGetGameInteractor(unittest.TestCase):

    def setUp(self):
        self.__target = GetGameInteractor()
        self.__persistence = Mock(MongoPersistence)
        self.__target.persistence = self.__persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_with_none_game_id_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_calls_persistence(self):
        self.__target.execute(game_id="gameid")
        self.__persistence.get_game.assert_called_with("gameid")
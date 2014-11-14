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
        self.__target.execute(game=Game())
        self.assertTrue(self.__persistence.update_game.called)
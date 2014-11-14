import unittest
from unittest.mock import Mock
from Game import Game
from Interactors.Interactor import Interactor
from Persistence.MongoPersistence import MongoPersistence
from Tests.Interactors.DeleteGameInteractor import DeleteGameInteractor


class TestDeleteGameInteractor(unittest.TestCase):

    def setUp(self):
        self.__persistence = Mock(MongoPersistence)
        self.__target = DeleteGameInteractor()
        self.__target.persistence = self.__persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute(self):
        self.__target.execute(Game())

    def test_execute_calls_persistence_method(self):
        self.__target.execute(Game())
        self.assertTrue(self.__persistence.delete_game.called)

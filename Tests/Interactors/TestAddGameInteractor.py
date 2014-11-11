import unittest

from mock import Mock

from Game import Game
from GamesGateway import GamesGateway
from Interactors.Interactor import Interactor
from Interactors.AddGameInteractor import AddGameInteractor


class TestAddGameInteractor(unittest.TestCase):

    def setUp(self):
        self.__target = AddGameInteractor()
        self.__gateway = Mock(GamesGateway)
        self.__target.games_gateway = self.__gateway

    def test_execute_calls_gateway(self):
        self.__target.execute(Game())
        self.assertTrue(self.__gateway.add_game.called)

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

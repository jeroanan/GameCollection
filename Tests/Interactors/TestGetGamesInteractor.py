import unittest
from unittest.mock import Mock

from GamesGateway import GamesGateway
from Interactors.GetGamesInteractor import GetGamesInteractor
from Interactors.Interactor import Interactor



class TestGetGamesInteractor(unittest.TestCase):

    def setUp(self):
        self.__target = GetGamesInteractor()
        self.__gateway = Mock(GamesGateway)
        self.__target.games_gateway = self.__gateway

    def test_execute_calls_gateway(self):
        self.__target.execute()
        self.assertTrue(self.__gateway.get_all_games.called)

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

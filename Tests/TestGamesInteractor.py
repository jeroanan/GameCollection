import unittest
from unittest.mock import Mock
from GamesGateway import GamesGateway
from GetGamesInteractor import GetGamesInteractor


class TestGamesInteractor(unittest.TestCase):

    def setUp(self):
        self.__target = GetGamesInteractor()
        self.__gateway = Mock(GamesGateway)
        self.__target.games_gateway = self.__gateway

    def test_get_my_games_calls_gateway(self):
        self.__target.execute()
        self.assertTrue(self.__gateway.get_all_games.called)

    def test_set_games_gateway(self):
        self.__target.games_gateway = GamesGateway()
        self.assertIsInstance(self.__target.games_gateway, GamesGateway)
import unittest
from GamesGateway import GamesGateway
from GetGamesInteractor import GetGamesInteractor
from Interactors.AddGameInteractor import AddGameInteractor
from Tests.Interactors.Exceptions.UnrecognisedInteractorTypeException import UnrecognisedInteractorTypeException
from Tests.Interactors.InteractorFactory import InteractorFactory


class TestInteractorFactory(unittest.TestCase):

    def setUp(self):
        self.__target = InteractorFactory()

    def test_create_unrecognised_type_string_throws_exception(self):
        self.assertRaises(UnrecognisedInteractorTypeException, self.__target.create, "InteractorType")

    def test_create_add_game_interactor_returns_add_game_interactor(self):
        self.assert_factory_returns_instance_of("AddGameInteractor", AddGameInteractor)

    def test_create_add_game_interactor_sets_gateway(self):
        result = self.__target.create("AddGameInteractor")
        self.assertIsInstance(result.games_gateway, GamesGateway)

    def test_create_get_games_interactor_returns_get_games_interactor(self):
        self.assert_factory_returns_instance_of("GetGamesInteractor", GetGamesInteractor)

    def test_create_get_games_interactor_sets_gateway(self):
        result = self.__target.create("GetGamesInteractor")
        self.assertIsInstance(result.games_gateway, GamesGateway)

    def assert_factory_returns_instance_of(self, type_string, interactor_type):
        result = self.__target.create(type_string)
        self.assertIsInstance(result, interactor_type)
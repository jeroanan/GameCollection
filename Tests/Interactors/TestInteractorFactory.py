import unittest
from unittest.mock import Mock

from Interactors.AddGameInteractor import AddGameInteractor
from Interactors.Exceptions.UnrecognisedInteractorTypeException import UnrecognisedInteractorTypeException
from Interactors.GetGamesInteractor import GetGamesInteractor
from Interactors.InteractorFactory import InteractorFactory
from Persistence.MongoPersistence import MongoPersistence
from Tests.Interactors.TestAddPlatformInteractor import AddPlatformInteractor
from Tests.Interactors.TestGetPlatformsInteractor import GetPlatformsInteractor


class TestInteractorFactory(unittest.TestCase):

    def setUp(self):
        self.__target = InteractorFactory(Mock(MongoPersistence))

    def test_create_unrecognised_type_string_throws_exception(self):
        self.assertRaises(UnrecognisedInteractorTypeException, self.__target.create, "InteractorType")

    def test_create_add_game_interactor_returns_add_game_interactor(self):
        self.assert_factory_returns_instance_of("AddGameInteractor", AddGameInteractor)

    def test_create_get_games_interactor_returns_get_games_interactor(self):
        self.assert_factory_returns_instance_of("GetGamesInteractor", GetGamesInteractor)

    def test_create_get_platforms_interactor_returns_get_platforms_interactor(self):
        self.assert_factory_returns_instance_of("GetPlatformsInteractor", GetPlatformsInteractor)

    def test_create_add_platform_interactor_returns_add_platform_interactor(self):
        self.assert_factory_returns_instance_of("AddPlatformInteractor", AddPlatformInteractor)

    def assert_factory_returns_instance_of(self, type_string, interactor_type):
        result = self.__target.create(type_string)
        self.assertIsInstance(result, interactor_type)
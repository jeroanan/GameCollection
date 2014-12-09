import unittest
from unittest.mock import Mock
from Interactors.DeleteHardwareInteractor import DeleteHardwareInteractor
from Interactors.DeletePlatformInteractor import DeletePlatformInteractor
from Interactors.GetHardwareInteractor import GetHardwareDetailsInteractor

from Interactors.GetHardwareListInteractor import GetHardwareListInteractor
from Interactors.AddGameInteractor import AddGameInteractor
from Interactors.DeleteGameInteractor import DeleteGameInteractor
from Interactors.Exceptions.UnrecognisedInteractorTypeException import UnrecognisedInteractorTypeException
from Interactors.GetGameInteractor import GetGameInteractor
from Interactors.GetGamesInteractor import GetGamesInteractor
from Interactors.GetPlatformInteractor import GetPlatformInteractor
from Interactors.GetSuggestedPlatformsInteractor import GetSuggestedPlatformsInteractor
from Interactors.InteractorFactory import InteractorFactory
from Interactors.SaveHardwareInteractor import SaveHardwareInteractor
from Interactors.UpdateGameInteractor import UpdateGameInteractor
from Interactors.UpdateHardwareInteractor import UpdateHardwareInteractor
from Persistence.MongoPersistence import MongoPersistence
from Tests.Interactors.TestAddPlatformInteractor import AddPlatformInteractor
from Tests.Interactors.TestGetPlatformsInteractor import GetPlatformsInteractor
from Tests.Interactors.TestUpdatePlatformInteractor import UpdatePlatformInteractor


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

    def test_create_get_game_interactor_returns_get_game_interactor(self):
        self.assert_factory_returns_instance_of("GetGameInteractor", GetGameInteractor)

    def test_create_update_game_interactor_returns_update_game_interactor(self):
        self.assert_factory_returns_instance_of("UpdateGameInteractor", UpdateGameInteractor)

    def test_create_delete_game_interactor_returns_delete_game_interactor(self):
        self.assert_factory_returns_instance_of("DeleteGameInteractor", DeleteGameInteractor)

    def test_create_get_hardware_list_interactor_returns_get_hardware_list_interactor(self):
        self.assert_factory_returns_instance_of("GetHardwareListInteractor", GetHardwareListInteractor)

    def test_create_save_hardware_interactor_returns_save_hardware_interactor(self):
        self.assert_factory_returns_instance_of("SaveHardwareInteractor", SaveHardwareInteractor)

    def test_create_get_platform_interactor_returns_get_platform_interactor(self):
        self.assert_factory_returns_instance_of("GetPlatformInteractor", GetPlatformInteractor)

    def test_create_update_platform_interactor_returns_update_platform_interactor(self):
        self.assert_factory_returns_instance_of("UpdatePlatformInteractor", UpdatePlatformInteractor)

    def test_create_delete_platform_interactor_returns_delete_platform_interactor(self):
        self.assert_factory_returns_instance_of("DeletePlatformInteractor", DeletePlatformInteractor)

    def test_create_get_hardware_details_interactor_returns_get_hardware_details_interactor(self):
        self.assert_factory_returns_instance_of("GetHardwareDetailsInteractor", GetHardwareDetailsInteractor)

    def test_create_update_hardware_interactor_returns_update_hardware_interactor(self):
        self.assert_factory_returns_instance_of("UpdateHardwareInteractor", UpdateHardwareInteractor)

    def test_create_delete_hardware_interactor_returns_delete_hardware_interactor(self):
        self.assert_factory_returns_instance_of("DeleteHardwareInteractor", DeleteHardwareInteractor)

    def test_create_get_suggested_platforms_interactor_returns_get_suggested_platforms_interactor(self):
        self.assert_factory_returns_instance_of("GetSuggestedPlatformsInteractor", GetSuggestedPlatformsInteractor)

    def assert_factory_returns_instance_of(self, type_string, interactor_type):
        result = self.__target.create(type_string)
        self.assertIsInstance(result, interactor_type)
import unittest
from unittest.mock import Mock

from Interactors.Genre.AddGenreInteractor import AddGenreInteractor
from Interactors.Game.CountGamesInteractor import CountGamesInteractor
from Interactors.Hardware.CountHardwareInteractor import CountHardwareInteractor
from Interactors.Hardware.DeleteHardwareInteractor import DeleteHardwareInteractor
from Interactors.Platform.DeletePlatformInteractor import DeletePlatformInteractor
from Interactors.Genre.GetGenreInteractor import GetGenreInteractor
from Interactors.Genre.GetGenresInteractor import GetGenresInteractor
from Interactors.Hardware.GetHardwareInteractor import GetHardwareDetailsInteractor
from Interactors.Hardware.GetHardwareListInteractor import GetHardwareListInteractor
from Interactors.Game.AddGameInteractor import AddGameInteractor
from Interactors.Game.DeleteGameInteractor import DeleteGameInteractor
from Interactors.Exceptions.UnrecognisedInteractorTypeException import UnrecognisedInteractorTypeException
from Interactors.Game.GetGameInteractor import GetGameInteractor
from Interactors.Game.GetGamesInteractor import GetGamesInteractor
from Interactors.Platform.GetPlatformInteractor import GetPlatformInteractor
from Interactors.Platform.GetSuggestedPlatformsInteractor import GetSuggestedPlatformsInteractor
from Interactors.InteractorFactory import InteractorFactory
from Interactors.Hardware.SaveHardwareInteractor import SaveHardwareInteractor
from Interactors.SearchInteractor import SearchInteractor
from Interactors.Game.UpdateGameInteractor import UpdateGameInteractor
from Interactors.Hardware.UpdateHardwareInteractor import UpdateHardwareInteractor
from Persistence.MongoPersistence import MongoPersistence
from Interactors.User.LoginInteractor import LoginInteractor
from Interactors.Platform.AddPlatformInteractor import AddPlatformInteractor
from Tests.Interactors.TestDeleteGenreInteractor import DeleteGenreInteractor
from Tests.Interactors.TestGetPlatformsInteractor import GetPlatformsInteractor
from Tests.Interactors.TestUpdatePlatformInteractor import UpdatePlatformInteractor
from Interactors.Genre.UpdateGenreInteractor import UpdateGenreInteractor


class TestInteractorFactory(unittest.TestCase):

    def setUp(self):
        self.__target = InteractorFactory(Mock(MongoPersistence))

    def test_create_unrecognised_type_string_throws_exception(self):
        self.assertRaises(UnrecognisedInteractorTypeException, self.__target.create, "InteractorType")

    def test_create_add_game_interactor_returns_add_game_interactor(self):
        self.__assert_factory_returns_instance_of("AddGameInteractor", AddGameInteractor)

    def test_create_get_games_interactor_returns_get_games_interactor(self):
        self.__assert_factory_returns_instance_of("GetGamesInteractor", GetGamesInteractor)

    def test_create_get_platforms_interactor_returns_get_platforms_interactor(self):
        self.__assert_factory_returns_instance_of("GetPlatformsInteractor", GetPlatformsInteractor)

    def test_create_add_platform_interactor_returns_add_platform_interactor(self):
        self.__assert_factory_returns_instance_of("AddPlatformInteractor", AddPlatformInteractor)

    def test_create_get_game_interactor_returns_get_game_interactor(self):
        self.__assert_factory_returns_instance_of("GetGameInteractor", GetGameInteractor)

    def test_create_update_game_interactor_returns_update_game_interactor(self):
        self.__assert_factory_returns_instance_of("UpdateGameInteractor", UpdateGameInteractor)

    def test_create_delete_game_interactor_returns_delete_game_interactor(self):
        self.__assert_factory_returns_instance_of("DeleteGameInteractor", DeleteGameInteractor)

    def test_create_get_hardware_list_interactor_returns_get_hardware_list_interactor(self):
        self.__assert_factory_returns_instance_of("GetHardwareListInteractor", GetHardwareListInteractor)

    def test_create_save_hardware_interactor_returns_save_hardware_interactor(self):
        self.__assert_factory_returns_instance_of("SaveHardwareInteractor", SaveHardwareInteractor)

    def test_create_get_platform_interactor_returns_get_platform_interactor(self):
        self.__assert_factory_returns_instance_of("GetPlatformInteractor", GetPlatformInteractor)

    def test_create_update_platform_interactor_returns_update_platform_interactor(self):
        self.__assert_factory_returns_instance_of("UpdatePlatformInteractor", UpdatePlatformInteractor)

    def test_create_delete_platform_interactor_returns_delete_platform_interactor(self):
        self.__assert_factory_returns_instance_of("DeletePlatformInteractor", DeletePlatformInteractor)

    def test_create_get_hardware_details_interactor_returns_get_hardware_details_interactor(self):
        self.__assert_factory_returns_instance_of("GetHardwareDetailsInteractor", GetHardwareDetailsInteractor)

    def test_create_update_hardware_interactor_returns_update_hardware_interactor(self):
        self.__assert_factory_returns_instance_of("UpdateHardwareInteractor", UpdateHardwareInteractor)

    def test_create_delete_hardware_interactor_returns_delete_hardware_interactor(self):
        self.__assert_factory_returns_instance_of("DeleteHardwareInteractor", DeleteHardwareInteractor)

    def test_create_get_suggested_platforms_interactor_returns_get_suggested_platforms_interactor(self):
        self.__assert_factory_returns_instance_of("GetSuggestedPlatformsInteractor", GetSuggestedPlatformsInteractor)

    def test_create_get_genres_interactor_returns_get_genres_interactor(self):
        self.__assert_factory_returns_instance_of("GetGenresInteractor", GetGenresInteractor)

    def test_create_add_genre_interactor_returns_add_genre_interactor(self):
        self.__assert_factory_returns_instance_of("AddGenreInteractor", AddGenreInteractor)

    def test_create_get_genre_interactor_returns_get_genre_interactor(self):
        self.__assert_factory_returns_instance_of("GetGenreInteractor", GetGenreInteractor)

    def test_create_update_genre_interactor_returns_update_genre_interactor(self):
        self.__assert_factory_returns_instance_of("UpdateGenreInteractor", UpdateGenreInteractor)

    def test_create_delete_genre_interactor_returns_delete_genre_interactor(self):
        self.__assert_factory_returns_instance_of("DeleteGenreInteractor", DeleteGenreInteractor)

    def test_create_count_games_interactor_returns_count_games_interactor(self):
        self.__assert_factory_returns_instance_of("CountGamesInteractor", CountGamesInteractor)

    def test_create_search_interactor_returns_search_interactor(self):
        self.__assert_factory_returns_instance_of("SearchInteractor", SearchInteractor)

    def test_create_count_hardware_interactor_returns_count_hardware_interactor(self):
        self.__assert_factory_returns_instance_of("CountHardwareInteractor", CountHardwareInteractor)

    def test_create_login_interactor_returns_login_interactor(self):
        self.__assert_factory_returns_instance_of("LoginInteractor", LoginInteractor)

    def __assert_factory_returns_instance_of(self, type_string, interactor_type):
        result = self.__target.create(type_string)
        self.assertIsInstance(result, interactor_type)
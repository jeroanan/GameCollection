import unittest
from unittest.mock import Mock

from Data.Config import Config
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.AddGameHandler import AddGameHandler
from UI.Handlers.AddHardwareHandler import AddHardwareHandler
from UI.Handlers.AddPlatformHandler.AddPlatformHandler import AddPlatformHandler
from UI.Handlers.AllGamesHandler.AllGamesHandler import AllGamesHandler
from UI.Handlers.AllHardwareHandler import AllHardwareHandler
from UI.Handlers.DeleteGameHandler import DeleteGameHandler
from UI.Handlers.DeleteHardwareHandler import DeleteHardwareHandler
from UI.Handlers.DeletePlatformHandler import DeletePlatformHandler
from UI.Handlers.EditGameHandler import EditGameHandler
from UI.Handlers.EditHardwareHandler import EditHardwareHandler
from UI.Handlers.Exceptions.UnrecognisedHandlerException import UnrecognisedHandlerException
from UI.Handlers.HandlerFactory import HandlerFactory
from UI.Handlers.IndexHandler.IndexHandler import IndexHandler
from UI.Handlers.PlatformsHandler import PlatformsHandler
from UI.Handlers.SaveGameHandler.SaveGameHandler import SaveGameHandler
from UI.Handlers.SaveHardwareHandler.SaveHardwareHandler import SaveHardwareHandler
from UI.Handlers.SearchHandler.SearchHandler import SearchHandler
from UI.Handlers.SortGamesHandler import SortGamesHandler
from UI.Handlers.UpdateGameHandler.UpdateGameHandler import UpdateGameHandler
from UI.Handlers.UpdateHardwareHandler.UpdateHardwareHandler import UpdateHardwareHandler
from UI.Handlers.UpdatePlatformHandler.UpdatePlatformHandler import UpdatePlatformHandler
from UI.TemplateRenderer import TemplateRenderer
from UI.Tests.Handlers.TestEditPlatformHandler import EditPlatformHandler


class TestHandlerFactory(unittest.TestCase):

    def setUp(self):
        interactor_factory = Mock(InteractorFactory)
        renderer = Mock(TemplateRenderer)
        config = Mock(Config)
        self.__target = HandlerFactory(interactor_factory, renderer, config)

    def test_create_with_unrecognised_type_string_throws_unrecognised_handler_exception(self):
        self.assertRaises(UnrecognisedHandlerException, self.__target.create, "UnrecognisedHandlerType")

    def test_create_index_handler_returns_index_handler(self):
        self.__assert_type_string_returns_handler_type("index", IndexHandler)

    def test_create_save_game_handler_returns_save_game_handler(self):
        self.__assert_type_string_returns_handler_type("savegame", SaveGameHandler)

    def test_create_add_game_handler_returns_add_game_handler(self):
        self.__assert_type_string_returns_handler_type("addgame", AddGameHandler)

    def test_add_hardware_handler_returns_add_hardware_handler(self):
        self.__assert_type_string_returns_handler_type("addhardware", AddHardwareHandler)

    def test_platforms_handler_returns_platforms_handler(self):
        self.__assert_type_string_returns_handler_type("platforms", PlatformsHandler)

    def test_add_platform_handler_returns_add_platform_handler(self):
        self.__assert_type_string_returns_handler_type("addplatform", AddPlatformHandler)

    def test_edit_handler_returns_edit_handler(self):
        self.__assert_type_string_returns_handler_type("editgame", EditGameHandler)

    def test_update_game_handler_returns_update_game_handler(self):
        self.__assert_type_string_returns_handler_type("updategame", UpdateGameHandler)

    def test_delete_game_handler_returns_delete_game_handler(self):
        self.__assert_type_string_returns_handler_type("deletegame", DeleteGameHandler)

    def test_save_hardware_handler_returns_save_hardware_handler(self):
        self.__assert_type_string_returns_handler_type("savehardware", SaveHardwareHandler)

    def test_edit_platform_handler_returns_edit_platform_handler(self):
        self.__assert_type_string_returns_handler_type("editplatform", EditPlatformHandler)

    def test_update_platform_handler_returns_update_platform_handler(self):
        self.__assert_type_string_returns_handler_type("updateplatform", UpdatePlatformHandler)

    def test_delete_platform_handler_returns_delete_platform_handler(self):
        self.__assert_type_string_returns_handler_type("deleteplatform", DeletePlatformHandler)

    def test_edit_hardware_handler_returns_edit_hardware_handler(self):
        self.__assert_type_string_returns_handler_type("edithardware", EditHardwareHandler)

    def test_update_hardware_handler_returns_update_hardware_handler(self):
        self.__assert_type_string_returns_handler_type("updatehardware", UpdateHardwareHandler)

    def test_delete_hardware_handler_returns_delete_hardware_handler(self):
        self.__assert_type_string_returns_handler_type("deletehardware", DeleteHardwareHandler)

    def test_allgames_handler_returns_allgames_handler(self):
        self.__assert_type_string_returns_handler_type("allgames", AllGamesHandler)

    def test_search_returns_search_handler(self):
        self.__assert_type_string_returns_handler_type("search", SearchHandler)

    def test_allhardware_returns_allhardware_handler(self):
        self.__assert_type_string_returns_handler_type("allhardware", AllHardwareHandler)

    def test_sortgames_returns_sortgames_handler(self):
        self.__assert_type_string_returns_handler_type("sortgames", SortGamesHandler)

    def __assert_type_string_returns_handler_type(self, type_string, handler_type):
        handler = self.__target.create(type_string)
        self.assertIsInstance(handler, handler_type)
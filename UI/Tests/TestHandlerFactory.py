import unittest
from unittest.mock import Mock
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.AddGameHandler import AddGameHandler
from UI.Handlers.AddHardwareHandler import AddHardwareHandler
from UI.Handlers.AddPlatformHandler import AddPlatformHandler
from UI.Handlers.Exceptions.UnrecognisedHandlerException import UnrecognisedHandlerException
from UI.Handlers.HandlerFactory import HandlerFactory
from UI.Handlers.IndexHandler import IndexHandler
from UI.Handlers.PlatformsHandler import PlatformsHandler
from UI.Handlers.SaveGameHandler import SaveGameHandler
from UI.TemplateRenderer import TemplateRenderer


class TestHandlerFactory(unittest.TestCase):

    def setUp(self):
        interactor_factory = Mock(InteractorFactory)
        renderer = Mock(TemplateRenderer)
        self.__target = HandlerFactory(interactor_factory, renderer)

    def test_create_with_unrecognised_type_string_throws_unrecognised_handler_exception(self):
        self.assertRaises(UnrecognisedHandlerException, self.__target.create, "UnrecognisedHandlerType")

    def test_create_index_handler_returns_index_handler(self):
        self.__assert_type_string_returns_handler_type("IndexHandler", IndexHandler)

    def test_create_save_game_handler_returns_save_game_handler(self):
        self.__assert_type_string_returns_handler_type("SaveGameHandler", SaveGameHandler)

    def test_create_add_game_handler_returns_add_game_handler(self):
        self.__assert_type_string_returns_handler_type("AddGameHandler", AddGameHandler)

    def test_add_hardware_handler_returns_add_hardware_handler(self):
        self.__assert_type_string_returns_handler_type("AddHardwareHandler", AddHardwareHandler)

    def test_platforms_handler_returns_platforms_handler(self):
        self.__assert_type_string_returns_handler_type("PlatformsHandler", PlatformsHandler)

    def test_add_platform_handler_returns_add_platform_handler(self):
        self.__assert_type_string_returns_handler_type("AddPlatformHandler", AddPlatformHandler)

    def __assert_type_string_returns_handler_type(self, type_string, handler_type):
        handler = self.__target.create(type_string)
        self.assertIsInstance(handler, handler_type)
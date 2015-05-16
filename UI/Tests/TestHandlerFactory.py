# This file is part of Icarus.

# Icarus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Icarus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Icarus.  If not, see <http://www.gnu.org/licenses/>

import unittest
from unittest.mock import Mock

from Data.Config import Config
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.AddGameHandler import AddGameHandler
from UI.Handlers.AddHardwareHandler import AddHardwareHandler
from UI.Handlers.AddPlatformHandler import AddPlatformHandler
from UI.Handlers.AllGamesHandler import AllGamesHandler
from UI.Handlers.AllHardwareHandler import AllHardwareHandler
from UI.Handlers.DeleteGameHandler import DeleteGameHandler
from UI.Handlers.DeleteHardwareHandler import DeleteHardwareHandler
from UI.Handlers.DeletePlatformHandler import DeletePlatformHandler
from UI.Handlers.EditGameHandler import EditGameHandler
from UI.Handlers.EditHardwareHandler import EditHardwareHandler
from UI.Handlers.Exceptions.UnrecognisedHandlerException import UnrecognisedHandlerException
from UI.Handlers.GenresHandler import GenresHandler
from UI.Handlers.HandlerFactory import HandlerFactory
from UI.Handlers.IndexHandler import IndexHandler
from UI.Handlers.LoginHandler import LoginHandler
from UI.Handlers.LogoutHandler import LogoutHandler
from UI.Handlers.PlatformsHandler import PlatformsHandler
from UI.Handlers.SaveGameHandler import SaveGameHandler
from UI.Handlers.SaveHardwareHandler import SaveHardwareHandler
from UI.Handlers.SearchHandler import SearchHandler
from UI.Handlers.SignupHandler import SignupHandler
from UI.Handlers.SigninHandler import SigninHandler
from UI.Handlers.SortGamesHandler import SortGamesHandler
from UI.Handlers.SortHardwareHandler import SortHardwareHandler
from UI.Handlers.UpdateGameHandler import UpdateGameHandler
from UI.Handlers.UpdateHardwareHandler import UpdateHardwareHandler
from UI.Handlers.UpdatePlatformHandler import UpdatePlatformHandler
from UI.Handlers.Session.Session import Session
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

    def test_handler_creation(self):
        mappings = {"index": IndexHandler,
                    "savegame": SaveGameHandler,
                    "addgame": AddGameHandler,
                    "addhardware": AddHardwareHandler,
                    "platforms": PlatformsHandler,
                    "addplatform": AddPlatformHandler,
                    "editgame": EditGameHandler,
                    "updategame": UpdateGameHandler,
                    "deletegame": DeleteGameHandler,
                    "savehardware": SaveHardwareHandler,
                    "editplatform": EditPlatformHandler,
                    "updateplatform": UpdatePlatformHandler,
                    "deleteplatform": DeletePlatformHandler,
                    "edithardware": EditHardwareHandler,
                    "updatehardware": UpdateHardwareHandler,
                    "deletehardware": DeleteHardwareHandler,
                    "allgames": AllGamesHandler,
                    "search": SearchHandler,
                    "allhardware": AllHardwareHandler,
                    "sortgames": SortGamesHandler,
                    "sorthardware": SortHardwareHandler,
                    "login": LoginHandler,
                    "signup": SignupHandler,
                    "signin": SigninHandler,
                    "logout": LogoutHandler,
                    "genres": GenresHandler}

        for m in mappings:
            self.__assert_type_string_returns_handler_type(m, mappings[m])

    def __assert_type_string_returns_handler_type(self, type_string, handler_type):
        handler = self.__target.create(type_string)
        self.assertIsInstance(handler, handler_type, type_string)

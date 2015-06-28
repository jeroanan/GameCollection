# Copyright (c) David Wilson 2015x
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
from UI.Handlers.AddGenreHandler import AddGenreHandler
from UI.Handlers.AddHardwareHandler import AddHardwareHandler
from UI.Handlers.AddHardwareTypeHandler import AddHardwareTypeHandler
from UI.Handlers.AddPlatformHandler import AddPlatformHandler
from UI.Handlers.AllGamesHandler import AllGamesHandler
from UI.Handlers.AllHardwareHandler import AllHardwareHandler
from UI.Handlers.DeleteGameHandler import DeleteGameHandler
from UI.Handlers.DeleteGenreHandler import DeleteGenreHandler
from UI.Handlers.DeleteHardwareHandler import DeleteHardwareHandler
from UI.Handlers.DeletePlatformHandler import DeletePlatformHandler
from UI.Handlers.DeleteUserHandler import DeleteUserHandler
from UI.Handlers.EditGameHandler import EditGameHandler
from UI.Handlers.EditGenreHandler import EditGenreHandler
from UI.Handlers.EditHardwareHandler import EditHardwareHandler
from UI.Handlers.EditHardwareTypeHandler import EditHardwareTypeHandler
from UI.Handlers.EditPlatformHandler import EditPlatformHandler
from UI.Handlers.EditUserHandler import EditUserHandler
from UI.Handlers.Exceptions.UnrecognisedHandlerException import UnrecognisedHandlerException
from UI.Handlers.GenresHandler import GenresHandler
from UI.Handlers.HandlerFactory import HandlerFactory
from UI.Handlers.HardwareTypesHandler import HardwareTypesHandler
from UI.Handlers.IndexHandler import IndexHandler
from UI.Handlers.LoginHandler import LoginHandler
from UI.Handlers.LogoutHandler import LogoutHandler
from UI.Handlers.PlatformsHandler import PlatformsHandler
from UI.Handlers.SaveGameHandler import SaveGameHandler
from UI.Handlers.SaveHardwareHandler import SaveHardwareHandler
from UI.Handlers.SearchHandler import SearchHandler
from UI.Handlers.Session.Session import Session
from UI.Handlers.SigninHandler import SigninHandler
from UI.Handlers.SignupHandler import SignupHandler
from UI.Handlers.SortGamesHandler import SortGamesHandler
from UI.Handlers.SortHardwareHandler import SortHardwareHandler
from UI.Handlers.UpdateGameHandler import UpdateGameHandler
from UI.Handlers.UpdateGenreHandler import UpdateGenreHandler
from UI.Handlers.UpdateHardwareHandler import UpdateHardwareHandler
from UI.Handlers.UpdateHardwareTypeHandler import UpdateHardwareTypeHandler
from UI.Handlers.UpdatePlatformHandler import UpdatePlatformHandler
from UI.Handlers.UpdateUserHandler import UpdateUserHandler
from UI.Handlers.UsersHandler import UsersHandler
from UI.TemplateRenderer import TemplateRenderer


class TestHandlerFactory(unittest.TestCase):
    """Unit tests for the HandlerFactory class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        interactor_factory = Mock(InteractorFactory)
        renderer = Mock(TemplateRenderer)
        config = Mock(Config)
        self.__target = HandlerFactory(interactor_factory, renderer, config)

    def test_create_with_unrecognised_type_string_throws_unrecognised_handler_exception(self):
        """Calling HandlerFactory.Create with an unrecognised handler type raises UnrecognisedHandlerException."""
        self.assertRaises(UnrecognisedHandlerException, self.__target.create, "UnrecognisedHandlerType")

    def test_handler_creation(self):
        """Calling HandlerFactory.Create with a recgonised handler type creates the correct ttype of Handler."""
        mappings = {
            "addgame": AddGameHandler,            
            "addgenre": AddGenreHandler,
            "addhardware": AddHardwareHandler,
            "addhardwaretype": AddHardwareTypeHandler,
            "addplatform": AddPlatformHandler,
            "allgames": AllGamesHandler,
            "allhardware": AllHardwareHandler,
            "deletegame": DeleteGameHandler,
            "deletegenre": DeleteGenreHandler,
            "deletehardware": DeleteHardwareHandler,
            "deleteplatform": DeletePlatformHandler,
            "deleteuser": DeleteUserHandler,
            "editgame": EditGameHandler,
            "editgenre": EditGenreHandler,            
            "edithardware": EditHardwareHandler,
            "edithardwaretype": EditHardwareTypeHandler,
            "editplatform": EditPlatformHandler,
            "edituser": EditUserHandler,
            "genres": GenresHandler,
            "hardwaretypes": HardwareTypesHandler,
            "index": IndexHandler,
            "login": LoginHandler,
            "logout": LogoutHandler,
            "platforms": PlatformsHandler,
            "savegame": SaveGameHandler,
            "savehardware": SaveHardwareHandler,
            "search": SearchHandler,
            "signin": SigninHandler,
            "signup": SignupHandler,
            "sortgames": SortGamesHandler,
            "sorthardware": SortHardwareHandler,
            "updategame": UpdateGameHandler,
            "updategenre": UpdateGenreHandler,
            "updatehardware": UpdateHardwareHandler,
            "updatehardwaretype": UpdateHardwareTypeHandler,
            "updateplatform": UpdatePlatformHandler,
            "updateuser": UpdateUserHandler,
            "users": UsersHandler
        }

        list(map(lambda m: self.assertIsInstance(self.__target.create(m), mappings[m]), mappings))

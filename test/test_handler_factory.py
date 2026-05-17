"""Provides unit tests for the HandlerFactory class."""
# Copyright (c) David Wilson 2015, 2026
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

from data.config import Config
from interactors.interactor_factory import InteractorFactory
from ui.Handlers.AddGameHandler import AddGameHandler
from ui.Handlers.add_genre_handler import AddGenreHandler
from ui.Handlers.AddHardwareHandler import AddHardwareHandler
from ui.Handlers.AddHardwareTypeHandler import AddHardwareTypeHandler
from ui.Handlers.AddPlatformHandler import AddPlatformHandler
from ui.Handlers.AllGamesHandler import AllGamesHandler
from ui.Handlers.AllHardwareHandler import AllHardwareHandler
from ui.Handlers.delete_game_handler import DeleteGameHandler
from ui.Handlers.DeleteGenreHandler import DeleteGenreHandler
from ui.Handlers.DeleteHardwareHandler import DeleteHardwareHandler
from ui.Handlers.DeleteHardwareTypeHandler import DeleteHardwareTypeHandler
from ui.Handlers.DeletePlatformHandler import DeletePlatformHandler
from ui.Handlers.DeleteUserHandler import DeleteUserHandler
from ui.Handlers.edit_game_handler import EditGameHandler
from ui.Handlers.EditGenreHandler import EditGenreHandler
from ui.Handlers.edit_hardware_handler import EditHardwareHandler
from ui.Handlers.EditHardwareTypeHandler import EditHardwareTypeHandler
from ui.Handlers.EditPlatformHandler import EditPlatformHandler
from ui.Handlers.EditUserHandler import EditUserHandler
from ui.Handlers.Exceptions.UnrecognisedHandlerException import UnrecognisedHandlerException
import ui.Handlers.ExportCollectionHandler as ech
from ui.Handlers.genres_handler import GenresHandler
import ui.Handlers.GetExportHandler as geh
from ui.Handlers.handler_factory import HandlerFactory
from ui.Handlers.HardwareTypesHandler import HardwareTypesHandler
from ui.Handlers.index_handler import IndexHandler
from ui.Handlers.LoginHandler import LoginHandler
from ui.Handlers.LogoutHandler import LogoutHandler
from ui.Handlers.PlatformsHandler import PlatformsHandler
from ui.Handlers.SaveGameHandler import SaveGameHandler
from ui.Handlers.SaveHardwareHandler import SaveHardwareHandler
from ui.Handlers.SearchHandler import SearchHandler
from ui.Handlers.SigninHandler import SigninHandler
from ui.Handlers.SignupHandler import SignupHandler
from ui.Handlers.SortGamesHandler import SortGamesHandler
from ui.Handlers.SortHardwareHandler import SortHardwareHandler
from ui.Handlers.UpdateGameHandler import UpdateGameHandler
from ui.Handlers.UpdateGenreHandler import UpdateGenreHandler
from ui.Handlers.UpdateHardwareHandler import UpdateHardwareHandler
from ui.Handlers.UpdateHardwareTypeHandler import UpdateHardwareTypeHandler
from ui.Handlers.UpdatePlatformHandler import UpdatePlatformHandler
from ui.Handlers.UpdateUserHandler import UpdateUserHandler
from ui.Handlers.UsersHandler import UsersHandler
from ui.Handlers.ViewGameHandler import ViewGameHandler
from ui.template_renderer import TemplateRenderer


class TestHandlerFactory(unittest.TestCase):
    """Unit tests for the HandlerFactory class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        interactor_factory = Mock(InteractorFactory)
        renderer = Mock(TemplateRenderer)
        config = Mock(Config)
        self.__target = HandlerFactory(interactor_factory, renderer, config)

    def test_create_with_unrecognised_type_string_throws_unrecognised_handler_exception(self):
        """Calling HandlerFactory.Create with an unrecognised handler type raises
        UnrecognisedHandlerException."""
        self.assertRaises(
            UnrecognisedHandlerException,
            self.__target.create,
            "UnrecognisedHandlerType")

    def test_handler_creation(self):
        """Calling HandlerFactory.Create with a recgonised handler type creates the correct type of
        Handler."""
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
            "deletehardwaretype": DeleteHardwareTypeHandler,
            "deleteplatform": DeletePlatformHandler,
            "deleteuser": DeleteUserHandler,
            "editgame": EditGameHandler,
            "editgenre": EditGenreHandler,            
            "edithardware": EditHardwareHandler,
            "edithardwaretype": EditHardwareTypeHandler,
            "editplatform": EditPlatformHandler,
            "edituser": EditUserHandler,
            "exportcollection": ech.ExportCollectionHandler,
            "genres": GenresHandler,
            "getexportcollection": geh.GetExportHandler,
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
            "users": UsersHandler,
            "viewgame": ViewGameHandler
        }

        list(map(lambda m: self.assertIsInstance(self.__target.create(m), mappings[m]), mappings))

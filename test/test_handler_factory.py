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
from ui.Handlers.add_game_handler import AddGameHandler
from ui.Handlers.add_genre_handler import AddGenreHandler
from ui.Handlers.add_hardware_handler import AddHardwareHandler
from ui.Handlers.add_hardware_type_handler import AddHardwareTypeHandler
from ui.Handlers.add_platform_handler import AddPlatformHandler
from ui.Handlers.all_games_handler import AllGamesHandler
from ui.Handlers.all_hardware_handler import AllHardwareHandler
from ui.Handlers.delete_game_handler import DeleteGameHandler
from ui.Handlers.delete_genre_handler import DeleteGenreHandler
from ui.Handlers.delete_hardware_handler import DeleteHardwareHandler
from ui.Handlers.delete_hardware_type_handler import DeleteHardwareTypeHandler
from ui.Handlers.delete_platform_handler import DeletePlatformHandler
from ui.Handlers.delete_user_handler import DeleteUserHandler
from ui.Handlers.edit_game_handler import EditGameHandler
from ui.Handlers.edit_genre_handler import EditGenreHandler
from ui.Handlers.edit_hardware_handler import EditHardwareHandler
from ui.Handlers.edit_hardware_type_handler import EditHardwareTypeHandler
from ui.Handlers.edit_platform_handler import EditPlatformHandler
from ui.Handlers.edit_user_handler import EditUserHandler
from ui.Handlers.Exceptions.UnrecognisedHandlerException import UnrecognisedHandlerException
import ui.Handlers.export_collection_handler as ech
from ui.Handlers.genres_handler import GenresHandler
import ui.Handlers.get_export_handler as geh
from ui.Handlers.handler_factory import HandlerFactory
from ui.Handlers.hardware_types_handler import HardwareTypesHandler
from ui.Handlers.index_handler import IndexHandler
from ui.Handlers.login_handler import LoginHandler
from ui.Handlers.logout_handler import LogoutHandler
from ui.Handlers.platforms_handler import PlatformsHandler
from ui.Handlers.save_game_handler import SaveGameHandler
from ui.Handlers.save_hardware_handler import SaveHardwareHandler
from ui.Handlers.search_handler import SearchHandler
from ui.Handlers.signin_handler import SigninHandler
from ui.Handlers.signup_handler import SignupHandler
from ui.Handlers.sort_games_handler import SortGamesHandler
from ui.Handlers.sort_hardware_handler import SortHardwareHandler
from ui.Handlers.update_game_handler import UpdateGameHandler
from ui.Handlers.update_genre_handler import UpdateGenreHandler
from ui.Handlers.update_hardware_handler import UpdateHardwareHandler
from ui.Handlers.update_hardware_type_handler import UpdateHardwareTypeHandler
from ui.Handlers.update_platform_handler import UpdatePlatformHandler
from ui.Handlers.update_user_handler import UpdateUserHandler
from ui.Handlers.users_handler import UsersHandler
from ui.Handlers.view_game_handler import ViewGameHandler
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

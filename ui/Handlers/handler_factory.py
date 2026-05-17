"""Factory for creating handlers."""
# copyright (c) David Wilson 2015, 2026
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

import importlib
import json

from ui.Cookies.Cookies import Cookies
from ui.Handlers.Exceptions.UnrecognisedHandlerException import UnrecognisedHandlerException
from ui.Handlers.index_handler import IndexHandler
from ui.Handlers.Session.Session import Session

class HandlerFactory:
    """Factory for creating handlers."""

    def __init__(self, interactor_factory, renderer, config):
        self.__interactor_factory = interactor_factory
        self.__renderer = renderer
        self.__config = config
        self.__handlers = self.__load_handlers()

    def __load_handlers(self):
        with open("ui/Handlers/handlers.json", encoding="utf-8") as f:
            return json.load(f)["handlers"][0]

    def create(self, handler_type):
        """Create a handler of the given type."""
        handler = None

        def renew_cookies():
            if handler is None:
                raise ValueError("handler not set")
            handler.renew_cookies()

        def string_to_handler():
            ht = self.__handlers[handler_type]

            #TODO: Clean this up at some point.
            handlers = {
                "add_game_handler": "AddGameHandler",
                "all_games_handler": "AllGamesHandler",
                "all_hardware_handler": "AllHardwareHandler",
                "add_genre_handler": "AddGenreHandler",
                "add_hardware_handler": "AddHardwareHandler",
                "add_hardware_type_handler": "AddHardwareTypeHandler",
                "add_platform_handler": "AddPlatformHandler",
                "delete_game_handler": "DeleteGameHandler",
                "delete_genre_handler": "DeleteGenreHandler",
                "delete_hardware_handler": "DeleteHardwareHandler",
                "delete_hardware_type_handler": "DeleteHardwareTypeHandler",
                "delete_platform_handler": "DeletePlatformHandler",
                "delete_user_handler": "DeleteUserHandler",
                "edit_game_handler": "EditGameHandler",
                "edit_genre_handler": "EditGenreHandler",
                "edit_hardware_handler": "EditHardwareHandler",
                "edit_hardware_type_handler": "EditHardwareTypeHandler",
                "edit_platform_handler": "EditPlatformHandler",
                "edit_user_handler": "EditUserHandler",
                "export_collection_handler": "ExportCollectionHandler",
                "genres_handler": "GenresHandler",
                "get_export_handler": "GetExportHandler",
                "hardware_types_handler": "HardwareTypesHandler",
                "login_handler": "LoginHandler",
                "logout_handler": "LogoutHandler",
                "platforms_handler": "PlatformsHandler",
                "save_game_handler": "SaveGameHandler",
                "save_hardware_handler": "SaveHardwareHandler",
                "search_handler": "SearchHandler",
                "signin_handler": "SigninHandler",
                "signup_handler": "SignupHandler",
                "sort_games_handler": "SortGamesHandler",
                "sort_hardware_handler": "SortHardwareHandler",
                "update_game_handler": "UpdateGameHandler",
                "update_genre_handler": "UpdateGenreHandler",
                "update_hardware_handler": "UpdateHardwareHandler",
                "update_hardware_type_handler": "UpdateHardwareTypeHandler",
                "update_platform_handler": "UpdatePlatformHandler",
                "update_user_handler": "UpdateUserHandler",
                "users_handler": "UsersHandler",
                "view_game_handler": "ViewGameHandler"
            }
            if ht in handlers:
                module = importlib.import_module(f"ui.Handlers.{ht}")
                class_ = getattr(module, handlers[ht])
            else:
                module = __import__("ui.Handlers." + ht, fromlist=ht)
                class_ = getattr(module, ht)

            return class_(self.__interactor_factory, self.__renderer)

        if handler_type == "index":
            handler = IndexHandler(self.__interactor_factory, self.__renderer, self.__config)
        elif handler_type in self.__handlers:
            handler = string_to_handler()
        else:
            raise UnrecognisedHandlerException

        handler.session = Session()
        handler.cookies = Cookies()
        renew_cookies()
        return handler

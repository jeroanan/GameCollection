"""Unit tests for the AddGameHandler class"""
# Copyright (c) 2015, 2026 David Wilson
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
# along with Icarus.  If not, see <http://www.gnu.org/licenses/>.

from typing import Any
import unittest
from unittest.mock import Mock

import genre as g
from interactors.interactor_factory import InteractorFactory
from interactors.interactor import Interactor
from interactors.platform_interactors import GetPlatformsInteractor
from interactors.genre_interactors import GetGenresInteractor
import icarus_platform as p
from ui.handlers.add_game_handler import AddGameHandler
from ui.handlers.authenticated_handler import AuthenticatedHandler
from ui.handlers.Session.Session import Session
from ui.template_renderer import TemplateRenderer


class TestAddGameHandler(unittest.TestCase):
    """Unit tests for the AddGameHandler class"""

    def setUp(self) -> None:
        """setUp function for all unit tests in this class"""

        def initialise_interactor(interactor_type: Interactor, return_value: Any) -> Mock:
            interactor = Mock(interactor_type)
            interactor.execute = Mock(return_value=return_value)
            return interactor

        self.__platforms = [p.Platform()]
        self.__genres = [g.Genre()]
        interactor_factory = Mock(InteractorFactory)

        get_platforms_interactor = initialise_interactor(
            GetPlatformsInteractor(),
            self.__platforms)

        get_genres_interactor = initialise_interactor(
            GetGenresInteractor(),
            self.__genres)

        def create_interactor(interactor_type: str) -> Mock:
            if interactor_type == "GetPlatformsInteractor":
                return get_platforms_interactor
            elif interactor_type == "GetGenresInteractor":
                return get_genres_interactor
            else:
                raise ValueError("Unknown interactor type: " + interactor_type)

        interactor_factory.create = Mock(side_effect=create_interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = AddGameHandler(interactor_factory, self.__renderer)
        session = Mock(Session)
        self.__target.session = session

    def test_is_instance_of_authenticated_handler(self) -> None:
        """Test that AddGameHandler is an instance of AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_get_page_calls_renderer(self) -> None:
        """Test that calling AddGameHandler.get_page causes renderer.render to be called 
        correctly"""
        self.__target.get_page({})
        self.__renderer.render.assert_called_with("addgame.html", title="Add Game",
                                                  platforms=self.__platforms, genres=self.__genres)

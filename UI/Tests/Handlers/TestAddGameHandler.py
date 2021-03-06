# Copyright (c) 2015 David Wilson
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

import unittest
from unittest.mock import Mock

import Genre as g
from Interactors.InteractorFactory import InteractorFactory
import Interactors.PlatformInteractors as pi
import Interactors.GenreInteractors as gi
import Platform as p
from UI.Handlers.AddGameHandler import AddGameHandler
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.Session.Session import Session
from UI.TemplateRenderer import TemplateRenderer


class TestAddGameHandler(unittest.TestCase):
    """Unit tests for the AddGameHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""

        def initialise_interactor(interactor_type, return_value):
            interactor = Mock(interactor_type)
            interactor.execute = Mock(return_value=return_value)
            return interactor

        self.__platforms = [p.Platform()]
        self.__genres = [g.Genre()]
        interactor_factory = Mock(InteractorFactory)
        get_platforms_interactor = initialise_interactor(pi.GetPlatformsInteractor, self.__platforms)
        get_genres_interactor = initialise_interactor(gi.GetGenresInteractor, self.__genres)
        interactor_factory.create = Mock(return_value=get_platforms_interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = AddGameHandler(interactor_factory, self.__renderer)
        session = Mock(Session)
        self.__target.session = session

    def test_is_instance_of_authenticated_handler(self):
        """Test that AddGameHandler is an instance of AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_get_page_calls_renderer(self):
        """Test that calling AddGameHandler.get_page causes renderer.render to be called correctly"""
        self.__target.get_page({})
        self.__renderer.render.assert_called_with("addgame.html", title="Add Game", 
                                                  platforms=self.__platforms, genres=self.__genres)


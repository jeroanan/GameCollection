# Copyright (c) David Wilson 2015
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

import cherrypy
import unittest
from unittest.mock import Mock

from Game import Game
from Interactors.GameInteractors import GetGamesInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.AllGamesHandler import AllGamesHandler
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.Session.Session import Session
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.TemplateRenderer import TemplateRenderer


class TestAllGamesHandler(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.__games = [Game()]
        interactor = Mock(GetGamesInteractor)
        interactor.execute = Mock(return_value=self.__games)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = AllGamesHandler(interactor_factory, self.__renderer)
        self.__target.session = Mock(Session)
        self.__get_page = lambda: self.__target.get_page(self.__get_params())

    def test_is_authenticated_handler(self):
        """Test that AllGamesHandler is derived from AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_get_page_calls_renderer(self):
        """Test that calling AllGamesHandler.get_page causes GetGamesInteractor.execute to be called"""
        self.__get_page()
        self.__renderer.render.assert_called_with("allgames.html", games=self.__games, title="All Games", 
                                                  game_sort_field="title", game_sort_dir="asc", platform="platform", 
                                                  query="platform=platform")
        self.assertTrue(self.__renderer.render.called)

    def __get_params(self):
        return {
            "gamesort": "title",
            "gamesortdir": "asc",
            "platform": "platform"
        }

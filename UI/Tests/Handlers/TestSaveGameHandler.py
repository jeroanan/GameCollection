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
from Interactors.GameInteractors import AddGameInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.SaveGameHandler import SaveGameHandler
from UI.Handlers.Session.Session import Session
from UI.TemplateRenderer import TemplateRenderer
from UI.Tests.Handlers.HandlerTestAssertions import get_missing_param_assertion, get_empty_param_assertion

class TestSaveGameHandler(unittest.TestCase):
    """Unit tests for the SaveGameHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        renderer = Mock(TemplateRenderer)
        interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(AddGameInteractor)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = SaveGameHandler(interactor_factory, renderer)
        session = Mock(Session)
        session.get_value = Mock(return_value="1234")
        self.__target.session = session
        self.__missing_param_returns_empty_string = get_missing_param_assertion(self.__target)
        self.__empty_param_returns_empty_string = get_empty_param_assertion(self.__target)
        self.__required_params = ["title", "platform"]
        self.__get_page = lambda: self.__target.get_page(params=self.__get_args())
        self.__get_game = lambda: Game.from_dict(self.__get_args())

    def test_get_page_executes_interactor(self):
        """Test that calling SaveGameHandler.get_page causes AddGameInteractor.execute to be called"""
        self.__get_page()
        self.__interactor.execute.assert_called_with(game=self.__get_game(), user_id="1234")

    def test_is_instance_of_authenticated_handler(self):
        """Test that SaveGameHandler is derived from AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_empty_required_params_returns_empty_string(self):
        """Test that calling SaveGameHandler with an empty required parameter causes an empty string to be returned"""
        p = self.__get_args()
        for r in self.__required_params:
            self.assertTrue(self.__empty_param_returns_empty_string(r, p))

    def test_missing_required_params_returns_empty_string(self):
        """Test that calling SaveGameHandler with a missing required parameter causes an empty string to be returned"""
        p = self.__get_args()
        for r in self.__required_params:
            self.assertTrue(self.__missing_param_returns_empty_string(r, p))

    def __get_args(self):
        return {
            "title": "Title",
            "numcopies": 1,
            "numboxed": 2,
            "nummanuals": 3,
            "platform": "Platform",
            "notes": "Notes"
        }

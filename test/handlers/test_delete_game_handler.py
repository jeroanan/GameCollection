"""Provides unit tests for the DeleteGameHandler class"""
# Copyright (c) David Wilson 2015, 2026
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

from test.handlers.HandlerTestAssertions import \
    get_missing_param_assertion, get_empty_param_assertion
from game import Game
from interactors.game_interactors import DeleteGameInteractor
from interactors.interactor_factory import InteractorFactory
from ui.handlers.authenticated_handler import AuthenticatedHandler
from ui.handlers.delete_game_handler import DeleteGameHandler
from ui.handlers.Session.Session import Session
from ui.template_renderer import TemplateRenderer

class TestDeleteGameHandler(unittest.TestCase):
    """Unit tests for the DeleteGameHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        renderer = Mock(TemplateRenderer)
        interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(DeleteGameInteractor)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = DeleteGameHandler(interactor_factory, renderer)
        session = Mock(Session)
        session.get_value = Mock(return_value="1234")
        self.__target.session = session
        self.__get_page = self.__target.get_page
        self.__get_args = lambda id="id": {"id": id}
        self.__missing_arg_returns_empty_string = get_missing_param_assertion(self.__target)
        self.__empty_arg_returns_empty_string = get_empty_param_assertion(self.__target)

    def test_is_instance_of_authenticated_handler(self):
        """Test that DeleteGameHandler derives from AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_calls_interactor_execute(self):
        """Test that calling DeleteGameHandler.get_page causes DeleteGameInteractor.execute to be 
        called"""
        self.__get_page(self.__get_args())
        self.__interactor.execute.assert_called_with(Game.from_dict({"id": "id"}), "1234")

    def test_no_id_returns_empty_string(self):
        """Test that calling DeleteGameHandler.get_page with an empty id causes an empty string 
        to be returned"""
        self.__assert_validate_param("id", self.__missing_arg_returns_empty_string)

    def test_empty_id_returns_empty_string(self):
        """Test that calling DeleteGameHandler.get_page with a null id causes an empty string to 
        be returned"""
        self.__assert_validate_param("id", self.__empty_arg_returns_empty_string)

    def __assert_validate_param(self, param, validation_func):
        p = self.__get_args()
        self.assertTrue(validation_func(param, p))

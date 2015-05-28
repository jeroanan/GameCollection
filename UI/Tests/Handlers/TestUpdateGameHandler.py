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

from AbstractPersistence import AbstractPersistence
from Game import Game
from Interactors.Exceptions.PersistenceException import PersistenceException
from Interactors.InteractorFactory import InteractorFactory
from Interactors.GameInteractors import UpdateGameInteractor
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.Session.Session import Session
from UI.Handlers.UpdateGameHandler import UpdateGameHandler
from UI.TemplateRenderer import TemplateRenderer
from UI.Tests.Handlers.HandlerTestAssertions import get_missing_param_assertion, get_empty_param_assertion


class TestUpdateGameHandler(unittest.TestCase):
    """Unit tests for the UpdateGameHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        self.__interactor = Mock(UpdateGameInteractor)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=self.__interactor)
        session = Mock(Session)
        session.get_value = Mock(return_value="1234")
        self.__target = UpdateGameHandler(interactor_factory, Mock(TemplateRenderer))
        self.__target.session = session
        self.__missing_arg_returns_empty_string = get_missing_param_assertion(self.__target)
        self.__empty_arg_returns_empty_string = get_empty_param_assertion(self.__target)

    def test_is_instance_of_authenticated_handler(self):
        """Test that UpdateGameHandler derives from AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_calls_interactor_execute(self):
        """Test that calling UpdateGameHandler.get_page causes UpdateGameInteractor.execute to be called"""
        self.__target.get_page(params=self.__get_params())
        self.__interactor.execute.assert_called_with(game=Game.from_dict(self.__get_params()), user_id="1234")

    def test_misssing_required_params_returns_empty_string(self):
        """Test that any null required parameters causes UpdateGameHandler.get_page to return an empty string"""
        self.__assert_operation_on_required_params_returns_empty_string(self.__missing_arg_returns_empty_string)

    def test_empty_required_params_returns_empty_string(self):
        """Test that any empty required parameters causes UpdateGameHandler.get_page to return an empty string"""
        self.__assert_operation_on_required_params_returns_empty_string(self.__empty_arg_returns_empty_string)

    def __assert_operation_on_required_params_returns_empty_string(self, func):
        required_params = ["title", "platform"]
        params = self.__get_params()
        for r in required_params:
            self.assertTrue(func(r, params))

    def test_persistence_exception_gives_empty_string(self):        
        """Test that an exception from persistence causes UpdateGameHandler.get_page to return an empty string"""

        def init_target():
            def update_game(game, user_id):
                raise PersistenceException

            p = Mock(AbstractPersistence)
            interactor = Mock(UpdateGameInteractor)
            interactor.execute = Mock(side_effect=update_game)
            interactor_factory = Mock(InteractorFactory)
            interactor_factory.create = Mock(return_value=interactor)
            target = UpdateGameHandler(interactor_factory, Mock(TemplateRenderer))
            target.session = Mock(Session)
            return target
        
        result = init_target().get_page(self.__get_params())
        self.assertEqual("", result)

    def __get_params(self, title="title", platform="platform"):
        return {
            "id": "id",
            "title": title,
            "numcopies": 1,
            "numboxed": 2,
            "nummanuals": 3,
            "platform": platform,
            "notes": "notes"
        }


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

import unittest
from unittest.mock import Mock

import cherrypy

from Interactors.PlatformInteractors import DeletePlatformInteractor
from Interactors.InteractorFactory import InteractorFactory
from Platform import Platform
from UI.Handlers.DeletePlatformHandler import DeletePlatformHandler
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.Session.Session import Session
from UI.TemplateRenderer import TemplateRenderer


class TestDeletePlatformHandler(unittest.TestCase):
    """Unit test for the DeletePlatformHandler class."""

    def setUp(self):
        """setup function for all unit tests in this class."""
        renderer = Mock(TemplateRenderer)
        self.__interactor = Mock(DeletePlatformInteractor)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = DeletePlatformHandler(interactor_factory, renderer)
        self.__target.session = Mock(Session)
        self.__get_params = lambda: {"platformid": "id"}
        self.__get_page = lambda: self.__target.get_page(self.__get_params())

    def test_is_instance_of_authenticated_handler(self):
        """Test that DeletePlatformHandler is an instance of AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_executes_interactor(self):
        """Test that calling DeletePlatformHandler.get_page causes DeletePlatformInteractor.execute to be called."""
        self.__get_page()
        self.__interactor.execute.assert_called_with("id")

    def test_null_id_returns_empty_string(self):
        p = self.__get_params()
        del p["platformid"]
        self.__assert_target_returns_empty_string(p)

    def test_empty_id_returns_empty_string(self):
        p = self.__get_params()
        p["platformid"] = ""
        self.__assert_target_returns_empty_string(p)

    def __assert_target_returns_empty_string(self, params):
        result = self.__target.get_page(params)
        self.assertEqual("", result)

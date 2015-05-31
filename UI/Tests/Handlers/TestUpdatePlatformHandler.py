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

from Interactors.InteractorFactory import InteractorFactory
from Platform import Platform
from Interactors.PlatformInteractors import UpdatePlatformInteractor
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException 
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.Session.Session import Session
from UI.Handlers.UpdatePlatformHandler import UpdatePlatformHandler
from UI.Tests.Handlers.HandlerTestAssertions import get_missing_param_assertion, get_empty_param_assertion
from UI.TemplateRenderer import TemplateRenderer


class TestUpdatePlatformHandler(unittest.TestCase):
    """Unit tests for the UpdatePlatformHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(UpdatePlatformInteractor)
        interactor_factory.create = Mock(return_value=self.__interactor)
        renderer = Mock(TemplateRenderer)
        self.__target = UpdatePlatformHandler(interactor_factory, renderer)
        self.__target.session = Mock(Session)
        self.__platform = Platform.from_dict({"id": "id", "name": "name", "description": "description"})
        self.__missing_arg_returns_empty_string = get_missing_param_assertion(self.__target)
        self.__empty_arg_returns_empty_string = get_empty_param_assertion(self.__target)
        self.__get_page = lambda: self.__target.get_page(self.__get_params())

    def test_is_instance_of_authenticated_handler(self):
        """Test that UpdatePlatformHandler is an instance of AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_executes_interactor(self):
        """Test that calling UpdatePlatformHandler.get_page causes UpdatePlatformInteractor.execute to be called"""
        self.__get_page()
        self.__interactor.execute.assert_called_with(platform=self.__platform)
    
    def test_null_platform_returns_empty_string(self):
        """Test that calling UpdatePlatformInteractor.get_page with a null plaform returns an empty string"""
        result = self.__target.get_page(None)
        self.assertEqual("", result)        

    def test_missing_required_param_returns_empty_string(self):
        """Test that calling UpdatePlatformInteractor.get_page with a missing required plaform property returns an empty 
        string"""
        self.__assert_invalid_param_returns_empty_string(self.__missing_arg_returns_empty_string)

    def test_empty_required_param_returns_empty_string(self):
        """Test that calling UpdatePlatformInteractor.get_page with an empty required plaform property returns an empty
        string"""
        self.__assert_invalid_param_returns_empty_string(self.__empty_arg_returns_empty_string)

    def __assert_invalid_param_returns_empty_string(self, validation_func):
        required_params = ["id", "name"]
        for rp in required_params:
            self.assertTrue(validation_func(rp, self.__get_params()))

    def test_interactor_throws_exception_returns_empty_string(self):
        """Test that if UpdatePlatformInteractor.execute raises an exception then an empty string is returned"""
        def boom(platform):
            raise Exception("Boom!")

        self.__interactor.execute = Mock(side_effect=boom)
        self.__target.interactor = self.__interactor
        result = self.__get_page()
        self.assertEqual("", result)

    def __get_params(self):
        return {
            "id": "id",
            "name": "name",
            "description": "description"
        }



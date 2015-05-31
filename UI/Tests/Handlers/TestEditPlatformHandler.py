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

from Interactors.PlatformInteractors import GetPlatformInteractor
from Interactors.InteractorFactory import InteractorFactory
from Platform import Platform
from UI.Handlers.EditPlatformHandler import EditPlatformHandler
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.Session.Session import Session
from UI.TemplateRenderer import TemplateRenderer
from UI.Tests.Handlers.HandlerTestAssertions import (get_missing_param_assertion, get_empty_param_assertion)

class TestEditPlatformHandler(unittest.TestCase):
    """Unit tests for the EditPlatformHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        self.__platform = Platform()
        interactor_factory = Mock(InteractorFactory)
        interactor = Mock(GetPlatformInteractor)
        interactor.execute = Mock(return_value=self.__platform)
        interactor_factory.create = Mock(return_value=interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__renderer.render = Mock(return_value="some html")
        self.__target = EditPlatformHandler(interactor_factory, self.__renderer)
        session = Mock(Session)
        self.__target.session = session
        self.__missing_arg_returns_empty_string = get_missing_param_assertion(self.__target)
        self.__empty_arg_returns_empty_string = get_empty_param_assertion(self.__target)
        self.__args = {"platformid": "platformid"}

    def test_is_instance_of_authenticated_handler(self):
        """Test that EditPlatformHandler is an instance of AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_calls_renderer(self):
        """Test that calling EditPlatformHandler.get_page calls renderer.render correctly"""
        self.__target.get_page(self.__args)
        self.__renderer.render.assert_called_with("editplatform.html", platform=self.__platform, title="Edit Platform")

    def test_with_null_platformid_returns_empty_string(self):
        """Test that calling EditPlatformHandler.get_page with a null platformid causes empty string to be returned"""
        self.assertTrue(self.__missing_arg_returns_empty_string("platformid", self.__args))

    def test_with_empty_platformid_returns_empty_string(self):
        """Test that calling EditPlatformHandler.get_page with an empty platformid causes empty string to be returned"""
        self.assertTrue(self.__empty_arg_returns_empty_string("platformid", self.__args))

    def test_interactor_raises_exception_returns_empty_string(self):
        """Test that if an exception is raised when calling GetPlatformInteractor.execute, 
        EditPlatformHandler.get_page returns an empty string"""
        def ker_boom(platform_id):
            raise Exception("Betcha didn't see that coming!")
        
        interactor = Mock(GetPlatformInteractor)
        interactor.execute = Mock(side_effect=ker_boom)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=interactor)
        target = EditPlatformHandler(interactor_factory, None)
        target.session = Mock(Session)
        target.interactor = interactor
        result = target.get_page(self.__args)
        self.assertEqual("", result)
        

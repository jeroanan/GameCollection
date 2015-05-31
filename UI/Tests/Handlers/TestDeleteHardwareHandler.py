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

import cherrypy

from Interactors.HardwareInteractors import DeleteHardwareInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.DeleteHardwareHandler import DeleteHardwareHandler
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.Session.Session import Session
from UI.TemplateRenderer import TemplateRenderer
from UI.Tests.Handlers.HandlerTestAssertions import get_missing_param_assertion, get_empty_param_assertion

class TestDeleteHardwareHandler(unittest.TestCase):
    """Unit tests for the DeleteHardwareHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        renderer = Mock(TemplateRenderer)
        self.__interactor = Mock(DeleteHardwareInteractor)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = DeleteHardwareHandler(interactor_factory, renderer)
        self.__target.session = Mock(Session)
        self.__get_args = lambda: {"hardwareid": "hardwareid"}
        self.__missing_param_returns_empty_string = get_missing_param_assertion(self.__target)
        self.__empty_param_returns_empty_string = get_empty_param_assertion(self.__target)

    def test_is_instance_of_authenticated_handler(self):
        """Test that DeleteHardwareHandler derives from AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_null_hardwareid_returns_empty_string(self):
        """Test that calling DeleteHardwareHandler.get_page without a hardwareid 
        causes an empty string to be returned"""
        self.__assert_operation_on_required_params_returns_empty_string(
            "hardwareid", self.__missing_param_returns_empty_string)

    def test_empty_hardwareid_returns_empty_string(self):
        """Test that calling DeleteHardwareHandler.get_page with an empty hardwareid 
        causes an empty string to be returned"""
        self.__assert_operation_on_required_params_returns_empty_string(
            "hardwareid", self.__empty_param_returns_empty_string)

    def __assert_operation_on_required_params_returns_empty_string(self, param, func):
        self.assertTrue(func(param, self.__get_args()))
        
    def test_interactor_raises_exception_returns_empty_string(self):
        """Test that if DeleteHardwareInteractor.execute raises an exception then DeleteHardwareHandler.get_page 
        returns an empty string"""
        def boom(hardware_id, user_id):
            raise Exception("ouch!")
        
        interactor = Mock(DeleteHardwareInteractor)
        interactor.execute = Mock(side_effect=boom)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=interactor)
        self.__target = DeleteHardwareHandler(interactor_factory, None)
        self.__target.session = Mock(Session)

        result = self.__target.get_page(self.__get_args())
        self.assertEqual("", result)



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

from Hardware import Hardware
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from Interactors.HardwareInteractors import SaveHardwareInteractor
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.Session.Session import Session
from UI.Handlers.SaveHardwareHandler import SaveHardwareHandler
from UI.TemplateRenderer import TemplateRenderer
from UI.Tests.Handlers.HandlerTestAssertions import get_missing_param_assertion, get_empty_param_assertion


class TestSaveHardwareHandler(unittest.TestCase):
    """Unit tests for the SaveHardwareHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        renderer = Mock(TemplateRenderer)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(SaveHardwareInteractor)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = SaveHardwareHandler(self.__interactor_factory, renderer)
        session = Mock(Session)
        session.get_value = Mock(return_value="1234")
        self.__target.session = session
        self.__empty_param_returns_empty_string = get_empty_param_assertion(self.__target)
        self.__missing_param_returns_empty_string = get_missing_param_assertion(self.__target)

    def test_is_instance_of_authenticated_handler(self):
        """Test that SaveHardwareHandler is an instance of AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_get_page_executes_save_hardware_interactor(self):
        """Test that calling SaveHardwareHandler.execute causes SaveHardwareInteractor.execute to be called"""
        self.__target.get_page(params=self.__get_params())        
        self.__interactor.execute.assert_called_with(hardware=self.__get_hardware(), user_id="1234")

    def __get_hardware(self):
        return Hardware.from_dict(self.__get_params())

    def test_null_required_param_returns_empty_string(self):
        """Test that calling SaveHardwareHandler.get_page with a null required parameter causes an empty string to 
        be returned"""
        self.__operation_on_required_params(self.__missing_param_returns_empty_string)

    def test_empty_required_param_returns_empty_string(self):
        """Test that calling SaveHardwareHandler.get_page with an empty required parameter causes an empty string to 
        be returned"""
        self.__operation_on_required_params(self.__empty_param_returns_empty_string)

    def __operation_on_required_params(self, func):
        required_params = ["name", "platform", "numcopies"]
        params = self.__get_params()
        for rp in required_params:
            self.assertTrue(func(rp, params), rp)

    def __get_params(self):
        return {
            "name": "name",
            "platform": "platform",
            "numcopies": 1,
            "numboxed": 2,
            "notes": "notes"
        }

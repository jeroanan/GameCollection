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
# along with Icarus.  If not, see <http://www.gnu.org/licenses/.>

import unittest
from unittest.mock import Mock

import cherrypy

from Hardware import Hardware
from Interactors.InteractorFactory import InteractorFactory
from Interactors.HardwareInteractors import UpdateHardwareInteractor
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.AddGameHandler import AuthenticatedHandler
from UI.Handlers.Session.Session import Session
from UI.Handlers.UpdateHardwareHandler import UpdateHardwareHandler
from UI.TemplateRenderer import TemplateRenderer
from UI.Tests.Handlers.HandlerTestAssertions import get_missing_param_assertion, get_empty_param_assertion


class TestUpdateHardwareHandler(unittest.TestCase):
    """Unit tests for the UpdateHardwareHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        self.__interactor = Mock(UpdateHardwareInteractor)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=self.__interactor)
        renderer = Mock(TemplateRenderer)
        self.__target = UpdateHardwareHandler(interactor_factory, renderer)
        session = Mock(Session)
        session.get_value = Mock(return_value="1234")
        self.__target.session = session
        self.__missing_param_returns_empty_string = get_missing_param_assertion(self.__target)
        self.__empty_param_returns_empty_string = get_empty_param_assertion(self.__target)

    def test_is_instance_of_authenticated_handler(self):
        """Test that UpdateHardwareHandler is an instance of AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_executes_interactor(self):
        """Test that calling UpdateHardwareHandler.get_page causes UpdateHardwareInteractor.execute to be called"""
        self.__target.get_page(params=self.__get_params())
        self.__interactor.execute.assert_called_with(self.__get_hardware(), "1234")
    
    def test_empty_required_param_returns_empty_string(self):
        """Test that calling UpdateHardwareHandler.get_page with an empty required parameter returns an empty string"""
        self.__operation_on_required_params(self.__empty_param_returns_empty_string)

    def test_null_required_param_returns_empty_string(self):
        """Test that calling UpdateHardwareHandler.get_page with a missing required parameter returns an empty string"""
        self.__operation_on_required_params(self.__missing_param_returns_empty_string)

    def __operation_on_required_params(self, func):
        required_params = ["name", "platform"]
        params = self.__get_params()
        for rp in required_params:
            self.assertTrue(func(rp, params), rp)
                    
    def __get_hardware(self):
        return Hardware.from_dict(self.__get_params())

    def __get_params(self):
        return {
            "id": "id",
            "name": "name",
            "platform": "platform",
            "numcopies": 1,
            "numboxed": 0,
            "notes": ""
        }

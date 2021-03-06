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

from functools import partial
import json
import unittest
from unittest.mock import Mock

import cherrypy

import Interactors.PlatformInteractors as pi
import Interactors.InteractorFactory as factory
import Platform as p
import UI.Handlers.AddPlatformHandler as aph
import UI.Handlers.AuthenticatedHandler as ah
import UI.Handlers.Session.Session as sess
import UI.Tests.Handlers.HandlerTestAssertions as hta

class TestAddPlatformHandler(unittest.TestCase):
    """Unit tests for all methods in the AddPlatformHandler class"""

    def setUp(self):
        """setUp method for all unit tests in this class"""
        interactor_factory = Mock(factory.InteractorFactory)
        self.__interactor = Mock(pi.AddPlatformInteractor)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = aph.AddPlatformHandler(interactor_factory, renderer=None)
        self.__target.session = Mock(sess.Session) 

    def test_is_instance_of_authenticated_handler(self):
        """Test that AddPlatformHandler is an instance of AuthenticatedHandler"""
        self.assertIsInstance(self.__target, ah.AuthenticatedHandler)

    def test_bad_name_gives_json_validation_failed_message(self):
        """
        Test that setting params['name'] to different bad values causes AddPlatformHandler.handler to return a json
        result of 'validation_failed'
        """
        assertion = hta.get_bad_value_returns_json_validation_failed_assertion(self, self.__target, ['name'])
        assertion(self.__get_args())
        
    def test_success_returns_json_success_message(self):
        """Test that if adding the platform is successful, the json result is 'ok'"""
        assertion = hta.get_params_returns_json_result_value_assertion(self, self.__target)
        assertion(self.__get_args(), 'ok')

    def test_exceptions_return_expected_json_results(self):
        """
        Test that when exceptions are encountered, the expected result value is returned
        """
        assertion = hta.get_exceptions_returns_json_result_value_assertion(self, self.__target, self.__interactor)

        expected_combos = [(pi.PlatformExistsException, 'already_exists'), 
                           (Exception, 'error')]
        
        assertion(self.__get_args(), expected_combos)

    def __get_args(self):
        return {
            "name": 'name',
            "description": 'description'
        }

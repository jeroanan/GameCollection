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

import json
import unittest
from unittest.mock import Mock

import HardwareType as ht
import Interactors.InteractorFactory as factory
import Interactors.HardwareInteractors as hi
import UI.Handlers.AddHardwareTypeHandler as ath
import UI.Handlers.AuthenticatedHandler as ah
import UI.Handlers.Session.Session as session
import UI.Tests.Handlers.HandlerTestAssertions as hta


class TestAddHardwareTypeHandler(unittest.TestCase):
    """Unit tests for the AddHardwareTypeHandler class"""

    def setUp(self):
        """setUp for all unit tests in this class"""
        interactor_factory = Mock(factory.InteractorFactory)
        self.__interactor = Mock(hi.AddHardwareTypeInteractor)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = ath.AddHardwareTypeHandler(interactor_factory, None)
        self.__target.session = Mock(session.Session)
 
    def test_is_instance_of_authenticated_handler(self):
        """Test that AddHardwareTypeHandler is an instance of AuthenticatedHandler"""
        self.assertIsInstance(self.__target, ah.AuthenticatedHandler)

    def test_successful_save_returns_json_ok_message(self):
        """
        Test that successfully adding a hardware type returns a json object with a field called result that has a value 
        of 'ok'
        """
        assertion = hta.get_params_returns_json_result_value_assertion(self, self.__target)
        assertion(self.__get_args(), 'ok')

    def test_invalid_params_return_json_validation_failed_message(self):
        """
        Test that setting params to invalid values returns a json object with a field called result that has a value of 
        'validation_failed'
        """
        assertion = hta.get_bad_value_returns_json_validation_failed_assertion(self, 
                                                                               self.__target, 
                                                                               ['name', 'description'])
        assertion(self.__get_args())

    def test_exceptions_return_expected_json_results(self):
        """
        Test that when exceptions are encountered, the expected result value is returned
        """
        assertion = hta.get_exceptions_returns_json_result_value_assertion(self, self.__target, self.__interactor)

        expected_combos = [(hi.HardwareTypeExistsException, 'already_exists'),
                           (Exception, 'error')]
       
        assertion(self.__get_args(), expected_combos)

    def __get_args(self):
        return {'name': 'name',
                'description': 'desc'}

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

    def test_get_page_executes_add_hardware_type_interactor(self):
        """Test that calling get_page causes AddHardwareTypeInteractor.execute to be callled"""

        dictionary = self.__get_args()
        hardware_type = ht.HardwareType.from_dict(dictionary)

        self.__target.get_page(dictionary)
        self.__interactor.execute.assert_called_with(hardware_type)

    def test_successful_save_returns_json_ok_message(self):
        """
        Test that successfully adding a hardware type returns a json object with a field called result that has a value 
        of 'ok'
        """
        self.__assert_args_give_json_result_value(self.__get_args(), 'ok')

    def test_invalid_params_return_json_validation_failed_message(self):
        """
        Test that setting params to invalid values returns a json object with a field called result that has a value of 
        'validation_failed'
        """
        forbidden_values = ['', None, ' ' ]
        
        for fv in forbidden_values:
            self.__assert_field_forbidden_value_returns_json_validation_failed_message(fv)

    def __assert_field_forbidden_value_returns_json_validation_failed_message(self, forbidden_value):
        required_fields = ['name', 'description']
        
        for rf in required_fields:
            args = self.__get_args()
            args[rf] = forbidden_value

            self.__assert_args_give_json_result_value(args, 'validation_failed')

    def test_hardware_type_already_exists_returns_json_already_exists_message(self):
        """
        Test that attempting to add a hardware type with the same name as an existing one returns a json object with 
        a field called result that has a value of 'already_exists'
        """
        self.__assert_exception_causes_result_value_to_be_returned(hi.HardwareTypeExistsException, 'already_exists')

    def test_misc_error_returns_json_error_message(self):
        """
        Test that a miscellaneous error arising while adding a hardware type returns a json object with a field called
        result that has a value of 'error'
        """
        self.__assert_exception_causes_result_value_to_be_returned(Exception, 'error')

    def __assert_exception_causes_result_value_to_be_returned(self, exception_type, result_value):
        """
        Assert that when the given exception is raised while adding a hardware type, the given value of result.result 
        is returned.

        Args:
            exception_type -- The class of exception to raise
            result_value -- The value of result.result that is expected when an exception of exception_type is raised
        """

        def interactor_execute(h):
            raise exception_type

        self.__interactor.execute = Mock(side_effect=interactor_execute)
        self.__assert_args_give_json_result_value(self.__get_args(), result_value)

    def __assert_args_give_json_result_value(self, args, json_result_value):
        result = json.loads(self.__target.get_page(args))
        self.assertEqual(json_result_value, result['result'])

    def __get_args(self):
        return {'name': 'name',
                'description': 'desc'}

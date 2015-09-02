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
import UI.Handlers.AuthenticatedHandler as ah
import UI.Handlers.Session.Session as session
import UI.Handlers.UpdateHardwareTypeHandler as handler


class TestUpdateHardwareTypeHandler(unittest.TestCase):
    """Unit tests for the UpdateHardwareTypeHandler class"""

    def setUp(self):
        """setUp for all unit tests in this class"""
        interactor_factory = Mock(factory.InteractorFactory)
        self.__interactor = Mock(hi.UpdateHardwareTypeInteractor)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = handler.UpdateHardwareTypeHandler(interactor_factory, None)
        self.__target.session = Mock(session.Session)
        self.__required_params = ['id', 'name']
    
    def test_is_instance_of_authenticated_handler(self):
        """Test that UpdateHardwareTypeHandler is am instance of AuthenticatedHandler"""
        self.assertIsInstance(self.__target, ah.AuthenticatedHandler)

    def test_get_page_executes_update_hardware_type_interactor(self):
        """
        Test that calling UpdateHardwareTypeHandler.get_page causes UpdateHardwareTypeInteractor.execute to be called.
        """
        params = self.__get_params()
        hardware_type = self.__get_hardware_type()
        self.__target.get_page(params)
        self.__interactor.execute.assert_called_with(hardware_type)

    def test_successful_save_returns_json_ok_message(self):
        """
        Test that successfully updating a hardware type returns a json object with a field called 'result' whose value 
        is 'ok'.
        """
        self.__assert_params_gives_json_result_message(self.__get_params(), 'ok')

    def test_none_hardware_type_returns_json_validation_failed_message(self):
        """
        Test that when hardware_type is None then a json object is returned with a field called 'result' whose value
        is 'validation_faled'
        """
        self.__assert_params_gives_json_validation_failed_message(None)

    def test_required_param_forbidden_value_returns_json_validation_failed_message(self):
        """
        Test that if a required parameter has a forbidden value then a json object is returned with a field called 
        'result' whose value is 'validation_failed'
        """
        forbidden_values = [None, '', ' ']

        for fv in forbidden_values:
            self.__assert_field_forbidden_value_returns_json_validation_failed_message(fv)

    def __assert_field_forbidden_value_returns_json_validation_failed_message(self, forbidden_value):
        """
        Assert that when required parameters are set to a forbidden value then a json object is returned with a field 
        called 'result' whose value is 'validation_failed'

        Args:
           forbidden_value: The forbidden value to set required fields to
        """
        for rf in self.__required_params:
            params = self.__get_params()
            params[rf] = forbidden_value

            self.__assert_params_gives_json_validation_failed_message(params)

    def test_missing_param_returns_json_validation_failed_message(self):
        """
        Test that when a required value is missing from hardware_type then a json object is returned with a field called 
        'result' whose value is 'validation_failed'
        """
        for rp in self.__required_params:
            params = self.__get_params()
            del(params[rp])
            self.__assert_params_gives_json_validation_failed_message(params)

    def __assert_params_gives_json_validation_failed_message(self, params):
        """
        Assert that when the given parameters are sent to UpdateHardwareTypeHandler.get_page then a json object is 
        returned with a field called 'result' whose value is 'validation_failed'

        Args:
            params: The parameters to send to UpdateHardwareTypeHandler.get_page
        """
        self.__assert_params_gives_json_result_message(params, 'validation_failed')

    def __assert_params_gives_json_result_message(self, params, result_value):
        """
        Assert that when the given parameters are sent to UpdateHardwareTypeHandler.get_page then a json object is
        returned with a field called 'result' whose value is the given result_value.
        
        Args:
            params: The parameters to send to UpdateHardwareTypeHandler.get_page
            result_value: The expected value of result.result
        """
        result = json.loads(self.__target.get_page(params))
        self.assertEqual(result_value, result['result'])

    def test_hardware_type_already_exists_returns_json_already_exists_message(self):
        """
        Test that when a different hardware type already exists with the same name then a json object is returned with 
        a field called 'result' whose value is 'already_exists'
        """
        self.__assert_exception_causes_json_message_to_be_returned(hi.HardwareTypeExistsException, 'already_exists')

    def test_hardware_type_doesnt_exists_raises_hardware_type_not_found_exception(self):
        """
        Test that when the hardware type does not exist then a json object is returned with a field called 'result' 
        whose value is 'not_found'
        """
        self.__assert_exception_causes_json_message_to_be_returned(hi.HardwareTypeNotFoundException, 'not_found')

    def test_misc_error_returns_json_error_message(self):
        """
        Test that when a miscellaneous exception is encountered by UpdateHardwareTypeHandler.get_page, a json object 
        is returned with a fiedl called 'result'' whose value is 'error'
        """
        self.__assert_exception_causes_json_message_to_be_returned(Exception, 'error')

    def __assert_exception_causes_json_message_to_be_returned(self, exception_type, result_value):
        """
        Assert that when the given type of exception is encountered by UpdateHardwareTypeHandler.get_page, a json object
        is returned with a field called 'result' whose value is result_value

        Args:
            exception_type: The type of exception that is expected to be encountered
            result_value: The expected value of result.result
        """
        def interactor_execute(x):
            raise exception_type

        self.__interactor.execute = Mock(side_effect=interactor_execute)

        result = json.loads(self.__target.get_page(self.__get_params()))
        self.assertEqual(result_value, result['result'])
        
    def __get_hardware_type(self):
        return ht.HardwareType.from_dict(self.__get_params())

    def __get_params(self):
        return {'id': 'myid',
                'name': 'n', 
                'description': 'd'}


        

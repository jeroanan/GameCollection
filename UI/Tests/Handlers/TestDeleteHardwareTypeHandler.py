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

import json
import unittest
from unittest.mock import Mock

import HardwareType as ht
import Interactors.HardwareInteractors as hi
import Interactors.InteractorFactory as factory
import UI.Handlers.AuthenticatedHandler as ah
import UI.Handlers.DeleteHardwareTypeHandler as handler
import UI.Handlers.Session.Session as session


class TestDeleteHardwareTypeHandler(unittest.TestCase):
    """Unit tests for the DeleteHardwareTypeHandler class"""

    def setUp(self):
        """setUp for all unit tests in this class"""
        interactor_factory = Mock(factory.InteractorFactory)
        self.__interactor = Mock(hi.DeleteHardwareTypeInteractor)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = handler.DeleteHardwareTypeHandler(interactor_factory, None)
        self.__target.session = Mock(session.Session)

    def test_is_instance_of_authenticated_handler(self):
        """Test that DeleteHardwareTypeHandler is an instance of AuthenticatedHandler"""
        self.assertIsInstance(self.__target, ah.AuthenticatedHandler)

    def test_get_page_executes_delete_hardware_type_interactor(self):
        """
        Test that calling DeleteHardwareTypeHandler.get_page causes DeleteHardwareTypeInteractor.execute to be called.
        """
        params = self.__get_params()
        hardware_type = self.__get_hardware_type()

        self.__target.get_page(params)
        self.__interactor.execute.assert_called_with(hardware_type)

    def test_deletion_successful_returns_json_ok_message(self):
        """
        Test that successfully deleting a hardware type causes a json object to be returned with a field called 'result' 
        whose value is 'ok'
        """
        self.__assert_params_gives_json_result_value(self.__get_params(), 'ok')

    def test_deleting_non_existant_hardware_type_returns_json_not_found_message(self):
        """
        Test that attempting to delete a non-existant hardwaretype causes a json object to be returned with a field 
        called 'result' whose value is 'not_found'
        """
        self.__assert_exception_gives_json_result_value(hi.HardwareTypeNotFoundException, 'not_found')

    def test_misc_error_returns_json_error_message(self):
        """
        Test that when target.get_page encounters a miscellaneous excpetion, a json object is returned with a field 
        called 'result' whose value is 'error'
        """
        self.__assert_exception_gives_json_result_value(Exception, 'error')

    def __assert_exception_gives_json_result_value(self, exception_type, result_value):
        """
        Assert that when target.get_page encounters the given exception, a json object is returned with a field called
        'result' whose value is result_value

        Args:
            exception_type: The expected exception type
            result_value: The expected value of result.result
        """
        def interactor_execute(x):
            raise exception_type
            
        self.__interactor.execute = Mock(side_effect=interactor_execute)
        self.__assert_params_gives_json_result_value(self.__get_params(), result_value)

    def __assert_params_gives_json_result_value(self, params, result_value):
        """
        Assert that calling target.get_page with the given params returns a json object with a field called 'result' 
        whose value is result_value

        Args:
            params: The dictionary of parameters to pass to target.get_page
            result_value: The expected value of result.result
        """
        result = json.loads(self.__target.get_page(params))
        self.assertEqual(result_value, result['result'])

    def __get_params(self):
        return {"name": "n", 
                "description": "desc"}

    def __get_hardware_type(self):
        return ht.HardwareType.from_dict(self.__get_params())

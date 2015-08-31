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

import Interactors.PlatformInteractors as pi
import Interactors.InteractorFactory as factory
import UI.Handlers.DeletePlatformHandler as dph
import UI.Handlers.AuthenticatedHandler as ah
import UI.Handlers.Session.Session as sess


class TestDeletePlatformHandler(unittest.TestCase):
    """Unit test for the DeletePlatformHandler class."""

    def setUp(self):
        """setup function for all unit tests in this class."""
        self.__interactor = Mock(pi.DeletePlatformInteractor)
        interactor_factory = Mock(factory.InteractorFactory)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = dph.DeletePlatformHandler(interactor_factory, None)
        self.__target.session = Mock(sess.Session)
        self.__get_params = lambda: {"id": "id"}
        self.__get_page = lambda: self.__target.get_page(self.__get_params())

    def test_is_instance_of_authenticated_handler(self):
        """Test that DeletePlatformHandler is an instance of AuthenticatedHandler"""
        self.assertIsInstance(self.__target, ah.AuthenticatedHandler)

    def test_executes_interactor(self):
        """Test that calling get_page causes DeletePlatformInteractor.execute to be called."""
        self.__get_page()
        self.__interactor.execute.assert_called_with("id")

    def test_deleltion_successful_returns_json_ok_message(self):
        """
        Test that when a platform is deleted successfully, a json object with a result field with a value of 'ok' is 
        returned.
        """
        self.__assert_params_give_json_result_message(self.__get_params(), 'ok')

    def test_null_id_returns_json_validation_failed_message(self):
        """
        Test that when calling get_page with no platform id, a json object with a result field with a value of 
        'validation_failed' is returned.
        """
        p = self.__get_params()
        del p["id"]
        self.__assert_params_gives_json_validation_failed(p)

    def test_empty_id_returns_json_validation_failed_message(self):
        """
        Test that when calling get_page with an empty id, a json object with a result field with a value of
        'validation_failed' is returned.
        """
        p = self.__get_params()
        p["id"] = ""
        self.__assert_params_gives_json_validation_failed(p)
    
    def test_null_id_returns_empty_string(self):
        """
        Test that when calling get_page with a null id, a json object with a result field with a value of
        'validation_failed' is returned.
        """
        p = self.__get_params()
        p["id"] = None
        self.__assert_params_gives_json_validation_failed(p)

    def __assert_params_gives_json_validation_failed(self, params):
        """
        Assert that when the given params are passed to target.get_page, a json object with a result field with a value
        of 'validation_failed' is returned.

        Args:
            params: An object of type Platform
        """
        self.__assert_params_give_json_result_message(params, 'validation_failed')

    def test_platform_does_not_exist_returns_json_not_found_message(self):
        """
        Test that if the platform to be deleted does not exist, a json object with a result field with a value of 
        'not_found' is returned.
        """
        
        def interactor_execute(p):
            raise pi.PlatformNotFoundException

        self.__interactor.execute = Mock(side_effect=interactor_execute)        
        self.__assert_params_give_json_result_message(self.__get_params(), 'not_found')

    def test_misc_error_returns_json_error_message(self):
        """
        Test that if a miscellaneous error is encountered while deleting a platform, a json object with a result field
        with a value of 'error' is returned.
        """
        
        def interactor_execute(p):
            raise Exception

        self.__interactor.execute = Mock(side_effect=interactor_execute)        
        self.__assert_params_give_json_result_message(self.__get_params(), 'error')

    def __assert_params_give_json_result_message(self, params, result_message):
        """
        Assert that when the given params are passed to target.get_page, a json object with a result field with a value
        of result_message is returned.

        Args:
            params: An object of type Platform
            result_message: The expected value of result['result']
        """
        result = json.loads(self.__target.get_page(params))
        self.assertEqual(result_message, result['result'])
        
    

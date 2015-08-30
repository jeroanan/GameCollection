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

import cherrypy

import Interactors.InteractorFactory as factory
import Platform as p
import Interactors.PlatformInteractors as pi
import UI.Handlers.AuthenticatedHandler as ah
import UI.Handlers.Session.Session as sess
import UI.Handlers.UpdatePlatformHandler as uph


class TestUpdatePlatformHandler(unittest.TestCase):
    """Unit tests for the UpdatePlatformHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        interactor_factory = Mock(factory.InteractorFactory)
        self.__interactor = Mock(pi.UpdatePlatformInteractor)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = uph.UpdatePlatformHandler(interactor_factory, renderer=None)
        self.__target.session = Mock(sess.Session)
        self.__platform = p.Platform.from_dict({"id": "id", "name": "name", "description": "description"})
        self.__get_page = lambda: self.__target.get_page(self.__get_params())

    def test_is_instance_of_authenticated_handler(self):
        """Test that UpdatePlatformHandler is an instance of AuthenticatedHandler"""
        self.assertIsInstance(self.__target, ah.AuthenticatedHandler)

    def test_update_successful_returns_json_ok_message(self):
        """
        Test that calling UpdatePlatformHandler.get_page causes a json object with a result value of 'ok' to be returned
        """
        self.__assert_get_page_with_params_returns_result_message(self.__get_params(), 'ok')

    def test_null_platform_returns_json_validation_failed_message(self):
        """
        Test that calling UpdatePlatformInteractor.get_page with a null plaform causes a json object with a result 
        value of 'failed_validation' to be returned.
        """
        self.__assert_get_page_with_params_returns_result_message(None, 'validation_failed')

    def test_missing_required_param_returns_json_validation_failed_message(self):
        """
        Test that calling UpdatePlatformInteractor.get_page with a missing required plaform property causes a json
        object with a result value of 'failed_validation' to be returned.
        """
        required_params = ['id', 'name']

        for rp in required_params:
            param = self.__get_params()
            del(param[rp])
            self.__assert_get_page_with_params_returns_result_message(param, 'validation_failed')

    def test_empty_required_param_returns_json_validation_failed_message(self):
        """
        Test that calling UpdatePlatformInteractor.get_page with an empty required plaform property causes a json object
        with a result value of 'failed_validation' to be returned.
        """
        required_params = ['id', 'name']

        for rp in required_params:
            param = self.__get_params()
            param[rp] = ''
            self.__assert_get_page_with_params_returns_result_message(param, 'validation_failed')

    def __assert_get_page_with_params_returns_result_message(self, params, result_value):
        """
        Test that calling UpdatePlatformHandler with the given params dictionary returns a json object with the 
        'result' field set tot the given value.
        :param params: The params dictionary to be passed to UpdatePlatformHandler.get_page
        :param result_value: The expected value of the 'result' field of the returned json object
        """
        result = json.loads(self.__target.get_page(params))
        self.assertEqual(result_value, result['result'])

    def test_interactor_throws_exception_returns_json_error_message(self):
        """
        Test that if a miscellaneous error happens when saving a platform then a json object with a result value of 
        'error' is returned
        """
        self.__assert_exception_causes_json_message_to_be_returned(Exception, 'error')

    def test_platform_already_exists_returns_json_already_exists_message(self):
        """
        Test that if the platform to be updated already exists (i.e. as a different record from this) then a json object
        with a result value of 'already_exists' is returned
        """
        self.__assert_exception_causes_json_message_to_be_returned(pi.PlatformExistsException, 'already_exists')

    def test_platform_does_not_exist_returns_json_not_found_message(self):
        """
        Test that if the platform to be updated does not exists then a json object with a result value of 'not_found'
        is returned
        """
        self.__assert_exception_causes_json_message_to_be_returned(pi.PlatformNotFoundException, 'not_found')

    def __assert_exception_causes_json_message_to_be_returned(self, exception_type, result_value):
        """
        Assert that when an exception of the given type is raised while updating a platform, a json object with a
        result field of result_value is returned
        """

        def interactor_execute(platform):
            raise exception_type

        self.__interactor.execute = Mock(side_effect=interactor_execute)
        self.__target.interactor = self.__interactor
        result = self.__get_page()
        json_result = json.loads(result)
        self.assertEqual(result_value, json_result['result'])

    def __get_params(self):
        return {
            "id": "id",
            "name": "name",
            "description": "description"
        }



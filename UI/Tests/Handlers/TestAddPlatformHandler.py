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


class TestAddPlatformHandler(unittest.TestCase):
    """Unit tests for all methods in the AddPlatformHandler class"""

    def setUp(self):
        """setUp method for all unit tests in this class"""

        interactor_factory = Mock(factory.InteractorFactory)
        self.__interactor = Mock(pi.AddPlatformInteractor)

        def add_platform_interactor_execute(platform):
            if platform.name == 'already_exists':
                raise pi.PlatformExistsException
            elif platform.name == 'go_boom':
                raise Exception

        self.__interactor.execute = Mock(side_effect=add_platform_interactor_execute)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = aph.AddPlatformHandler(interactor_factory, renderer=None)
        self.__target.session = Mock(sess.Session) 

    def test_is_instance_of_authenticated_handler(self):
        """Test that AddPlatformHandler is an instance of AuthenticatedHandler"""
        self.assertIsInstance(self.__target, ah.AuthenticatedHandler)

    def test_platform_fails_validation_returns_json_validation_failed_message(self):
        """Test that if validation of parameters fails, the json result is 'validation_failed'"""
        params = self.__get_args(name='')
        self.__assert_add_platform_returns_json_message(params, 'validation_failed')
        
    def test_success_returns_json_success_message(self):
        """Test that if adding the platform is successful, the json result is 'ok'"""
        params = self.__get_args(name='platform')
        self.__assert_add_platform_returns_json_message(params, 'ok')

    def test_platform_already_exists_returns_json_platform_exists_message(self):
        """Test that if the platform already exists, the json result is 'already_exists'"""
        params = self.__get_args(name='already_exists')
        self.__assert_add_platform_returns_json_message(params, 'already_exists')
    
    def test_misc_error_returns_json_error_message(self):
        """Test that if a misc exception occurs when adding a platform, the json result is 'error'"""
        params = self.__get_args(name='go_boom')
        self.__assert_add_platform_returns_json_message(params, 'error')

    def __assert_add_platform_returns_json_message(self, params, result_content):
        """
        Assert that sending the given parameters to the platofrm returns the given content in its json result.
        :param params: An dictionary containing the platform details
        :json_content: The expected content of json result
        """
        result = self.__target.get_page(params)
        json_result = json.loads(result)
        self.assertEqual(result_content, json_result['result'])

    def __get_args(self, name="name", description="description"):
        return {
            "name": name,
            "description": description
        }

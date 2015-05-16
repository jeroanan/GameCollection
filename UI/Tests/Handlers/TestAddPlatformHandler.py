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
import unittest
from unittest.mock import Mock

import cherrypy

from Interactors.Platform.AddPlatformInteractor import AddPlatformInteractor
from Interactors.InteractorFactory import InteractorFactory
from Platform import Platform
from UI.Handlers.AddPlatformHandler import AddPlatformHandler
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.Session.Session import Session
from UI.TemplateRenderer import TemplateRenderer
from UI.Tests.Handlers.HandlerTestAssertions import (get_missing_param_assertion, 
                                                     get_empty_param_assertion)
                                                     

class TestAddPlatformHandler(unittest.TestCase):

    def setUp(self):
        interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(AddPlatformInteractor)
        interactor_factory.create = Mock(return_value=self.__interactor)
        renderer = Mock(TemplateRenderer)
        self.__target = AddPlatformHandler(interactor_factory, renderer)
        self.__target.session = Mock(Session) 
        missing_param_assertion = get_missing_param_assertion(self.__target)
        self.__missing_param_test = partial(missing_param_assertion, params=self.__get_args())
        empty_param_assertion = get_empty_param_assertion(self.__target)
        self.__empty_param_test = partial(empty_param_assertion, params=self.__get_args())

    def test_is_instance_of_authenticated_handler(self):
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_calls_interactor_execute(self):
        self.__get_page()
        self.__interactor.execute.assert_called_with(Platform.from_dict(self.__get_args()))

    def __get_page(self):
        params = self.__get_args()
        self.__target.get_page(params)

    def test_platform_null_name_returns_empty_string(self):
        self.assertTrue(self.__missing_param_test("name"))

    def test_platform_empty_name_returns_empty_string(self):
        self.assertTrue(self.__empty_param_test("name"))

    def __get_args(self, name="name", description="description"):
        return {
            "name": name,
            "description": description
        }


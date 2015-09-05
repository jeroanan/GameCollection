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
import UI.Tests.Handlers.HandlerTestAssertions as hta


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

    def test_deletion_successful_returns_json_ok_message(self):
        """
        Test that successfully deleting a hardware type causes a json object to be returned with a field called 'result' 
        whose value is 'ok'
        """
        assertion = hta.get_params_returns_json_result_value_assertion(self, self.__target)
        assertion(self.__get_params(), 'ok')

    def test_exceptions_return_expected_json_results(self):
        """
        Test that when exceptions are encountered, the expected result value is returned
        """
        assertion = hta.get_exceptions_returns_json_result_value_assertion(self, self.__target, self.__interactor)

        expected_combos = [(hi.HardwareTypeNotFoundException, 'not_found'),
                           (Exception, 'error')]
        
        assertion(self.__get_params(), expected_combos)

    def __get_params(self):
        return {"name": "n", 
                "description": "desc"}

    def __get_hardware_type(self):
        return ht.HardwareType.from_dict(self.__get_params())

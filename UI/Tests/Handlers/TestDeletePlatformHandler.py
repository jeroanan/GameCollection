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
import UI.Tests.Handlers.HandlerTestAssertions as hta


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

        self.__json_message_assertion = hta.get_params_returns_json_result_value_assertion(self, self.__target)
        self.__exception_assertion = hta.get_exception_returns_json_result_value_assertion(self, self.__target, self.__interactor)

    def test_is_instance_of_authenticated_handler(self):
        """Test that DeletePlatformHandler is an instance of AuthenticatedHandler"""
        self.assertIsInstance(self.__target, ah.AuthenticatedHandler)

    def test_deleltion_successful_returns_json_ok_message(self):
        """
        Test that when a platform is deleted successfully, a json object with a result field with a value of 'ok' is 
        returned.
        """
        self.__json_message_assertion(self.__get_params(), 'ok')

    def test_bad_id_gives_json_validation_failed_message(self):
        """
        Test that setting params['id'] to different bad values causes DeletePlatformHandler.handler to return a json 
        result of 'validation_failed'
        """
        
        def delete_id(x):
            del x['id']
            return x

        def empty_id(x):
            x['id'] = ''
            return x

        def null_id(x):
            x['id'] = None
            return x

        make_bad_funcs = [delete_id, empty_id, null_id]

        for bf in make_bad_funcs:
            p = bf(self.__get_params())
            self.__json_message_assertion(p, 'validation_failed')

    def test_exceptions_return_expected_json_results(self):
        """
        Test that when exceptions are encountered by DeletePlatformHandler.get_page, the expected result value is 
        returned
        """
        expected_combos = [(pi.PlatformNotFoundException, 'not_found'), 
                           (Exception, 'error')]

        for ec in expected_combos:
            expected_exception, result_value = ec
            self.__exception_assertion(self.__get_params(), expected_exception, result_value)

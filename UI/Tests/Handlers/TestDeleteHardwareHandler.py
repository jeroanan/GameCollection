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

import unittest
from unittest.mock import Mock

import Interactors.HardwareInteractors as hi
import Interactors.InteractorFactory as factory
import UI.Handlers.DeleteHardwareHandler as dhh
import UI.Handlers.AuthenticatedHandler as ah
import UI.Handlers.Session.Session as sess
import UI.Tests.Handlers.HandlerTestAssertions as hta

class TestDeleteHardwareHandler(unittest.TestCase):
    """Unit tests for the DeleteHardwareHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        self.__interactor = Mock(hi.DeleteHardwareInteractor)
        interactor_factory = Mock(factory.InteractorFactory)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = dhh.DeleteHardwareHandler(interactor_factory, None)
        self.__target.session = Mock(sess.Session)
        self.__get_args = lambda: {"id": "hardwareid"}
        self.__missing_param_returns_empty_string = hta.get_missing_param_assertion(self.__target)
        self.__empty_param_returns_empty_string = hta.get_empty_param_assertion(self.__target)

    def test_is_instance_of_authenticated_handler(self):
        """Test that DeleteHardwareHandler derives from AuthenticatedHandler"""
        self.assertIsInstance(self.__target, ah.AuthenticatedHandler)

    def test_null_id_returns_empty_string(self):
        """Test that calling DeleteHardwareHandler.get_page without a id
        causes an empty string to be returned"""
        self.__assert_operation_on_required_params_returns_empty_string(
            "id", self.__missing_param_returns_empty_string)

    def test_empty_id_returns_empty_string(self):
        """Test that calling DeleteHardwareHandler.get_page with an empty id
        causes an empty string to be returned"""
        self.__assert_operation_on_required_params_returns_empty_string(
            "id", self.__empty_param_returns_empty_string)

    def __assert_operation_on_required_params_returns_empty_string(self, param, func):
        self.assertTrue(func(param, self.__get_args()))
        
    def test_interactor_raises_exception_returns_empty_string(self):
        """Test that if DeleteHardwareInteractor.execute raises an exception then DeleteHardwareHandler.get_page 
        returns an empty string"""
        def boom(hardware_id, user_id):
            raise Exception("ouch!")
        
        interactor = Mock(hi.DeleteHardwareInteractor)
        interactor.execute = Mock(side_effect=boom)
        interactor_factory = Mock(factory.InteractorFactory)
        interactor_factory.create = Mock(return_value=interactor)
        self.__target = dhh.DeleteHardwareHandler(interactor_factory, None)
        self.__target.session = Mock(sess.Session)

        result = self.__target.get_page(self.__get_args())
        self.assertEqual("", result)



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

import AbstractPersistence as ap
import HardwareType as ht
import Interactors.HardwareInteractors as hi
import Interactors.Interactor as interactor


class TestDeleteHardwareTypeInteractor(unittest.TestCase):
    """Unit tests for the DeleteHardwareTypeInteractor class"""

    def setUp(self):
        """setUp for all unit tests in this class"""
        self.__persistence = Mock(ap.AbstractPersistence)
        self.__persistence.get_hardware_types_list = Mock(return_value=[self.__get_hardware_type()])
        self.__target = hi.DeleteHardwareTypeInteractor()
        self.__target.persistence = self.__persistence
    
    def test_is_instance_of_interactor(self):
        """Test that DeleteHardwareTypeInteractor is an instance of Interactor"""
        self.assertIsInstance(self.__target, interactor.Interactor)

    def test_execute_calls_persistence_delete_hardware_type_method(self):
        """
        Test that calling DeleteHardwareTypeInteractor.execute causes persistence.delete_hardware_type to be called
        """
        h = self.__get_hardware_type()
        self.__target.execute(h)
        self.__persistence.delete_hardware_type.assert_called_with(h)

    def test_hardware_type_does_not_exist_raises_hardware_type_not_found_exception(self):
        """
        Test that when an attempt is made to delete a non-existant hardware type, HardwareTypeNotFoundException is 
        raised.
        """
        non_existant_hardware_type = self.__get_hardware_type(1415)
        self.assertRaises(hi.HardwareTypeNotFoundException, self.__target.execute, non_existant_hardware_type)

    def __get_hardware_type(self, id='1414'):
        h = {'id': id,
             'name': 'name',
             'description': 'description'}
        return ht.HardwareType.from_dict(h)

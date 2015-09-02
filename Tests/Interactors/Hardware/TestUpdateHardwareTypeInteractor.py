# Copyright (c) 20115 David Wilson
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


class TestUpdateHardwareTypeInteractor(unittest.TestCase):
    """Unit tests for the UpdateHardwareTypeInteractor class"""

    def setUp(self):
        """setUp for all unit tests in this class"""
        self.__persistence = Mock(ap.AbstractPersistence)
        self.__target = hi.UpdateHardwareTypeInteractor()
        self.__target.persistence = self.__persistence
        self.__required_fields = ['name', 'description']

    def test_is_instance_of_interactor(self):
        """Test that UpdateHardwareTypeInteractor is an instance of Interactor"""
        self.assertIsInstance(self.__target, interactor.Interactor)

    def test_execute_none_hardware_type_raises_type_error(self):
        """Test that calling execute with a hardware_type of None causes a TypeError to be raised"""
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_invalid_hardware_type_member_values_raises_value_error(self):
        """
        Test that calling execute with invalid values of required fields of hardware_type causes ValueError to be raised
        """
        forbidden_values = ['', None, ' ']
        
        for fv in forbidden_values:
            self.__assert_forbidden_value_raises_value_error(fv)

    def test_hardware_type_already_exists_raises_hardware_type_exists_exception(self):
        """
        Test that if another hardware type exists with the same name as the one we're trying to update, 
        HardwareTypeExistsException is raised.
        """
        existing_hardware_type = self.__get_hardware_type()
        existing_hardware_type.id = 1414
        self.__persistence.get_hardware_types_list = Mock(return_value=[existing_hardware_type])
        
        hardware_type = self.__get_hardware_type()
        hardware_type.id = 1415
    
        self.assertRaises(hi.HardwareTypeExistsException, self.__target.execute, hardware_type)

    def test_hardware_type_doesnt_exists_raises_hardware_type_not_found_exception(self):
        
        existing_hardware_type = self.__get_hardware_type()
        existing_hardware_type.id = 1414
        self.__persistence.get_hardware_types_list = Mock(return_value=[existing_hardware_type])

        hardware_type = self.__get_hardware_type()
        hardware_type.id = 1415
        hardware_type.name = 'doesnt exist'

        self.assertRaises(hi.HardwareTypeNotFoundException, self.__target.execute, hardware_type)

    def __assert_forbidden_value_raises_value_error(self, forbidden_value):
        for rf in self.__required_fields:
            hardware_type = self.__get_hardware_type()
            setattr(hardware_type, rf, forbidden_value)
            self.assertRaises(ValueError, self.__target.execute, hardware_type)

    def __get_hardware_type(self):
        h = {'name': 'name',
             'description': 'description'}
        return ht.HardwareType.from_dict(h)


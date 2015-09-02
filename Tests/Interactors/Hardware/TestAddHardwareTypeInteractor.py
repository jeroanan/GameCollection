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
import unittest.mock as mock

import AbstractPersistence as abstract_persistence
import HardwareType as ht
import Interactors.Interactor as interactor
import Interactors.HardwareInteractors as hi


class TestAddHardwareTypeInteractor(unittest.TestCase):
    """Unit tests for the AddHardwareTypeInteractor class"""
    
    def setUp(self):
        """setUp for all unit tests in this class"""
        self.__persistence = mock.Mock(abstract_persistence.AbstractPersistence)
        self.__target = hi.AddHardwareTypeInteractor()
        self.__target.persistence = self.__persistence
        self.__required_fields = ['name', 'description']

    def test_is_instance_of_interactor(self):
        """Test that AddHardwareTypeInteractor is an instance of Interactor"""
        self.assertIsInstance(self.__target, interactor.Interactor)

    def test_none_hardware_raises_type_error(self):
        """Test that passing a hardware_type of None causes a TypeError to be raised"""
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_null_or_empty_required_field_raises_value_error(self):
        """Test that passing in required members of Platform causes a ValueError to be raised"""
        self.__assert_forbidden_value_raises_value_error(None)
        self.__assert_forbidden_value_raises_value_error('')
        self.__assert_forbidden_value_raises_value_error(' ')

    def __assert_forbidden_value_raises_value_error(self, forbidden_value):
        for rf in self.__required_fields:
            hardware_type = self.__get_hardware_type()
            setattr(hardware_type, rf, forbidden_value)
            self.assertRaises(ValueError, self.__target.execute, hardware_type)

    def test_hardware_type_already_exists_raises_hardware_type_exists_exception(self):
        """Test that adding a hardware type that already exists causes HardwareTypeExistsException to be raised"""
        existing_hardware_type = self.__get_hardware_type()
        self.__persistence.get_hardware_types_list = mock.Mock(return_value=[existing_hardware_type])
        self.__target.persistence = self.__persistence

        self.assertRaises(hi.HardwareTypeExistsException, self.__target.execute, existing_hardware_type)

    def __get_hardware_type(self):
        h = {'name': 'name',
             'description': 'description'}
        return ht.HardwareType.from_dict(h)


        

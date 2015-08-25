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
import Interactors.HardwareInteractors as hardware_interactors


class TestAddHardwareTypeInteractor(unittest.TestCase):
    
    def setUp(self):
        self.__persistence = mock.Mock(abstract_persistence.AbstractPersistence)
        self.__target = hardware_interactors.AddHardwareTypeInteractor()
        self.__target.persistence = self.__persistence
        self.__required_fields = ['name', 'description']

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, interactor.Interactor)

    def test_none_hardware_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_null_or_empty_required_field_raises_value_error(self):
        self.__assert_forbidden_value_raises_value_error(None)
        self.__assert_forbidden_value_raises_value_error('')

    def __get_hardware_type(self):
        hardware_type = ht.HardwareType()
        hardware_type.name = 'name'
        hardware_type.description = 'description'
        return hardware_type

    def __assert_forbidden_value_raises_value_error(self, forbidden_value):
        for rf in self.__required_fields:
            hardware_type = self.__get_hardware_type()
            setattr(hardware_type, rf, forbidden_value)
            self.assertRaises(ValueError, self.__target.execute, hardware_type)

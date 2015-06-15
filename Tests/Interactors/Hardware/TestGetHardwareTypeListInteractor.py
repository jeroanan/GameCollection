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

import AbstractPersistence as ap
import Interactors.Interactor as i
import Interactors.HardwareInteractors as hi

class TestGetHardwareTypeListInteractor(unittest.TestCase):
    
    def setUp(self):
        self.__persistence = Mock(ap.AbstractPersistence)
        self.__target = hi.GetHardwareTypeListInteractor()
        self.__target.persistence = self.__persistence
        
    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, i.Interactor)

    def test_execute_calls_persistence_method(self):
        self.__target.execute()
        self.__persistence.get_hardware_types_list.assert_called_with()

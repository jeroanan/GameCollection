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
import Interactors.Interactor as interactor
import Interactors.HardwareInteractors as hi


class TestGetHardwareTypeInteractor(unittest.TestCase):
    
    def setUp(self):
        self.__target = hi.GetHardwareTypeInteractor()
        self.__persistence = Mock(ap.AbstractPersistence)
        self.__target.persistence = self.__persistence 

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, interactor.Interactor)

    def test_execute_calls_persistence_method(self):
        hardware_type = ht.HardwareType()
        self.__target.execute(hardware_type)
        self.__persistence.get_hardware_type.assert_called_with(hardware_type)

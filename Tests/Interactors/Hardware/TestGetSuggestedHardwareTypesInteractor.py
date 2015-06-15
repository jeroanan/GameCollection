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
import HardwareType as h
import Interactors.Interactor as interactor
import Interactors.HardwareInteractors as hi

class TestGetSuggestedHardwareTypesInteractor(unittest.TestCase):
    
    def setUp(self):

        get_hardware_type = lambda name: h.HardwareType.from_dict({"name": name})

        def setUp_persistence():
            stored_hardware_types = [get_hardware_type("type1")]
            persistence = Mock(ap.AbstractPersistence)
            persistence.get_hardware_types_list = Mock(return_value=stored_hardware_types)
            return persistence

        get_suggested_hardware_types = lambda: self.__suggested_hardware_types

        self.__suggested_hardware_types = [get_hardware_type("type1"), get_hardware_type("type2")]
        self.__target = hi.GetSuggestedHardwareTypesInteractor(get_suggested_hardware_types)
        self.__target.persistence = setUp_persistence()

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, interactor.Interactor)

    def test_execute_only_returns_hardware_types_not_stored(self):
        hardware_types = self.__target.execute()
        self.assertEqual(1, len(hardware_types))

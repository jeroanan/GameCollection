"""Unit tests for GetSuggestedHardwareTypesInteractor."""
# Copyright (c) 2015, 2026 David Wilson
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

import abstract_persistence as ap
import HardwareType as h
import Interactors.Interactor as interactor
import Interactors.HardwareInteractors as hi

class TestGetSuggestedHardwareTypesInteractor(unittest.TestCase):
    """Unit tests for GetSuggestedHardwareTypesInteractor."""

    def setUp(self):

        def get_hardware_type(name):
            return h.HardwareType.from_dict({"name": name})

        def setup_persistence():
            """Sets up a mock persistence with one stored hardware type."""
            stored_hardware_types = [get_hardware_type("type1")]
            persistence = Mock(ap.AbstractPersistence)
            persistence.get_hardware_types_list = Mock(return_value=stored_hardware_types)
            return persistence

        self.__suggested_hardware_types = [get_hardware_type("type1"), get_hardware_type("type2")]

        def get_suggested_hardware_types():
            return self.__suggested_hardware_types

        self.__target = hi.GetSuggestedHardwareTypesInteractor(get_suggested_hardware_types)
        self.__target.persistence = setup_persistence()

    def test_is_instance_of_interactor(self):
        """Tests that the interactor is an instance of Interactor."""
        self.assertIsInstance(self.__target, interactor.Interactor)

    def test_execute_only_returns_hardware_types_not_stored(self):
        """Tests that Execute only returns hardware types that are not already stored."""
        hardware_types = self.__target.execute()
        self.assertEqual(1, len(hardware_types))

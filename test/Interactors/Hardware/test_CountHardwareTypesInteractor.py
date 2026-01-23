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
import Interactors.HardwareInteractors as hi
import Interactors.Interactor as interactor


class TestCountHardwareTypesInteractor(unittest.TestCase):
    """Unit tests for the CountHardwareTypesInteractor class"""

    def setUp(self):
        """setUp for all tests in this class"""
        self.__persistence = Mock(ap.AbstractPersistence)
        self.__target = hi.CountHardwareTypesInteractor()
        self.__target.persistence = self.__persistence
    
    def test_is_instance_of_interactor(self):
        """Test that CountHardwareTypesInteractor is a subclass of Interactor"""
        self.assertIsInstance(self.__target, interactor.Interactor)

    def test_execute_calls_persistence_method(self):
        """Test that CountHardwareTypesInteractor.execute causes persistence.count_hardware_types to be called"""
        self.__target.execute()
        self.__persistence.count_hardware_types.assert_called_with()

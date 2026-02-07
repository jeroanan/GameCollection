"""Unit tests for the CountHardwareInteractor class"""
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

from unittest.mock import Mock

from test.Interactors.interactor_test_base import InteractorTestBase
from abstract_persistence import AbstractPersistence
from Interactors.hardware_interactors import CountHardwareInteractor
from Interactors.interactor import Interactor


class TestCountHardwareInteractor(InteractorTestBase):
    """Unit tests for the CountHardwareInteractor class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        super().setUp()
        self.__target = CountHardwareInteractor()
        self.__persistence = Mock(AbstractPersistence)
        self.__target.persistence = self.__persistence

    def test_is_interactor(self):
        """Test that CountHardwareInteractor derives from Interactor"""
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        """Test that calling CountHardwareInteractor.execute causes persistence.count_hardware to 
        be called"""
        user_id = "user_id"
        self.__target.execute(user_id)
        self.__persistence.count_hardware.assert_called_with(user_id)

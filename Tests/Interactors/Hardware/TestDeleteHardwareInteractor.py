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

from Interactors.HardwareInteractors import DeleteHardwareInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestDeleteHardwareInteractor(InteractorTestBase):
    """Unit tests for the DeleteHardwareInteractor class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        super().setUp()
        self.__target = DeleteHardwareInteractor()
        self.__target.persistence = self.persistence
        self.__target.validate_string_field = self.validate_string_field
        self.__target.validate_integer_field = self.validate_integer_field

    def test_is_instance_of_interactor(self):
        """Test that DeleteHardwareInteractor derives from Interactor"""
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_with_none_hardware_id_raises_type_error(self):
        """Test that calling DeleteHardwareInteractor.execute with a null hardwareid causes a TypeError to be raised"""
        self.assertRaises(TypeError, self.__execute, None)

    def test_execute_validates_id_field(self):
        """Test that calling DeleteHardwareInteractor.execute causes the hardware id to be validated"""
        self.__execute("id")
        self.validate_string_field_was_called_with("Hardware Id", "id")

    def test_execute_calls_persistence_method(self):
        """Test that calling DeleteHardwareInteractor.execute causes persistence.delete_hardware to be called"""
        hardwareid = "hardwareid"
        user_id = "user_id"
        self.__execute(hardware_id=hardwareid, user_id=user_id)
        self.persistence.delete_hardware.assert_called_with(hardwareid, user_id)

    def __execute(self, hardware_id, user_id="userid"):
        self.__target.execute(hardware_id, user_id)

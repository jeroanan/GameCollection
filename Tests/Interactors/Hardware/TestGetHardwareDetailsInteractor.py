# Copyright (c) David Wilson 2015
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

from Interactors.HardwareInteractors import GetHardwareDetailsInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestGetHardwareDetailsInteractor(InteractorTestBase):
    """Unit tests for the GetHardwareDetailsInteractor class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        super().setUp()
        self.__target = GetHardwareDetailsInteractor()
        self.__target.persistence = self.persistence

    def test_is_instance_of_interactor(self):
        """Test that GetHardwareDetailsInteractor derives from Interactor"""
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_with_none_hardware_id_raises_type_error(self):
        """Test that calling GetHardwareDetailsInteractor.execute with a null hardware_id 
        causes a TypeError to be raised"""
        self.assertRaises(TypeError, self.__execute, None)

    def test_execute_calls_persistence_method(self):
        """Test that calling GetHardwareDetailsInteractor.execute 
        causes persistence.get_hardware_details to be called"""
        self.__execute(hardware_id="platformid", user_id="user_id")
        self.persistence.get_hardware_details.assert_called_with("platformid", "user_id")

    def __execute(self, hardware_id, user_id="userid"):
        self.__target.execute(hardware_id, user_id)

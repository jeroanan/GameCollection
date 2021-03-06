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

from Interactors.HardwareInteractors import GetHardwareListInteractor
from Interactors.Hardware.Params.GetHardwareListInteractorParams import GetHardwareListInteractorParams
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestGetHardwareListInteractor(InteractorTestBase):
    """Unit tests for the GetHardwareListInteractor class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        super().setUp()
        self.__target = GetHardwareListInteractor()
        self.__target.persistence = self.persistence

    def test_is_instance_of_interactor(self):
        """Test that GetHardwareListInteractor is an instance of Interactor"""
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_with_no_platform_calls_get_hardware_list_persistence_method(self):
        """Test that calling GetHardwareListInteractor.execute causes persistence.get_hardware_list to be called"""
        p = self.__get_params()
        p.platform = ""
        self.__target.execute(p)
        self.persistence.get_hardware_list.assert_called_with(p)

    def test_execute_with_platform_calls_get_hardware_list_for_platform_persistence_method(self):
        p = self.__get_params()
        self.__target.execute(p)
        self.persistence.get_hardware_list_for_platform.assert_called_with(p)


    def __get_params(self):
        return GetHardwareListInteractorParams.from_dict({
            "platform": "p",
            "sort_field": "name",
            "sort_direction": "asc",
            "user_id": "userid"})

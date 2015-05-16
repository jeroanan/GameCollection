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

from Interactors.Hardware.GetHardwareListInteractor import GetHardwareListInteractor
from Interactors.Hardware.Params.GetHardwareListInteractorParams import GetHardwareListInteractorParams
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestGetHardwareListInteractor(InteractorTestBase):

    def setUp(self):
        super().setUp()
        self.__target = GetHardwareListInteractor()
        self.__target.persistence = self.persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence(self):
        def get_params():
            p = GetHardwareListInteractorParams()
            p.sort_field = "name"
            p.sort_direction = "asc"
            p.user_id = "userid"
            return p

        self.__target.execute(get_params())
        self.persistence.get_hardware_list.assert_called_with(sort_field="name", sort_direction="asc", user_id="userid")

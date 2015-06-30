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

import unittest
from unittest.mock import Mock

import HardwareType as ht
import Interactors.HardwareInteractors as hi
import Interactors.InteractorFactory as factory
import UI.Handlers.AuthenticatedHandler as ah
import UI.Handlers.DeleteHardwareTypeHandler as handler
import UI.Handlers.Session.Session as session


class TestDeleteHardwareTypeHandler(unittest.TestCase):

    def setUp(self):
        interactor_factory = Mock(factory.InteractorFactory)
        self.__interactor = Mock(hi.DeleteHardwareTypeInteractor)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = handler.DeleteHardwareTypeHandler(interactor_factory, None)
        self.__target.session = Mock(session.Session)

    def test_is_instance_of_authenticated_handler(self):
        self.assertIsInstance(self.__target, ah.AuthenticatedHandler)

    def test_get_page_executes_delete_hardware_type_interactor(self):
        params = {"name": "n", "description": "desc"}
        hardware_type = ht.HardwareType.from_dict(params)
        self.__target.get_page(params)
        self.__interactor.execute.assert_called_with(hardware_type)

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

import HardwareType as ht
import Interactors.InteractorFactory as factory
import Interactors.HardwareInteractors as hi
import UI.Handlers.AuthenticatedHandler as ah
import UI.Handlers.Session.Session as session
import UI.Handlers.UpdateHardwareTypeHandler as handler


class TestUpdateHardwareTypeHandler(unittest.TestCase):

    def setUp(self):
        self.__interactor_factory = Mock(factory.InteractorFactory)
        self.__interactor = Mock(hi.UpdateHardwareTypeInteractor)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = handler.UpdateHardwareTypeHandler(self.__interactor_factory, None)
        self.__target.session = Mock(session.Session)
    
    def test_is_instance_of_authenticated_handler(self):
        self.assertIsInstance(self.__target, ah.AuthenticatedHandler)

    def test_get_page(self):
        self.__target.get_page({"":""})

    def test_get_page_creates_update_hardware_type_interactor(self):
        self.__target.get_page({"":""})
        self.__interactor_factory.create.assert_called_with("UpdateHardwareTypeInteractor")

    def test_get_page_executes_update_hardware_type_interactor(self):
        params = {"name": "n", "description": "d"}
        hardware_type = ht.HardwareType.from_dict(params)
        self.__target.get_page(params)
        self.__interactor.execute.assert_called_with(hardware_type)
        

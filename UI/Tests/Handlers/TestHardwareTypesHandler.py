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
import Interactors.InteractorFactory as interactor_factory
import Interactors.HardwareInteractors as hi
import UI.Handlers.AuthenticatedHandler as ah
import UI.Handlers.HardwareTypesHandler as hth
import UI.Handlers.Session.Session as session
import UI.TemplateRenderer as tr


class TestHardwareTypesHandler(unittest.TestCase):
    
    def setUp(self):
        self.__stored_hardware_types = [ht.HardwareType.from_dict({"name": "type1"})]
        self.__suggested_hardware_types = [ht.HardwareType.from_dict({"name": "type2"})]

        def get_hardware_type_list_interactor():
            interactor = Mock(hi.GetHardwareTypeListInteractor)
            interactor.execute = Mock(return_value=self.__stored_hardware_types)
            return interactor

        def get_suggested_hardware_types_interactor():
            interactor = Mock(hi.GetSuggestedHardwareTypesInteractor)
            interactor.execute = Mock(return_value=self.__suggested_hardware_types)
            return interactor

        get_hardware_type_list_interactor = get_hardware_type_list_interactor()
        get_suggested_hardware_types_interactor = get_suggested_hardware_types_interactor()

        def create_interactor(interactor_type):
            interactors = {
                "GetHardwareTypeListInteractor": get_hardware_type_list_interactor,
                "GetSuggestedHardwareTypesInteractor": get_suggested_hardware_types_interactor
            }
            return interactors[interactor_type]

        factory = Mock(interactor_factory.InteractorFactory)        
        factory.create = Mock(side_effect=create_interactor)
        self.__renderer = Mock(tr.TemplateRenderer)

        self.__target = hth.HardwareTypesHandler(factory, self.__renderer)
        self.__target.session = Mock(session.Session)        

    def test_is_instance_of_authenticated_handler(self):
        self.assertIsInstance(self.__target, ah.AuthenticatedHandler)

    def test_get_page_calls_renderer_correctly(self):
        self.__target.get_page({"":""})
        self.__renderer.render.assert_called_with("hardwaretypes.html", title="Manage Hardware Types",
                                                  hardware_types=self.__stored_hardware_types, 
                                                  suggested_hardware_types=self.__suggested_hardware_types)

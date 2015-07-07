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
    """Unit tests for the HardwareTypesHandler class"""
    
    def setUp(self):
        """setUp for all unit tests in this class"""
        self.__stored_hardware_types = [ht.HardwareType.from_dict({"name": "type1"})]
        self.__suggested_hardware_types = [ht.HardwareType.from_dict({"name": "type2"})]

        def create_interactor(interactor_type):
            """Mock for InteractorFactory.create"""
            interactor = None

            interactors = {
                "GetHardwareTypeListInteractor": (hi.GetHardwareTypeListInteractor, self.__stored_hardware_types),
                "GetSuggestedHardwareTypesInteractor": (hi.GetSuggestedHardwareTypesInteractor, self.__suggested_hardware_types)
            }

            if interactor_type in interactors:
                interactor_type, data = interactors[interactor_type]
                interactor = Mock(interactor_type)
                interactor.execute = Mock(return_value=data)

            return interactor

        factory = Mock(interactor_factory.InteractorFactory)        
        factory.create = Mock(side_effect=create_interactor)
        self.__renderer = Mock(tr.TemplateRenderer)

        self.__target = hth.HardwareTypesHandler(factory, self.__renderer)
        self.__target.session = Mock(session.Session)        

    def test_is_instance_of_authenticated_handler(self):
        """Test that HardwareTypesHandler is an instance of AuthenticatedHandler"""
        self.assertIsInstance(self.__target, ah.AuthenticatedHandler)

    def test_get_page_calls_renderer_correctly(self):
        """Test that calling HardwareTypesHandler.get_page causes TemplateRenderer.render to be called correctly"""    
        self.__target.get_page({"":""})
        self.__renderer.render.assert_called_with("hardwaretypes.html", title="Manage Hardware Types",
                                                  hardware_types=self.__stored_hardware_types, 
                                                  suggested_hardware_types=self.__suggested_hardware_types)

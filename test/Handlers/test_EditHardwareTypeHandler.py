# Copyright (c) 20115 David Wilson
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
import UI.Handlers.EditHardwareTypeHandler as ehth
import UI.Handlers.Session.Session as session
import UI.TemplateRenderer as renderer


class TestEditHardwareTypeHandler(unittest.TestCase):
    
    def setUp(self):
        self.__params = {"name": "n", "description": "d"}
        self.__hardware_type = ht.HardwareType.from_dict(self.__params)
        interactor = Mock(hi.GetHardwareTypeInteractor)
        interactor.execute = Mock(return_value=self.__hardware_type)
        interactor_factory = Mock(factory.InteractorFactory)
        interactor_factory.create = Mock(return_value=interactor)
        self.__renderer = Mock(renderer.TemplateRenderer)
        self.__target = ehth.EditHardwareTypeHandler(interactor_factory, self.__renderer)
        self.__target.session = Mock(session.Session)

    def test_is_instance_of_authenticated_handler(self):
        self.assertIsInstance(self.__target, ah.AuthenticatedHandler)

    def test_get_page_calls_renderer_correctly(self):        
        self.__target.get_page(self.__params)
        self.__renderer.render.assert_called_with("edithardwaretype.html", title="Edit Hardware Type", 
                                                  hardware_type=self.__hardware_type)
        


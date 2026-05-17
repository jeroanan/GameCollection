"""Provides unit tests for the AddHardwareHandler class"""
# Copyright (c) David Wilson 2015, 2026
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

import interactors.hardware_interactors as hi
import interactors.interactor_factory as factory
import interactors.platform_interactors as pi
import hardware_type as ht
import icarus_platform as platform
import ui.Handlers.add_hardware_handler as ahh
import ui.Handlers.authenticated_handler as ah
import ui.Handlers.Session.Session as sess
import ui.template_renderer as renderer


class TestAddHardwareHandler(unittest.TestCase):
    """Unit tests for the AddHardwareHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""

        def interactor_factory_create(interactor_type):
            """Mock function for InteractorFactory.create"""

            interactors = {
                "GetPlatformsInteractor": (pi.GetPlatformsInteractor, self.__platforms), 
                "GetHardwareTypeListInteractor": (
                    hi.GetHardwareTypeListInteractor,
                    self.__hardware_types)}

            if interactor_type in interactors:
                interactor_class, data = interactors[interactor_type]
                interactor = Mock(interactor_class)
                interactor.execute = Mock(return_value=data)
                return interactor
            return None

        self.__platforms = [platform.Platform()]
        self.__hardware_types = [ht.HardwareType()]
        self.__renderer = Mock(renderer.TemplateRenderer)
        interactor_factory = Mock(factory.InteractorFactory)
        interactor_factory.create = Mock(side_effect=interactor_factory_create)
        self.__target = ahh.AddHardwareHandler(interactor_factory, self.__renderer)
        session = Mock(sess.Session)
        self.__target.session = session

    def test_is_instance_of_authenticated_handler(self):
        """Test that AddHardwareHandler is an instance of AuthenticatedHandler"""
        self.assertIsInstance(self.__target, ah.AuthenticatedHandler)

    def test_get_page_calls_renderer(self):
        """Test that calling AddHardwareHandler.get_page causes renderer.render to be called
        correctly"""
        self.__target.get_page({})
        self.__renderer.render.assert_called_with(
            "addhardware.html",
            title="Add Hardware",
            platforms=self.__platforms,
            hardware_types=self.__hardware_types)

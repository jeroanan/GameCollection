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

import Hardware as h
import HardwareType as ht
import Interactors.HardwareInteractors as hi
import Interactors.InteractorFactory as factory
import Interactors.PlatformInteractors as pi
import Platform as p
import UI.Handlers.AuthenticatedHandler as ah
import UI.Handlers.EditHardwareHandler as ehh
import UI.Handlers.Session.Session as sess
import UI.TemplateRenderer as renderer


class TestEditHardwareHandler(unittest.TestCase):
    """Unit tests for the EditHardwareHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class."""

        def interactor_factory_create(interactor_type):
            """Mock function for InteractorFactory.Create"""
            interactors = {"GetHardwareDetailsInteractor": (hi.GetHardwareDetailsInteractor, self.__hardware),
                           "GetPlatformsInteractor": (pi.GetPlatformsInteractor, self.__platforms),
                           "GetHardwareTypeListInteractor": (hi.GetHardwareTypeListInteractor, self.__hardware_types)}

            if interactor_type in interactors:
                interactor_type, data = interactors[interactor_type]
                interactor = Mock(interactor_type)
                interactor.execute = Mock(return_value=data)
                return interactor

        self.__hardware = h.Hardware()
        self.__platforms = [p.Platform()]
        self.__hardware_types = [ht.HardwareType()]

        interactor_factory = Mock(factory.InteractorFactory)
        interactor_factory.create = Mock(side_effect=interactor_factory_create)

        self.__renderer = Mock(renderer.TemplateRenderer)
        self.__target = ehh.EditHardwareHandler(interactor_factory, self.__renderer)
        self.__target.session = Mock(sess.Session)
        args = {"hardwareid": "hardwareid"}
        self.__get_page = lambda: self.__target.get_page(args)

    def test_is_instance_of_authenticated_handler(self):
        """Test that EditHardwareHandler derives from AuthenticatedHandler"""
        self.assertIsInstance(self.__target, ah.AuthenticatedHandler)

    def test_calls_renderer(self):
        """Test that calling EditHardwareHandler.get_page causes renderer.render to be called correctly"""
        self.__get_page()
        self.__renderer.render.assert_called_with("edithardware.html", title="Edit Hardware", hardware=self.__hardware,
                                                  platforms=self.__platforms, hardware_types=self.__hardware_types, 
                                                  hardware_found=True)




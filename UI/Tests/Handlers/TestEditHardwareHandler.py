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

from Hardware import Hardware
from Interactors.HardwareInteractors import GetHardwareDetailsInteractor
from Interactors.InteractorFactory import InteractorFactory
from Interactors.PlatformInteractors import GetPlatformsInteractor
from Platform import Platform
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.EditHardwareHandler import EditHardwareHandler
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.Session.Session import Session
from UI.TemplateRenderer import TemplateRenderer


class TestEditHardwareHandler(unittest.TestCase):
    """Unit tests for the EditHardwareHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class."""
        interactors = lambda: [get_hardware_details_interactor, get_platforms_interactor]
        self.__hardware = Hardware()
        self.__platforms = [Platform()]
        get_hardware_details_interactor = Mock(GetHardwareDetailsInteractor)
        get_hardware_details_interactor.execute = Mock(return_value=self.__hardware)
        get_platforms_interactor = Mock(GetPlatformsInteractor)
        get_platforms_interactor.execute = Mock(return_value=self.__platforms)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(side_effect=interactors())
        self.__renderer = Mock(TemplateRenderer)
        self.__target = EditHardwareHandler(interactor_factory, self.__renderer)
        self.__target.session = Mock(Session)
        args = {"hardwareid": "hardwareid"}
        self.__get_page = lambda: self.__target.get_page(args)

    def test_is_instance_of_authenticated_handler(self):
        """Test that EditHardwareHandler derives from AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_calls_renderer(self):
        """Test that calling EditHardwareHandler.get_page causes renderer.render to be called correctly"""
        self.__get_page()
        self.__renderer.render.assert_called_with("edithardware.html", title="Edit Hardware", hardware=self.__hardware, 
                                                  platforms=self.__platforms, hardware_found=True)




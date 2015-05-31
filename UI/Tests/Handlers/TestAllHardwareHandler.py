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
from Interactors.HardwareInteractors import GetHardwareListInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.AllHardwareHandler import AllHardwareHandler
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.Session.Session import Session
from UI.TemplateRenderer import TemplateRenderer


class TestAllHardwareHandler(unittest.TestCase):
    """Unit tests for the AllHardwareHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        interactor_factory = Mock(InteractorFactory)
        interactor = Mock(GetHardwareListInteractor())
        self.__hardware = [Hardware()]
        interactor.execute = Mock(return_value=self.__hardware)
        interactor_factory.create = Mock(return_value=interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = AllHardwareHandler(interactor_factory, self.__renderer)
        self.__target.session = Mock(Session)
        
    def test_is_instance_of_authethenticated_handler(self):
        """Test that AllHardwareHandler is an instance of AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_get_page_calls_renderer(self):
        """Test that calling AllHardwareHandler.get_page causes renderer.render to be called correctly."""
        self.__target.get_page({"": ""})
        self.__renderer.render.assert_called_with("allhardware.html",
                                                  hardware=self.__hardware, title="All Hardware",
                                                  hw_sort_field="name", hw_sort_dir="asc")


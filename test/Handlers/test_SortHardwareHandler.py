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

from Hardware import Hardware
from Interactors.HardwareInteractors import GetHardwareListInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.Session.Session import Session
from UI.Handlers.SortHardwareHandler import SortHardwareHandler
from UI.TemplateRenderer import TemplateRenderer


class TestSortHardwareHandler(unittest.TestCase):
    """Unit tests for the SortHardwareHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        self.__hardware = [Hardware()]
        interactor = Mock(GetHardwareListInteractor)
        interactor.execute = Mock(return_value=self.__hardware)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = SortHardwareHandler(interactor_factory, self.__renderer)
        self.__target.session = Mock(Session)

    def test_is_authenticated_handler(self):
        """Test that SortHardwareHandler is an instance of AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_executes_renderer(self):
        """Test that calling SortHardwareHandler.get_page causes renderer.render to be called correctly"""
        args = {"field": "title", "sortdir": "asc", "numrows": 2}
        self.__target.get_page(args)
        self.__renderer.render.assert_called_with("hardware.html", hardware=self.__hardware,
                                                  hw_sort_field=args["field"], hw_sort_dir=args["sortdir"])

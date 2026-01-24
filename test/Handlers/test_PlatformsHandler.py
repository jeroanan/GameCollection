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

from Interactors.PlatformInteractors import GetPlatformsInteractor, GetSuggestedPlatformsInteractor
from Interactors.InteractorFactory import InteractorFactory
from Platform import Platform
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.PlatformsHandler import PlatformsHandler
from UI.Handlers.Session.Session import Session
from UI.TemplateRenderer import TemplateRenderer


class TestPlatformsHandler(unittest.TestCase):
    """Unit tests for the PlatformsHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""

        def interactor_factory_create():
            return [get_platforms_interactor, get_suggested_platforms_interactor]

        self.__platforms = [Platform()]
        self.__suggested_platforms = [Platform(), Platform()]
        get_platforms_interactor = Mock(GetPlatformsInteractor)
        get_platforms_interactor.execute = Mock(return_value=self.__platforms)
        get_suggested_platforms_interactor = Mock(GetSuggestedPlatformsInteractor)
        get_suggested_platforms_interactor.execute = Mock(return_value=self.__suggested_platforms)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(side_effect=interactor_factory_create())
        self.__renderer = Mock(TemplateRenderer)
        self.__target = PlatformsHandler(interactor_factory, self.__renderer)
        session = Mock(Session)
        self.__target.session = session

    def test_is_instance_of_authenticated_handler(self):
        """Test that PlatformsHandler is an instance of AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_get_page_calls_renderer(self):
        """Test that calling PlatformsHandler.get_page causes renderer.render to be called correctly"""
        self.__target.get_page({})
        self.__renderer.render.assert_called_with("platforms.html", title="Manage Platforms", 
                                                  platforms=self.__platforms, 
                                                  suggested_platforms=self.__suggested_platforms)
        


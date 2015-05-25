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

from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.EditUserHandler import EditUserHandler
from UI.Handlers.Session.Session import Session
from Interactors.InteractorFactory import InteractorFactory
from Interactors.User.GetUserInteractor import GetUserInteractor
from UI.TemplateRenderer import TemplateRenderer
from User import User


class TestEditUserHandler(unittest.TestCase):
    """Unit tests for the EditUserHandler class"""

    def setUp(self):
        """setUp function for unit tests in this class"""
        params = {"id": "id"}
        self.__user = User.from_dict(params)
        interactor_factory = Mock(InteractorFactory)
        interactor = Mock(GetUserInteractor)
        interactor.execute = Mock(return_value=self.__user)
        interactor_factory.create = Mock(return_value=interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = EditUserHandler(interactor_factory, self.__renderer)
        self.__target.session = Mock(Session)
        self.__get_page = lambda: self.__target.get_page(params)

    def test_is_type_of_handler(self):
        """Test that EditUserHandler is derived from AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_get_page_calls_renderer(self):
        """Test that EditUserHandler correctly renders a webpage for the requested user"""
        self.__get_page()
        self.__renderer.render.assert_called_with("edituser.html", title="Edit User", user=self.__user)
        

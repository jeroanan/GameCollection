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

from Interactors.InteractorFactory import InteractorFactory
from Interactors.User.GetUsersInteractor import GetUsersInteractor
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.Session.Session import Session
from UI.Handlers.UsersHandler import UsersHandler
from UI.TemplateRenderer import TemplateRenderer
from User import User


class TestUsersHandler(unittest.TestCase):

    def setUp(self):
        self.__users = [User()]
        interactor = Mock(GetUsersInteractor)
        interactor.execute = Mock(return_value=self.__users)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = UsersHandler(interactor_factory, self.__renderer)
        self.__target.session = Mock(Session)
            
    def test_is_instance_of_authenticated_handler(self):
        """Test that UsersHandler is derived from AuthenticatedHandler."""        
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_get_page_renders_template(self):
        """Test that executing UsersHandler returns a rendered page with the correct parameters"""
        self.__target.get_page(None)
        self.__renderer.render.assert_called_with("users.html", title="User Management", users=self.__users)

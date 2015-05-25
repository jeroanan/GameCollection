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
from Interactors.InteractorFactory import InteractorFactory
from Interactors.User.UpdateUserInteractor import UpdateUserInteractor
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.Session.Session import Session
from UI.Handlers.UpdateUserHandler import UpdateUserHandler
from User import User


class TestUpdateUserHandler(unittest.TestCase):
    
    def setUp(self):
        self.__interactor = Mock(UpdateUserInteractor)
        interactor_factory = Mock(InteractorFactory)        
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = UpdateUserHandler(interactor_factory, None)
        self.__target.session = Mock(Session)
        params = {"id": "id"}
        self.__user = User.from_dict(params)
        self.__get_page = lambda: self.__target.get_page(params)

    def test_is_instance_of_authenticated_handler(self):
        """Test that UpdateUserHandler is derived from AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_executes_interactor(self):
        """Test that UpdateUserHandler calls UpdateUserInteractor.execute"""
        self.__get_page()
        self.__interactor.execute.assert_called_with(self.__user)

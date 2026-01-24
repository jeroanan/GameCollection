# Copyright (C) 2015 David Wilson
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
from Interactors.UserInteractors import ChangePasswordInteractor
from UI.Handlers.ChangePasswordHandler import ChangePasswordHandler
from UI.Handlers.Handler import Handler
from User import User        

class TestChangePasswordHandler(unittest.TestCase):
    """Unit tests for the ChangePasswordHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(ChangePasswordInteractor)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = ChangePasswordHandler(interactor_factory, None)
    
    def test_is_handler(self):
        """Test that ChangePasswordHandler is an instance of Handler"""
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_missing_required_param_raises_value_error(self):
        """Test that calling ChangePasswordHandler.get_page with missing required parameters raises a ValueError"""
        required_params = ["user_id", "password"]
        for rp in required_params:
            p = self.__get_params()
            del p[rp]
            self.assertRaises(ValueError, self.__target.get_page, p)

    def test_get_page_empty_required_params_raises_value_error(self):
        """Test that calling ChangePasswordHandler.get_page with empty required parameters raises a ValueError"""
        required_params = ["user_id", "password"]
        for rp in required_params:
            p = self.__get_params()
            p[rp] = ""
            self.assertRaises(ValueError, self.__target.get_page, p)

    def test_get_page_executes_interactor(self):
        """Test that caling ChangePasswordHandler.get_page correctly causes ChangePasswordInteractor.execute to be
        called"""
        self.__target.get_page(self.__get_params())
        self.__interactor.execute.assert_called_with(self.__get_user())

    def __get_params(self):
        return {"user_id": "user",
                "password": "password"}

    def __get_user(self):
        p = self.__get_params()
        u = User()
        u.user_id = p["user_id"]
        u.password = ["password"]
        return u
        

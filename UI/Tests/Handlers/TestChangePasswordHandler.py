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

from Interactors.User.ChangePasswordInteractor import ChangePasswordInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.ChangePasswordHandler import ChangePasswordHandler
from UI.Handlers.Handler import Handler
from User import User        

class TestChangePasswordHandler(unittest.TestCase):

    def setUp(self):
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(ChangePasswordInteractor)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = ChangePasswordHandler(self.__interactor_factory, None)
    
    def test_is_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_none_params_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.get_page, None)

    def test_get_page_none_user_id_raises_value_error(self):
        self.__assert_missing_param_raises_value_error("user_id")

    def test_get_page_empty_user_id_raises_value_error(self):
        p = self.__get_params()
        p["user_id"] = ""
        self.assertRaises(ValueError, self.__target.get_page, p)

    def test_get_page_none_password_raises_value_error(self):
        self.__assert_missing_param_raises_value_error("password")

    def test_get_page_empty_password_raises_value_error(self):
        p = self.__get_params()
        p["password"] = ""
        self.assertRaises(ValueError, self.__target.get_page, p)
        
    def __assert_missing_param_raises_value_error(self, param_key):
        p = self.__get_params()
        del p[param_key]
        self.assertRaises(ValueError, self.__target.get_page, p)

    def test_get_page_creates_interactor(self):
        self.__target.get_page(self.__get_params())
        self.__interactor_factory.create.assert_called_with("ChangePasswordInteractor")

    def test_get_page_executes_interactor(self):
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
        

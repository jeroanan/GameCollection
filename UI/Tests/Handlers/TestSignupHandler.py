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
from Interactors.Exceptions.UserExistsException import UserExistsException
from Interactors.InteractorFactory import InteractorFactory
from Interactors.User.AddUserInteractor import AddUserInteractor
from Interactors.User.GetUserInteractor import GetUserInteractor
from Interactors.User.LoginInteractor import LoginInteractor
from UI.Cookies.Cookies import Cookies
from UI.Handlers.Handler import Handler
from UI.Handlers.Exceptions.CookiesNotSetException import CookiesNotSetException
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.Session.Session import Session
from UI.Handlers.SignupHandler import SignupHandler
from User import User


class TestSignupHandler(unittest.TestCase):

    def setUp(self):
        self.__add_user_interactor = Mock(AddUserInteractor)
        self.__add_user_interactor.execute = Mock(side_effect=self.__interactor_execute)
        self.__login_interactor = Mock(LoginInteractor)
        self.__get_user_interactor = Mock(GetUserInteractor)
        get_user = lambda u: User.from_dict({"id": "1234"})
        self.__get_user_interactor.execute = Mock(side_effect=get_user)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(side_effect=self.__interactor_factory_create)
        self.__session = Mock(Session)
        self.__cookies = Mock(Cookies)
        self.__target = SignupHandler(interactor_factory, None)
        self.__target.session = self.__session
        self.__target.cookies = self.__cookies

    def __interactor_factory_create(self, interactor_type):
        interactors = {"AddUserInteractor": self.__add_user_interactor,
                       "LoginInteractor": self.__login_interactor,
                       "GetUserInteractor": self.__get_user_interactor}
        return interactors.get(interactor_type, None)

    def __interactor_execute(self, user):
        if user.user_id == "alreadyexists":
            raise UserExistsException

    def test_is_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_successful_signup_sets_hash_provider(self):
        self.__target.get_page(self.__get_params())
        self.assertTrue(self.__add_user_interactor.set_hash_provider.called)

    def test_successful_signup_executes_add_user_interactor(self):
        params = self.__get_params()
        user = self.__get_user(params["userid"], params["password"])
        self.__target.get_page(params)
        self.__add_user_interactor.execute.assert_called_with(user)

    def test_successful_signup_executes_login_interactor(self):
        params = self.__get_params()
        user = self.__get_user(params["userid"], params["password"])
        self.__target.get_page(params)
        self.__login_interactor.execute.assert_called_with(user)

    def test_successful_signup_executes_get_user_interactor(self):
        params = self.__get_params()
        user = self.__get_user(params["userid"], params["password"])
        self.__target.get_page(params)
        self.__get_user_interactor.execute.assert_called_with(user)

    def test_successful_signup_sets_login_session(self):
        params = self.__get_params()                
        user = self.__get_user(params["userid"], params["password"])
        self.__target.get_page(params)
        self.__session.set_value.assert_called_with("user_id", "1234")    
    
    def test_successful_signup_sets_session_status_cookie(self):
        params = self.__get_params()
        self.__target.get_page(params)
        self.__cookies.set_cookie.assert_any_call("session_status", "1")

    def test_successful_signup_sets_user_id_cookie(self):
        params = self.__get_params()
        self.__target.get_page(params)
        self.__cookies.set_cookie.assert_any_call("user_id", params["userid"])

    def test_user_exists_returns_true(self):
        result = self.__target.get_page(self.__get_params("alreadyexists"))
        self.assertTrue(result)

    def test_user_does_not_exist_returns_true(self):
        result = self.__target.get_page(self.__get_params())
        self.assertTrue(result)

    def test_session_not_set_raises_session_not_set_exception(self):
        self.__target.session = None
        self.assertRaises(SessionNotSetException, self.__target.get_page, self.__get_params())        

    def test_cookies_not_set_raises_cookies_not_set_exception(self):
        self.__target.cookies = None
        self.assertRaises(CookiesNotSetException, self.__target.get_page, self.__get_params())

    def test_no_user_id_returns_failed_signup(self):
        result = self.__target.get_page({})
        self.assertEqual("False", result)        

    def test_no_password_returns_failed_signup(self):
        params = self.__get_params()
        del params["password"]
        result = self.__target.get_page(params)
        self.assertEqual("False", result)

    def __get_params(self, userid="user", password="password"):
        return {
            "userid": userid,
            "password": password
        }

    def __get_user(self, userid, password):
        ud = {"userid": userid,
              "password": password}
        return User.from_dict(ud)

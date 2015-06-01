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

from Cryptography.HashProvider import HashProvider
from Interactors.InteractorFactory import InteractorFactory
from Interactors.UserInteractors import GetUserInteractor, LoginInteractor
from UI.Cookies.Cookies import Cookies
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.Exceptions.CookiesNotSetException import CookiesNotSetException
from UI.Handlers.Handler import Handler
from UI.Handlers.Session.Session import Session
from UI.Handlers.SigninHandler import SigninHandler
from User import User


class TestSigninHandler(unittest.TestCase):
    """Unit tests for the SigninHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        get_user = lambda u: User.from_dict({"id": "1234",
                                             "userid": u.user_id})
        self.__login_interactor = Mock(LoginInteractor)
        self.__login_interactor_execute = lambda u: u.user_id == "validuser"
        self.__login_interactor.execute = Mock(side_effect=self.__login_interactor_execute)
        self.__get_user_interactor = Mock(GetUserInteractor)
        self.__get_user_interactor.execute = Mock(side_effect=get_user)
        self.__hash_provider = Mock(HashProvider)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(side_effect=self.__interactor_factory_create)
        self.__session = Mock(Session)
        self.__target = SigninHandler(interactor_factory, None)
        self.__target.session = self.__session
        self.__cookies = Mock(Cookies)
        self.__target.cookies = self.__cookies

    def __interactor_factory_create(self, interactor_type):
        interactors = {"LoginInteractor": self.__login_interactor,
                       "GetUserInteractor": self.__get_user_interactor}
        return interactors.get(interactor_type, None)

    def test_is_handler(self):
        """Test that SigninHandler is an instance of Handler"""
        self.assertIsInstance(self.__target, Handler)

    def test_sets_interactor_hash_provider(self):
        """Test that calling SigninHandler.get_page causes LoginInteractor.set_hash_provider to be called"""
        self.__target.get_page(self.__get_params())
        self.assertTrue(self.__login_interactor.set_hash_provider.called)
    
    def test_executes_interactor(self):
        """Test that calling SigninHandler.get_page causes LoginInteractor.execute to be called"""
        self.__target.get_page(self.__get_params())
        self.__login_interactor.execute.assert_called_with(self.__get_user())

    def test_login_successful_sets_session(self):
        """Test that calling SigninHandler.get_page causes session.user_id to be set"""
        user_id = "validuser"
        u = self.__get_user(user_id)
        self.__target.get_page(self.__get_params(user_id))
        self.__session.set_value.assert_called_with("user_id", "1234")

    def test_login_successful_sets_cookies(self):
        """Test that calling SigninHandler.get_page causes cookies to be set correctly"""
        u = self.__get_user(user_id="validuser")
        cookies = {"session_status": "1",
                   "user_id": u.user_id}
        self.__target.get_page(self.__get_params(u.user_id))
        for c in cookies:
            self.__cookies.set_cookie.assert_any_call(c, cookies[c])

    def test_login_successful_excutes_get_user_interactor(self):
        """Test that calling SigninHandler.get_page causes GetUserInteractor.execute to be called"""
        user_id = "validuser"
        u = self.__get_user(user_id)
        self.__target.get_page(self.__get_params(user_id))
        self.__get_user_interactor.execute.assert_called_with(u)

    def test_no_session_set_raises_session_not_set_exception(self):
        """Test that calling SigninHandler.get_page without setting session raises SessionNotSetException"""
        self.__target.session = None
        self.assertRaises(SessionNotSetException, self.__target.get_page, self.__get_params())
        
    def test_no_cookies_set_raises_cookies_not_set_exception(self):
        """Test that calling SigninHandler.get_page without setting cookies raises CookiesNotSetException"""
        self.__target.cookies = None
        self.assertRaises(CookiesNotSetException, self.__target.get_page, self.__get_params())

    def test_get_page_missing_required_param_returns_false(self):        
        """Test that calling SigninHandler.get_page with missing required parameters returns 'False'"""
        required_params = ["userid", "password"]
        for rp in required_params:
            params = self.__get_params()
            del params[rp]
            self.assertEqual("False", self.__target.get_page(params))

    def __get_params(self, user_id="userid"):
        return {
            "userid": user_id,
            "password": "password"
            }

    def __get_user(self, user_id="userid"):
        return User.from_dict({"userid": user_id,
                               "password": "password"})

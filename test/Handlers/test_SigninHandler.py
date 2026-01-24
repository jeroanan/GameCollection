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

import json
import unittest
from unittest.mock import Mock

import Cryptography.HashProvider as hp
import Interactors.InteractorFactory as factory
import Interactors.UserInteractors as ui
import UI.Cookies.Cookies as cookies
import UI.Handlers.Handler as handler
import UI.Handlers.Session.Session as session
import UI.Handlers.SigninHandler as sh
import User as user


class TestSigninHandler(unittest.TestCase):
    """Unit tests for the SigninHandler class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        get_user = lambda u: user.User.from_dict({"id": "1234",
                                             "userid": u.user_id})


        def get_interactor(interactor_type, execute_effect):
            interactor = Mock(interactor_type)
            interactor.execute = Mock(side_effect=execute_effect)
            return interactor

        def setup_login_interactor():
            interactor_execute = lambda u: u.user_id == "validuser"
            return get_interactor(ui.LoginInteractor, interactor_execute)
            
        setup_get_user_interactor = lambda: get_interactor(ui.GetUserInteractor, get_user)

        def setup_interactor_factory():
            f = Mock(factory.InteractorFactory)
            f.create = Mock(side_effect=self.__interactor_factory_create)
            return f

        self.__login_interactor = setup_login_interactor()
        self.__get_user_interactor = setup_get_user_interactor()
        interactor_factory = setup_interactor_factory()

        self.__hash_provider = Mock(hp.HashProvider)
        self.__interactor_factory = setup_interactor_factory()
        self.__session = Mock(session.Session)
        self.__target = sh.SigninHandler(interactor_factory, None)
        self.__target.session = self.__session
        self.__cookies = Mock(cookies.Cookies)
        self.__target.cookies = self.__cookies

    def __interactor_factory_create(self, interactor_type):
        interactors = {"LoginInteractor": self.__login_interactor,
                       "GetUserInteractor": self.__get_user_interactor}
        return interactors.get(interactor_type, None)

    def test_is_handler(self):
        """Test that SigninHandler is an instance of Handler"""
        self.assertIsInstance(self.__target, handler.Handler)

    def test_sets_interactor_hash_provider(self):
        """Test that calling SigninHandler.get_page causes LoginInteractor.set_hash_provider to be called"""
        self.__target.get_page(self.__get_params())
        self.assertTrue(self.__login_interactor.set_hash_provider.called)
    
    def test_executes_interactor(self):
        """Test that calling SigninHandler.get_page causes LoginInteractor.execute to be called"""
        self.__target.get_page(self.__get_params())
        self.__login_interactor.execute.assert_called_with(self.__get_user())

    def test_login_successful_sets_session(self):
        """Test that a successful sign-in causes session.user_id to be set"""

        self.__successful_login()
        self.__session.set_value.assert_called_with("user_id", "1234")

    def test_login_successful_sets_cookies(self):
        """Test that a successful sign-in causes cookies to be set correctly"""

        u = self.__successful_login()['user']

        cookies = {"session_status": "1",
                   "user_id": u.user_id}

        for c in cookies:
            self.__cookies.set_cookie.assert_any_call(c, cookies[c])

    def test_login_successful_excutes_get_user_interactor(self):
        """Test that a successful sign-in causes GetUserInteractor.execute to be called"""

        u = self.__successful_login()['user']
        self.__get_user_interactor.execute.assert_called_with(u)

    def test_login_successful_returns_ok_json(self):
        """Test that a successful sign-in returns a successful sign-in json object"""

        j = json.dumps({'result': 'ok', 'message': 'success'})
        result = self.__successful_login()['result']
        self.assertEqual(j, result)

    def test_unsuccessful_login_returns_failed_json(self):
        """Test that an unsuccessful sign-in returns a failed json object"""

        j = json.dumps({'result': 'failed', 'message': 'invalid'})
        result = self.__unsuccessful_login()['result']
        self.assertEqual(j, result)

    def __login(self, user_id):
        u = self.__get_user(user_id)
        result = self.__target.get_page(self.__get_params(u.user_id))
        return {'user': u, 'result': result}

    def __successful_login(self):
        return self.__login('validuser')

    def __unsuccessful_login(self):
        return self.__login('invaliduser')        

    def test_missing_required_param_returns_failed_json(self):
        j = json.dumps({'result': 'failed', 'message' : 'failed_validation'});
        required_params = ['userid', 'password']

        for rp in required_params:
            params = self.__get_params()
            del params[rp]
            self.assertEqual(j, self.__target.get_page(params))

    def test_empty_required_param_returns_failed_json(self):
        j = json.dumps({'result': 'failed', 'message' : 'failed_validation'});
        required_params = ['userid', 'password']

        for rp in required_params:
            params = self.__get_params()
            params[rp] = ''
            self.assertEqual(j, self.__target.get_page(params))

    def __get_params(self, user_id="userid"):
        return {
            "userid": user_id,
            "password": "password"
            }

    def __get_user(self, user_id="userid"):
        return user.User.from_dict({"userid": user_id,
                                    "password": "password"})

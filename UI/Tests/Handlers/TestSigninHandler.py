import unittest
from unittest.mock import Mock

from Cryptography.HashProvider import HashProvider
from Interactors.InteractorFactory import InteractorFactory
from Interactors.User.GetUserInteractor import GetUserInteractor
from Interactors.User.LoginInteractor import LoginInteractor
from UI.Cookies.Cookies import Cookies
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.Exceptions.CookiesNotSetException import CookiesNotSetException
from UI.Handlers.Handler import Handler
from UI.Handlers.Session.Session import Session
from UI.Handlers.SigninHandler import SigninHandler
from User import User


class TestSigninHandler(unittest.TestCase):
    
    def setUp(self):
        def get_user(u):
            user = User()
            user.id = "1234"        
            user.user_id = u.user_id
            return user

        self.__interactor = Mock(LoginInteractor)
        self.__interactor.execute = Mock(side_effect=self.__interactor_execute)
        self.__get_user_interactor = Mock(GetUserInteractor)
        self.__get_user_interactor.execute = Mock(side_effect=get_user)
        self.__hash_provider = Mock(HashProvider)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor_factory.create = Mock(side_effect=self.__interactor_factory_create)
        self.__session = Mock(Session)
        self.__target = SigninHandler(self.__interactor_factory, None)
        self.__target.session = self.__session
        self.__cookies = Mock(Cookies)
        self.__target.cookies = self.__cookies

    def __interactor_execute(self, user):
        if user.user_id == "validuser":
            return True
        return False

    def __interactor_factory_create(self, interactor_type):
        if interactor_type == "LoginInteractor":
            return self.__interactor
        if interactor_type == "GetUserInteractor":
            return self.__get_user_interactor

    def test_is_session_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_sets_interactor_hash_provider(self):
        self.__target.get_page(self.__get_params())
        self.assertTrue(self.__interactor.set_hash_provider.called)
    
    def test_executes_interactor(self):
        self.__target.get_page(self.__get_params())
        self.__interactor.execute.assert_called_with(self.__get_user())

    def test_login_successful_sets_session(self):
        user_id = "validuser"
        u = self.__get_user(user_id)
        self.__target.get_page(self.__get_params(user_id))
        self.__session.set_value.assert_called_with("user_id", "1234")

    def test_login_successful_sets_cookie(self):
        user_id = "validuser"
        self.__target.get_page(self.__get_params(user_id))
        self.__cookies.set_cookie.assert_any_call("session_status", "1")

    def test_login_successful_sets_user_id_cookie(self):
        user_id = "validuser"
        u = self.__get_user(user_id)
        self.__target.get_page(self.__get_params(user_id))
        self.__cookies.set_cookie.assert_any_call("user_id", u.user_id)

    def test_login_successful_excutes_get_user_interactor(self):
        user_id = "validuser"
        u = self.__get_user(user_id)
        self.__target.get_page(self.__get_params(user_id))
        self.__get_user_interactor.execute.assert_called_with(u)

    def test_no_session_set_raises_session_not_set_exception(self):
        self.__target.session = None
        self.assertRaises(SessionNotSetException, self.__target.get_page, self.__get_params())
        
    def test_no_cookies_set_raises_cookies_not_set_exception(self):
        self.__target.cookies = None
        self.assertRaises(CookiesNotSetException, self.__target.get_page, self.__get_params())

    def test_get_page_no_user_id_returns_failed_signin(self):
        result = self.__target.get_page({})
        self.assertEqual("False", result)

    def test_get_page_no_password_returns_failed_signin(self):
        params = self.__get_params()
        del params["password"]
        result = self.__target.get_page(params)
        self.assertEqual("False", result)

    def __get_params(self, user_id="userid"):
        return {
            "userid": user_id,
            "password": "password"
            }

    def __get_user(self, user_id="userid"):
        u = User()
        u.user_id = user_id
        u.password = "password"
        return u

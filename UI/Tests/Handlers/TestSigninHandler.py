import unittest
from unittest.mock import Mock

from Cryptography.HashProvider import HashProvider
from Interactors.InteractorFactory import InteractorFactory
from Interactors.User.LoginInteractor import LoginInteractor
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.Handler import Handler
from UI.Handlers.Session.Session import Session
from UI.Handlers.SigninHandler import SigninHandler
from User import User


class TestSigninHandler(unittest.TestCase):
    
    def setUp(self):
        self.__interactor = Mock(LoginInteractor)
        self.__interactor.execute = Mock(side_effect=self.__interactor_execute)
        self.__hash_provider = Mock(HashProvider)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor_factory.create = Mock(side_effect=self.__interactor_factory_create)
        self.__session = Mock(Session)
        self.__target = SigninHandler(self.__interactor_factory, None)
        self.__target.session = self.__session

    def __interactor_execute(self, user):
        if user.user_id == "validuser":
            return True
        return False

    def __interactor_factory_create(self, interactor_type):
        if interactor_type == "LoginInteractor":
            return self.__interactor

    def test_is_session_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_sets_interactor_hash_provider(self):
        self.__target.get_page(self.__get_params())
        self.assertTrue(self.__interactor.set_hash_provider.called)
    
    def test_get_page_executes_interactor(self):
        self.__target.get_page(self.__get_params())
        self.__interactor.execute.assert_called_with(self.__get_user())

    def test_login_successful_sets_session(self):
        user_id = "validuser"
        self.__target.get_page(self.__get_params(user_id))
        self.__session.set_value.assert_called_with("user_id", user_id)

    def test_no_session_set_raises_session_not_found_exception(self):
        target = SigninHandler(Mock(InteractorFactory), None)
        self.assertRaises(SessionNotSetException, target.get_page, self.__get_params())

    def __get_params(self, user_id="userid"):
        return {
            "userid": user_id,
            "password": "password"
            }

    def __get_user(self):
        u = User()
        u.user_id = "userid"
        u.password = "password"
        return u

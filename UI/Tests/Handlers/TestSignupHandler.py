import unittest
from unittest.mock import Mock
from Interactors.Exceptions.UserExistsException import UserExistsException
from Interactors.InteractorFactory import InteractorFactory
from Interactors.User.AddUserInteractor import AddUserInteractor
from Interactors.User.LoginInteractor import LoginInteractor
from UI.Handlers.Handler import Handler
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.Session.Session import Session
from UI.Handlers.SignupHandler import SignupHandler
from User import User


class TestSignupHandler(unittest.TestCase):

    def setUp(self):
        self.__add_user_interactor = Mock(AddUserInteractor)
        self.__add_user_interactor.execute = Mock(side_effect=self.__interactor_execute)
        self.__login_interactor = Mock(LoginInteractor)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor_factory.create = Mock(side_effect=self.__interactor_factory_create)
        self.__session = Mock(Session)
        self.__target = SignupHandler(self.__interactor_factory, None)
        self.__target.session = self.__session

    def __interactor_factory_create(self, interactor_type):
        if interactor_type == "AddUserInteractor":
            return self.__add_user_interactor
        if interactor_type == "LoginInteractor":
            return self.__login_interactor

    def __interactor_execute(self, user):
        if user.user_id == "alreadyexists":
            raise UserExistsException

    def test_is_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_create_page_sets_hash_provider(self):
        self.__target.get_page(self.__get_params())
        self.assertTrue(self.__add_user_interactor.set_hash_provider.called)

    def test_get_create_page_executes_add_user_interactor(self):
        params = self.__get_params()
        user = self.__get_user(params["userid"], params["password"])
        self.__target.get_page(params)
        self.__add_user_interactor.execute.assert_called_with(user)

    def test_get_page_executes_login_interactor(self):
        params = self.__get_params()
        user = self.__get_user(params["userid"], params["password"])
        self.__target.get_page(params)
        self.__login_interactor.execute.assert_called_with(user)

    def test_get_page_sets_login_session(self):
        params = self.__get_params()                
        user = self.__get_user(params["userid"], params["password"])
        self.__target.get_page(params)
        self.__session.set_value.assert_called_with("user_id", user.user_id)    

    def test_get_page_user_exists_returns_true(self):
        result = self.__target.get_page(self.__get_params("alreadyexists"))
        self.assertTrue(result)

    def test_get_page_user_does_not_exist_returns_true(self):
        result = self.__target.get_page(self.__get_params())
        self.assertTrue(result)

    def test_get_page_without_setting_session_raises_session_not_set_exception(self):
        target = SignupHandler(self.__interactor_factory, None)
        self.assertRaises(SessionNotSetException, target.get_page, self.__get_params())        

    def __get_params(self, userid="user", password="password"):
        return {
            "userid": userid,
            "password": password
        }

    def __get_user(self, userid, password):
        u = User()
        u.user_id = userid
        u.password = password
        return u

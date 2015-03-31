import unittest
from unittest.mock import Mock

from Cryptography.HashProvider import HashProvider
from Interactors.InteractorFactory import InteractorFactory
from Interactors.User.LoginInteractor import LoginInteractor
from UI.Handlers.Handler import Handler
from UI.Handlers.SigninHandler import SigninHandler
from User import User


class TestSigninHandler(unittest.TestCase):
    
    def setUp(self):
        self.__interactor = Mock(LoginInteractor)
        self.__interactor.execute = Mock(side_effect=self.__interactor_execute)
        self.__hash_provider = Mock(HashProvider)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = SigninHandler(interactor_factory, None)
        
    def __interactor_execute(self, user):
        if user.user_id == "validuser":
            return True
        return False

    def test_is_session_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_sets_interactor_hash_provider(self):
        self.__target.get_page(self.__get_params())
        self.assertTrue(self.__interactor.set_hash_provider.called)
    
    def test_get_page_executes_interactor(self):
        self.__target.get_page(self.__get_params())
        self.__interactor.execute.assert_called_with(self.__get_user())
        
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

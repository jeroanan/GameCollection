import unittest
from unittest.mock import Mock
from Interactors.Exceptions.UserExistsException import UserExistsException
from Interactors.InteractorFactory import InteractorFactory
from Interactors.User.AddUserInteractor import AddUserInteractor
from UI.Handlers.Handler import Handler
from UI.Handlers.SignupHandler import SignupHandler
from User import User


class TestSignupHandler(unittest.TestCase):

    def setUp(self):
        self.__interactor = Mock(AddUserInteractor)
        self.__interactor.execute = Mock(side_effect=self.__interactor_execute)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = SignupHandler(self.__interactor_factory, None)

    def __interactor_execute(self, user):
        if user.user_id == "alreadyexists":
            raise UserExistsException

    def test_is_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_create_page_sets_hash_provider(self):
        self.__target.get_page(self.__get_params())
        self.assertTrue(self.__interactor.set_hash_provider.called)

    def test_get_create_page_executes_interactor(self):
        params = self.__get_params()
        user = self.__get_user(params["userid"], params["password"])
        self.__target.get_page(params)
        self.__interactor.execute.assert_called_with(user)

    def test_get_page_user_exists_returns_true(self):
        result = self.__target.get_page(self.__get_params("alreadyexists"))
        self.assertTrue(result)

    def test_get_page_user_does_not_exist_returns_true(self):
        result = self.__target.get_page(self.__get_params())
        self.assertTrue(result)

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

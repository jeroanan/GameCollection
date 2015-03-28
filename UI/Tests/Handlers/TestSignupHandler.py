import unittest
from unittest.mock import Mock
from Interactors.InteractorFactory import InteractorFactory
from Interactors.User.AddUserInteractor import AddUserInteractor
from UI.Handlers.Handler import Handler
from UI.Handlers.SignupHandler import SignupHandler


class TestSignupHandler(unittest.TestCase):

    def setUp(self):
        self.__interactor = Mock(AddUserInteractor)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = SignupHandler(self.__interactor_factory, None)

    def test_is_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_create_page_executes_interactor(self):
        params = self.__get_params()
        self.__target.get_page(params)
        self.__interactor.execute.assert_called_with(params["userid"], params["password"])

    def __get_params(self):
        return {
            "userid": "user",
            "password": "password"
        }

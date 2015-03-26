import unittest
from unittest.mock import Mock
from AbstractPersistence import AbstractPersistence
from Interactors.Exceptions.UserExistsException import UserExistsException
from Interactors.Interactor import Interactor
from Interactors.User.AddUserInteractor import AddUserInteractor
from User import User


class TestAddUserInteractor(unittest.TestCase):

    def setUp(self):
        self.__persistence = Mock(AbstractPersistence)
        self.__persistence.get_user = Mock(side_effect=self.__get_db_user)
        self.__target = AddUserInteractor()
        self.__target.persistence = self.__persistence

    def __get_db_user(self, user):
        if user.user_id == "existing_user":
            return [User()]
        return []

    def test_is_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_null_user_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_empty_user_id_raises_value_error(self):
        u = self.__get_user()
        self.assertRaises(ValueError, self.__target.execute, u)

    def test_execute_empty_password_raises_value_error(self):
        u = self.__get_user("user")
        self.assertRaises(ValueError, self.__target.execute, u)

    def test_execute_user_already_exists_raises_error(self):
        u = self.__get_user("existing_user", "pass")
        self.assertRaises(UserExistsException, self.__target.execute, u)

    def test_execute_adds_new_user(self):
        u = self.__get_user("new_user", "pass")
        self.__target.execute(u)
        self.__persistence.add_user.assert_called_with(u)

    def __get_user(self, user_id="", password=""):
        u = User()
        u.user_id = user_id
        u.password = password
        return u
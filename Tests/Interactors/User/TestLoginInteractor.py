from mock import Mock

from AbstractPersistence import AbstractPersistence
from Cryptography.HashProvider import HashProvider
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase
from Interactors.User.LoginInteractor import LoginInteractor
from User import User


class TestLoginInteractor(InteractorTestBase):

    def setUp(self):
        self.__hash_provider = Mock(HashProvider)
        self.__hash_provider.hash_text = Mock(side_effect=self.__get_hash)
        self.__hash_provider.verify_password = Mock(side_effect=self.__verify_password)
        self.__target = LoginInteractor()
        self.__persistence = Mock(AbstractPersistence)
        self.__persistence.get_user = Mock(side_effect=self.__get_user_from_persistence)
        self.__target.persistence = self.__persistence
        self.__target.set_hash_provider(self.__hash_provider)

    def __get_hash(self, hash_text):
        return "myhashedhash"

    def __verify_password(self, entered_password, hashed_password):
        return entered_password == hashed_password

    def __get_user_from_persistence(self, user):
        u = User()

        if user.user_id == "correctpass":
            u.user_id = "correctpass"
            u.password = "mypassword"

        if user.user_id == "incorrectpass":
            u.user_id = "incorrectpass"
            u.password = "wrongpassword"

        return u

    def test_is_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_correct_user_password_logs_in(self):
        u = self.__get_user("correctpass", "mypassword")
        self.assertTrue(self.__target.execute(u))

    def test_execute_incorrect_user_password_does_not_log_in(self):
        u = self.__get_user("incorrectpass", "somethingsilly")
        self.assertFalse(self.__target.execute(u))

    def test_execute_user_does_not_exist_returns_false(self):
        u = self.__get_user("unknown", "somepass")
        self.assertFalse(self.__target.execute(u))

    def test_execute_user_does_not_exist_does_not_verify_password(self):
        u = self.__get_user("unknown", "somepass")
        self.__target.execute(u)
        self.assertFalse(self.__hash_provider.verify_password.called)

    def test_execute_null_user_gives_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_empty_userid_gives_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, User())

    def test_execute_empty_password_gives_value_error(self):
        u = self.__get_user("userid", "")
        self.assertRaises(ValueError, self.__target.execute, u)

    def __get_user(self, user_id, password):
        u = User()
        u.user_id = user_id
        u.password = password
        return u

    def test_set_hash_provider_not_hash_provider_gives_value_error(self):
        self.assertRaises(ValueError, self.__target.set_hash_provider, ())

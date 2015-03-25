from mock import Mock
from AbstractPersistence import AbstractPersistence
from Cryptography.HashProvider import HashProvider
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase
from User import User


class LoginInteractor(Interactor):

    def __init__(self):
        super().__init__()
        self.hash_provider = HashProvider()

    def execute(self, user):
        self.__validate(user)
        hashed_pw = self.hash_provider.hash_text(user.password)
        db_user = self.persistence.get_user(user)

    def __validate(self, user):
        if user is None:
            raise TypeError
        self.validate_string_field("user_ud", user.user_id)
        self.validate_string_field("password", user.password)

    def set_hash_provider(self, param):
        if not isinstance(param, HashProvider):
            raise ValueError
        self.hash_provider = param


class TestLoginInteractor(InteractorTestBase):

    def setUp(self):
        self.__hash_provider = Mock(HashProvider)
        self.__hash_provider.hash_text = Mock(side_effect=self.get_hash)
        self.__target = LoginInteractor()
        self.__persistence = Mock(AbstractPersistence)
        self.__persistence.get_user = Mock(side_effect=self.get_user)
        self.__target.persistence = self.__persistence
        self.__target.set_hash_provider(self.__hash_provider)

    def get_hash(self, hash_text):
        return "myhash"

    def get_user(self, user):
        return User()

    def test_is_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_hash_provider(self):
        u = self.__get_user()
        self.__target.execute(u)
        self.__hash_provider.hash_text.assert_called_with(u.password)

    def test_execute_calls_persistence(self):
        u = self.__get_user()
        self.__target.execute(u)
        self.__persistence.get_user.assert_called_with(u)

    def test_execute_null_user_gives_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_empty_userid_gives_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, User())

    def test_execute_empty_password_gives_value_error(self):
        u = User()
        u.user_id = "userid"
        self.assertRaises(ValueError, self.__target.execute, u)

    def __get_user(self):
        u = User()
        u.user_id = "userid"
        u.password = "mypass"
        return u

    def test_set_hash_provider_not_hash_provider_gives_value_error(self):
        self.assertRaises(ValueError, self.__target.set_hash_provider, ())
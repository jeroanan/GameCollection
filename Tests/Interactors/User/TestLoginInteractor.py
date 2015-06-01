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

from logging import Logger
from mock import Mock

from AbstractPersistence import AbstractPersistence
from Cryptography.HashProvider import HashProvider
from Interactors.LoggingInteractor import LoggingInteractor
from Tests.Interactors.InteractorTestBase import InteractorTestBase
from Interactors.UserInteractors import LoginInteractor
from User import User


class TestLoginInteractor(InteractorTestBase):
    """Unit tests for the LoginInteractor class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        self.__get_hash = lambda hash_text: "myhashedhash"
        self.__hash_provider = Mock(HashProvider)
        self.__hash_provider.hash_text = Mock(side_effect=self.__get_hash)
        self.__hash_provider.verify_password = Mock(side_effect=self.__verify_password)
        self.__target = LoginInteractor()
        self.__persistence = Mock(AbstractPersistence)
        self.__persistence.get_user = Mock(side_effect=self.__get_user_from_persistence)
        self.__target.persistence = self.__persistence
        self.__target.logger = Mock(Logger)
        self.__target.set_hash_provider(self.__hash_provider)

    def __verify_password(self, entered_password, hashed_password):
        return entered_password == hashed_password

    def __get_user_from_persistence(self, user):
        if user.user_id == "correctpass":
            return User.from_dict({"userid": "correctpass", "password": "mypassword"})        
        if user.user_id == "incorrectpass":
            return User.from_dict({"userid": "incorrectpass", "password": "wrongpassword"})
        return User()

    def test_is_logging_interactor(self):
        """Test that LoginInteractor is an instance of LoggingInteractor"""
        self.assertIsInstance(self.__target, LoggingInteractor)

    def test_execute_correct_user_password_logs_in(self):
        """Test that calling LoginInteractor.execute with a correct password returns True"""
        u = self.__get_user("correctpass", "mypassword")
        self.assertTrue(self.__target.execute(u))

    def test_execute_incorrect_user_password_does_not_log_in(self):
        """Test that calling LoginInteractor.execute with an incorrect password returns False"""
        u = self.__get_user("incorrectpass", "somethingsilly")
        self.assertFalse(self.__target.execute(u))

    def test_execute_user_does_not_exist_returns_false(self):
        """Test that calling LoginInteractor.execute for a non-existent user returns False"""
        u = self.__get_user("unknown", "somepass")
        self.assertFalse(self.__target.execute(u))

    def test_execute_null_user_gives_type_error(self):
        """Test that calling LoginInteractor.execute with a null user raises TypeError"""
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_empty_userid_gives_value_error(self):
        """Test that calling LoginInteractor.execute with an empty userid raises ValueError"""
        self.assertRaises(ValueError, self.__target.execute, User())

    def test_execute_empty_password_gives_value_error(self):
        """Test that calling LoginInteractor.execute with an empty password raises ValueError"""
        u = self.__get_user("userid", "")
        self.assertRaises(ValueError, self.__target.execute, u)

    def __get_user(self, user_id, password):
        return User.from_dict({"userid": user_id, "password": password})


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
import unittest
from unittest.mock import Mock
from AbstractPersistence import AbstractPersistence
from Cryptography.HashProvider import HashProvider
from Interactors.Exceptions.UserExistsException import UserExistsException
from Interactors.LoggingInteractor import LoggingInteractor
from Interactors.UserInteractors import AddUserInteractor
from User import User


class TestAddUserInteractor(unittest.TestCase):
    """Unit tests for the AddUserInteractor class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        self.__persistence = Mock(AbstractPersistence)
        self.__persistence.get_user = Mock(side_effect=self.__get_db_user)
        self.__hash_provider = Mock(HashProvider)
        self.__target = AddUserInteractor()
        self.__target.persistence = self.__persistence
        self.__target.logger = Mock(Logger)
        self.__target.set_hash_provider(self.__hash_provider)

    def __get_db_user(self, user):
        if user.user_id == "existing_user":
            return user
        return User()

    def test_is_logging_interactor(self):
        """Test that AddUserInteractor is an instance of LoggingInteractor"""
        self.assertIsInstance(self.__target, LoggingInteractor)

    def test_execute_null_user_raises_type_error(self):
        """Test that calling AddUserInteractor.execute with a null user raises a TypeError"""
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_empty_user_id_raises_value_error(self):
        """Test that calling AddUserInteractor.execute with a null user_id raises a ValueError"""
        u = self.__get_user()
        self.assertRaises(ValueError, self.__target.execute, u)

    def test_execute_empty_password_raises_value_error(self):
        """Test that calling AddUserInteractor.execute with an empty password raises a ValueError"""
        u = self.__get_user("user")
        self.assertRaises(ValueError, self.__target.execute, u)

    def test_execute_user_already_exists_raises_user_exists_exception(self):
        """Test that calling AddUserInteractor.execute with an existing user raises a UserExistsException"""
        u = self.__get_user("existing_user", "pass")
        self.assertRaises(UserExistsException, self.__target.execute, u)

    def test_execute_adds_new_user(self):
        """Test that calling AddUserInteractor.execute with valid parameters causes persistence.add_user to be called"""
        u = self.__get_user("new_user", "pass")
        self.__target.execute(u)
        self.__persistence.add_user.assert_called_with(u)

    def test_execute_calls_hash_provider(self):
        """Test that calling AddUserInteractor.execute with valid parameters causes user.passwod to be hashed"""
        u = self.__get_user("new_user", "pass")
        passwd = u.password
        self.__target.execute(u)
        self.__hash_provider.hash_text.assert_called_with(passwd)

    def __get_user(self, user_id="", password=""):
        return User.from_dict({"userid": user_id, "password": password})


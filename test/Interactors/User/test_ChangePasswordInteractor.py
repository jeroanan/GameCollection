# Copyright (c) David Wilson 2015
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

import unittest
from unittest.mock import Mock

from AbstractPersistence import AbstractPersistence
from Cryptography.HashProvider import HashProvider
from Interactors.Exceptions.InteractorFactoryNotSetException import InteractorFactoryNotSetException
from Interactors.InteractorFactory import InteractorFactory
from Interactors.LoggingInteractor import LoggingInteractor
from Interactors.UserInteractors import ChangePasswordInteractor, GetUserInteractor
from User import User


class TestChangePasswordInteractor(unittest.TestCase):
    """Unit tests for the ChangePasswordInteractor class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        self.__get_user_interactor = self.__setUp_get_user_interactor()
        self.__interactor_factory = self.__setUp_interactor_factory()
        self.__target = ChangePasswordInteractor()
        self.__target.interactor_factory = self.__interactor_factory
        self.__persistence = Mock(AbstractPersistence)
        self.__target.persistence = self.__persistence
        self.__hash_provider = Mock(HashProvider)
        self.__target.set_hash_provider(self.__hash_provider)

    def __setUp_get_user_interactor(self):

        def get_user_interactor_execute(user):
            return self.__get_user(user_id=user.user_id, password="MyOldPassword", id="123456")

        get_user_interactor = Mock(GetUserInteractor)
        get_user_interactor.execute = Mock(side_effect=get_user_interactor_execute)
        return get_user_interactor

    def __setUp_interactor_factory(self):
        
        def interactor_factory_create(interactor_type):
            return self.__get_user_interactor

        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(side_effect=interactor_factory_create)
        return interactor_factory

    def test_is_logging_interactor(self):
        """Test that ChangePasswordInteractor is an instance of LoggingInteractor"""
        self.assertIsInstance(self.__target, LoggingInteractor)

    def test_user_is_nothing_raises_type_error(self):
        """Test that calling ChangePasswordInteractor.execute with a null user raises a TypeError"""
        self.assertRaises(TypeError, self.__target.execute, None)
        
    def test_user_id_is_empty_raises_value_error(self):
        """Test that calling ChangePasswordInteractor.execute with an empty user_id raises ValueError"""
        u = self.__get_user("", "")
        self.assertRaises(ValueError, self.__target.execute, u)
        
    def test_password_is_empty_raises_value_error(self):
        """Test that calling ChangePasswordInteractor.execute with an empty password raises ValueError"""
        u = self.__get_user(password="")
        self.assertRaises(ValueError, self.__target.execute, u)
 
    def test_interactor_factory_not_set_raises_interactor_factory_not_set_exception(self):
        """Test that calling ChangePasswordInteractor.execute without setting interactor_factory raises 
        InteractorFactoryNotSetException"""
        self.__target.interactor_factory = None
        self.assertRaises(InteractorFactoryNotSetException, self.__target.execute, User())

    def test_executes_user_interactor(self):
        """Test that calling ChangePasswordInteractor.execute correctly causes GetUserInteractor.execute to be called"""
        u = self.__get_user()
        self.__target.execute(u)
        self.__get_user_interactor.execute.assert_called_with(u)

    def test_user_found_creates_calls_change_password_persistence_method(self):
        """Test that calling ChangePasswordInteractor.execute correctly causes persistence.change_password to be 
        called"""
        u = self.__get_user()
        dbu = self.__get_user(id="123456", password=u.password)
        self.__target.execute(u)
        self.__persistence.change_password.assert_called_with(dbu)
        
    def test_user_found_hashes_password(self):
        """Test that calling ChangePasswordInteractor.execute correctly causes hash_provider.hash_text to be called"""
        u = self.__get_user()
        self.__target.execute(u)
        self.__hash_provider.hash_text.assert_called_with(u.password)

    def __get_user(self, user_id="user", password="password", id="id"):
        u = User()
        u.user_id = user_id
        u.password = password
        u.id = id
        return u

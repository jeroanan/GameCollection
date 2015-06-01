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
from Interactors.Interactor import Interactor
from Interactors.UserInteractors import GetUserInteractor
from Tests.Interactors.InteractorTestBase import InteractorTestBase
from User import User
        

class TestGetUserInteractor(InteractorTestBase):
    """Unit tests for GetUserInteractor"""

    def setUp(self):
        """setUp function for all unit tests in this class."""
        self.__persistence = Mock(AbstractPersistence)
        self.__target = GetUserInteractor()        
        self.__target.persistence = self.__persistence
        self.__get_user = lambda user_id: User.from_dict({"userid": user_id})

    def test_is_interactor(self):
        """Test that GetUserInteractor dervies from Interactor"""
        self.assertIsInstance(self.__target, Interactor)
        
    def test_execute_with_null_user_raises_type_error(self):
        """Test that executing GetUserInteractor with a null object raises a TypeError"""
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_with_user_id_gets_user_from_persistence(self):
        """Test that executing GetUserInteractor calls persistence for the User record."""    
        self.__target.execute(self.__get_user("userid"))
        self.assertTrue(self.__persistence.get_user.called)



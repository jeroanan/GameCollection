# Copyright (c) 20115 David Wilson
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
from Interactors.User.UpdateUserInteractor import UpdateUserInteractor
from User import User


class TestUpdateUserInteractor(unittest.TestCase):
    """Unit tests for the UpdateUserInteractor class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        self.__target = UpdateUserInteractor()
        self.__persistence = Mock(AbstractPersistence)
        self.__target.persistence = self.__persistence
        self.__user = User.from_dict({"id": "id", "userid": "userid"})
        
    def test_is_type_of_interactor(self):
        """Test that UpdateUserInteractor is derived from Interactor"""
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        """Test that executing UpdateUserInteractor causes it to call persistence.update_user."""
        self.__target.execute(self.__user)
        self.__persistence.update_user.assert_called_with(self.__user)

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

from unittest.mock import Mock
from AbstractPersistence import AbstractPersistence
from Interactors.Exceptions.PersistenceException import PersistenceException
from Interactors.Interactor import Interactor
from Interactors.GameInteractors import UpdateGameInteractor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestUpdateGameInteractor(InteractorTestBase):
    """Unit tests for the UpdateGameInteractor class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        super().setUp()
        self.__target = UpdateGameInteractor()
        self.__target.persistence = self.persistence
        self.__target.validate_string_field = self.validate_string_field
        self.__target.validate_integer_field = self.validate_integer_field
        self.__game = self.get_game(title="title", platform="platform", num_copies=1, num_boxed=2, num_manuals=3,
                                    notes="")

    def test_is_instance_of_interactor(self):
        """Test that UpdateGameInteractor derives from Interactor"""
        self.assertIsInstance(self.__target, Interactor)

    def test_calls_persistence_method(self):
        """Test that calling UpdateGameInteractor.execute causes persistence.update_game to be called"""
        self.__execute(self.__game, "userid")
        self.persistence.update_game.assert_called_with(self.__game, "userid")

    def test_with_null_game_raises_type_error(self):
        """Test that calling UpdateGameInteractor.execute with a null game causes TypeError to be raised"""
        self.assertRaises(TypeError, self.__execute, None)

    def test_validates_title_field(self):
        #DUPLICATION
        self.__assert_string_validation("Game title", self.__game.title)

    def test_validates_platform_field(self):
        self.__assert_string_validation("Game platform", self.__game.platform)

    def __assert_string_validation(self, field_name, field_value):
        self.__execute(self.__game)
        self.validate_string_field_was_called_with(field_name, field_value)

    def test_validates_num_copies_field(self):
        self.__assert_integer_validation("Number of copies", self.__game.num_copies)

    def test_validates_num_boxed_field(self):
        self.__assert_integer_validation("Number of boxed copies", self.__game.num_boxed)

    def test_validates_num_manuals_field(self):
        self.__assert_integer_validation("Number of manuals", self.__game.num_manuals)

    def __assert_integer_validation(self, field_name, field_value):
        self.__execute(self.__game)
        self.validate_integer_field_was_called_with(field_name, field_value)

    def test_raises_persistence_exception_when_database_throws(self):
        def update_game(g):
            raise Exception

        self.__target.persistence = None
        p = Mock(AbstractPersistence)
        p.update_game = Mock(side_effect=update_game)
        self.__target.persistence = p
        self.assertRaises(PersistenceException, self.__execute, self.__game)

    def __execute(self, game, user_id="user_id"):
        self.__target.execute(game, user_id)

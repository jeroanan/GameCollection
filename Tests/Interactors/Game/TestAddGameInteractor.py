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

from Interactors.GameInteractors import AddGameInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestAddGameInteractor(InteractorTestBase):
    """Unit tests for the AddGameInteractor class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        super().setUp()
        self.__target = AddGameInteractor()
        self.__target.persistence = self.persistence
        self.__target.validate_integer_field = self.validate_integer_field
        self.__target.validate_string_field = self.validate_string_field

    def test_is_instance_of_interactor(self):
        """Test that AddGameInteractor is derived from Interactor"""
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        """Test that calling AddGameInteractor.execute causes persistence.add_game to be called"""
        game = self.get_game()
        user_id = "1234"
        self.__execute(game, user_id)
        self.persistence.add_game.assert_called_with(game, user_id)

    def test_execute_with_null_game_raises_type_error(self):
        """Test that calling AddGameInteractor.execute with a null game causes a TypeError to be raised"""
        self.assertRaises(TypeError, self.__execute, None)

    def test_execute_validates_integer_fields(self):
        """Test that calling AddGameInteractor.execute causes all integer fields in game to be validated"""
        integer_validations = {"Number of boxed items": 1,
                               "Number of copies": 2,
                               "Number of manuals": 3}        
        self.__execute(self.get_game(num_boxed=1, num_copies=2, num_manuals=3))

        for iv in integer_validations:
            self.assertTrue(self.validate_integer_field_was_called_with(iv, integer_validations[iv]))

    def test_execute_validates_string_fields(self):
        """Test that calling AddGameInteractor.execute causes all string fields in game to be validated"""
        string_validations = {"Platform": "platform",
                              "Game title": "title"}
        self.__execute(self.get_game(title="title", platform="platform"))
        for sv in string_validations:
            self.assertTrue(self.validate_string_field_was_called_with(sv, string_validations[sv]))
                
    def test_execute_with_game_id_raises_value_error(self):
        """Test that adding a game with its id property set raises a ValueError"""
        game = self.get_game(game_id="id")
        self.assertRaises(ValueError, self.__execute, game)
    
    def __execute(self, game, user_id="1234"):
        self.__target.execute(game, user_id)

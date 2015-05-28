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

from Interactors.GameInteractors import DeleteGameInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestDeleteGameInteractor(InteractorTestBase):
    """Unit tests for the DeleteGameInteractor class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        super().setUp()
        self.__target = DeleteGameInteractor()
        self.__target.persistence = self.persistence
        self.__target.validate_string_field = self.validate_string_field

    def test_is_instance_of_interactor(self):        
        """Test that DeleteGameInteractor derives from Interactor"""
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        """Test that calling DeleteGameInteractor.execute causes persistence.delete_game to be called"""
        game = self.get_game(game_id="1337")        
        self.__execute(game, "user_id")
        self.persistence.delete_game.assert_called_with(game, "user_id")

    def test_execute_with_none_game_raises_type_error(self):
        """Test that calling DeleteGameInteractor.execute with a null game causes a TypeError to be raised"""
        self.assertRaises(TypeError, self.__execute, None)

    def test_execute_validates_id_field(self):
        """Test that calling DeleteGameInteractor.execute causes the id field to be validated."""
        game = self.get_game(game_id="id")
        self.__execute(game)
        self.assertTrue(self.validate_string_field_was_called_with("Game id", game.id))

    def __execute(self, game, user_id="user"):
        self.__target.execute(game, user_id) 

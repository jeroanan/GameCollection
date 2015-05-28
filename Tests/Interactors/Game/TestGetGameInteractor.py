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

from Interactors.GameInteractors import GetGameInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestGetGameInteractor(InteractorTestBase):
    """Unit tests for the GetGameInteractor class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        super().setUp()
        self.__target = GetGameInteractor()
        self.__target.persistence = self.persistence

    def test_is_instance_of_interactor(self):
        """Test that GetGameInteractor derives from Interactor"""
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_with_none_game_id_raises_value_error(self):
        """Test that calling GetGameInteractor.execute with a null game raises a ValueError"""
        self.assertRaises(ValueError, self.__target.execute, None, "user")

    def test_execute_calls_persistence(self):
        """Test that calling GetGameInteractor.execute causes persistence.get_game to be called"""
        self.__target.execute("gameid", "user")
        self.persistence.get_game.assert_called_with("gameid", "user")


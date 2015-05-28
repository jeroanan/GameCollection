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

from Interactors.GameInteractors import CountGamesInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestCountGamesInteractor(InteractorTestBase):
    """Unit tests for the CountGamesInteractor class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        super().setUp()
        self.__target = CountGamesInteractor()
        self.__target.persistence = self.persistence

    def test_is_interactor(self):
        """Test that CountGamesInteractor derives from Interactor"""
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        """Test that calling CountGamesInteractor.execute causes persistence.count_games to be called."""
        user_id = "user_id"
        self.__target.execute(user_id)
        self.persistence.count_games.assert_called_with(user_id)

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

from Interactors.GenreInteractors import GetGenreInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestGetGenreInteractor(InteractorTestBase):
    """Unit tests for the GetGenreInteractor class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        super().setUp()
        self.__target = GetGenreInteractor()
        self.__target.persistence = self.persistence

    def test_is_instance_of_interactor(self):
        """Test that GetGenreInteractor is derived from Interactor"""
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        """Test that calling GetGenreInteractor.execute causes persistence.get_genre_details to be called"""
        self.__target.execute(genre_id="id")
        self.persistence.get_genre_details.assert_called_with("id")

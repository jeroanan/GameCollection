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

from Genre import Genre
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase
from Interactors.GenreInteractors import UpdateGenreInteractor


class TestUpdateGenreInteractor(InteractorTestBase):
    """Unit tests for the UpdateGenreInteractor class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        super().setUp()
        self.__target = UpdateGenreInteractor()
        self.__target.persistence = self.persistence

    def test_is_interactor(self):
        """Test that UpdateGenreInteractor is derived from Interactor"""
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        """Test that callign UpdateGenreInteractor.execute causes persistence.update_genre to be called"""
        genre = Genre()
        self.__target.execute(genre)
        self.persistence.update_genre.assert_called_with(genre)


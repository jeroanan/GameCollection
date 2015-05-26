# copyright (c) David Wilson 2015
# This file is part of Icarus.

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
from Interactors.GenreInteractors import DeleteGenreInteractor
from Interactors.Interactor import Interactor
from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestDeleteGenreInteractor(InteractorTestBase):
    """Unit tests for the DeleteGenreInteractor class"""
    
    def setUp(self):
        """setUp function for all unit tests in this class"""
        super().setUp()
        self.__target = DeleteGenreInteractor()
        self.__target.persistence = self.persistence

    def test_is_interactor(self):
        """Test that DeleteGenreInteractor is derived from Interactor"""
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence(self):
        """Test that calling DeleteGenreInteractor.execute calls persistence.delete_genre"""
        g = Genre.from_dict({"id": "id"})
        self.__target.execute(genre=g)
        self.persistence.delete_genre.assert_called_with(g.id)

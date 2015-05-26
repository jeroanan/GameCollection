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
from Interactors.GenreInteractors import AddGenreInteractor
from Interactors.Interactor import Interactor

from Tests.Interactors.InteractorTestBase import InteractorTestBase


class TestAddGenreInteractor(InteractorTestBase):
    """Unit tests for the AddGenreInteractor class"""

    def setUp(self):
        """setUp function for all unit tests in this class"""
        super().setUp()
        self.__target = AddGenreInteractor()
        self.__target.persistence = self.persistence
        self.__target.validate_string_field = self.validate_string_field

    def test_is_interactor(self):
        """Test that AddGenreInteractor is derived from Interactor"""
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        """Test that calling AddGenreInteractor.execute causes persistence.add_genre to be called"""
        genre = Genre()
        self.__target.execute(genre=genre)
        self.persistence.add_genre.assert_called_with(genre)

    def test_execute_with_none_genre_raises_type_error(self):
        """Test that calling AddGenreInteractor.execute with a null Genre causes a TypeError to be raised.""" 
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_validates_title_field(self):
        """Tes that AddGenreInteractor.execute validates the name field in the Genre it is passed"""
        genre = Genre()
        genre.name = "Genre"
        self.__target.execute(genre)
        self.assertTrue(self.validate_string_field_was_called_with("Name", genre.name))

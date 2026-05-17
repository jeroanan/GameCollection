"""Unit tests for GetSuggestedGenresInteractor."""
# Copyright (c) David Wilson 2015, 2026
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

from persistence import abstract_persistence
from interactors import interactor
import interactors.genre_interactors as gi
import genre


class TestGetSuggestedGenresInteractor(unittest.TestCase):
    """Unit tests for GetSuggestedGenresInteractor."""

    def setUp(self):
        persistence = Mock(abstract_persistence.AbstractPersistence)
        persistence.get_genres = Mock(return_value=[genre.Genre.from_dict({"name": "genre1"})])
        self.__target = gi.GetSuggestedGenresInteractor(self.__get_suggested_genres)
        self.__target.persistence = persistence

    def __get_suggested_genres(self):

        def from_dict(d):
            return genre.Genre.from_dict(d)

        return [from_dict({"name": "genre1"}), from_dict({"name": "genre2"})]

    def test_is_instance_of_interactor(self):
        """Test that the interactor is an instance of Interactor."""
        self.assertIsInstance(self.__target, interactor.Interactor)

    def test_execute_only_returns_suggested_genres_not_already_stored(self):
        """Test that execute only returns suggested genres not already stored."""
        suggested_genres = self.__target.execute()
        self.assertEqual(1, len(suggested_genres))

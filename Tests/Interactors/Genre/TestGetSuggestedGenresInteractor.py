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

import unittest
from unittest.mock import Mock

import AbstractPersistence as abstract_persistence
import Interactors.Interactor as interactor
import Interactors.GenreInteractors as gi
import Genre as genre


class TestGetSuggestedGenresInteractor(unittest.TestCase):
    
    def setUp(self):
        persistence = Mock(abstract_persistence.AbstractPersistence)
        persistence.get_genres = Mock(return_value=[genre.Genre.from_dict({"name": "genre1"})])
        self.__target = gi.GetSuggestedGenresInteractor(self.__get_suggested_genres)
        self.__target.persistence = persistence

    def __get_suggested_genres(self):
        from_dict = lambda d: genre.Genre.from_dict(d)
        return [from_dict({"name": "genre1"}), from_dict({"name": "genre2"})]

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, interactor.Interactor)

    def test_execute_only_returns_suggested_genres_not_already_stored(self):
        suggested_genres = self.__target.execute()
        self.assertEqual(1, len(suggested_genres))


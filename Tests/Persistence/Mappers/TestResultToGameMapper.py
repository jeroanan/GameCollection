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
# along with Icarus.  If not, see <http://www.gnu.org/licenses/>

import unittest
from Game import Game
from Persistence.Exceptions.GameNotFoundException import GameNotFoundException
from Persistence.Mappers.ResultToGameMapper import ResultToGameMapper


class TestResultToGameMapper(unittest.TestCase):

    def setUp(self):        
        self.__mongo_result = {"_id": "id", "_Game__title": "title", "_Game__platform": "platform",
                               "_Game__num_copies": "1", "_Game__num_boxed": "2", "_Game__num_manuals": "3",
                               "_Game__notes": "notes", "_Game__date_purchased": "1/1/1990", 
                               "_Game__approximate_date_purchased": "true"}
        self.__target = ResultToGameMapper(self.__mongo_result)

    def test_map_returns_game(self):
        game = self.__target.map()
        self.assertIsInstance(game, Game)    

    def test_map_none_raises_gamenotfoundexception(self):
        target = ResultToGameMapper(None)
        self.assertRaises(GameNotFoundException, target.map)

    def test_map_id_maps_id(self):
        self.__assert_mapped("id", "id")

    def test_map_title_maps_title(self):
        self.__assert_mapped("title", "title")

    def test_map_platform_maps_platform(self):
        self.__assert_mapped("platform", "platform")

    def test_map_num_copies_maps_num_copies(self):
        self.__assert_mapped("1", "num_copies")

    def test_map_num_boxed_maps_num_boxed(self):
        self.__assert_mapped("2", "num_boxed")
        
    def test_map_num_boxed_maps_num_manuals(self):
        self.__assert_mapped("3", "num_manuals")

    def test_map_maps_notes(self):
        self.__assert_mapped("notes", "notes")

    def test_map_date_purchased(self):
        self.__assert_mapped("1/1/1990", "date_purchased")

    def test_map_approximate_date_purchased(self):
        self.__assert_mapped("true", "approximate_date_purchased")

    def __assert_mapped(self, expected_value, field_name):
        mapped = self.__target.map()
        self.assertEqual(expected_value, getattr(mapped, field_name))

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
from Tests.Persistence.Mappers.MapTools import get_map_checker
from Persistence.Mappers.ResultToGameMapper import ResultToGameMapper


class TestResultToGameMapper(unittest.TestCase):

    def setUp(self):        
        mongo_result = {"_id": "id", "_Game__title": "title", "_Game__platform": "platform",
                        "_Game__num_copies": "1", "_Game__num_boxed": "2", "_Game__num_manuals": "3",
                        "_Game__notes": "notes", "_Game__date_purchased": "1/1/1990", 
                        "_Game__approximate_date_purchased": "true"}
        target = ResultToGameMapper(mongo_result)
        self.__check_maps = get_map_checker(target)

    def test_map_none_raises_gamenotfoundexception(self):
        target = ResultToGameMapper(None)
        self.assertRaises(GameNotFoundException, target.map)

    def test_fields_map(self):
        mappings = {"id": "id",
                    "title": "title",
                    "platform": "platform",
                    "1": "num_copies",
                    "2": "num_boxed",
                    "3": "num_manuals",
                    "notes": "notes",
                    "1/1/1990": "date_purchased",
                    "true": "approximate_date_purchased"}
        for m in mappings:
            self.assertTrue(self.__check_maps(m, mappings[m]), "Failed to map {0}.".format(mappings[m]))

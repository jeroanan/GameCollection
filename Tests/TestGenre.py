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
from Genre import Genre

class TestGenre(unittest.TestCase):
    
    def test_from_dict_returns_genre(self):
        g = Genre.from_dict({"": ""})
        self.assertIsInstance(g, Genre)

    def test_from_dict_does_mappings(self):
        d = {"name": "name",
             "description": "description",
             "id": "id"}
        g = Genre.from_dict(d)
        self.assertEqual(d["name"], g.name)
        self.assertEqual(d["description"], g.description)
        self.assertEqual(d["id"], g.id)

    def test_from_mongo_result_returns_genre(self):
        g = Genre.from_mongo_result({"": ""})
        self.assertIsInstance(g, Genre)

    def test_from_mongo_result_does_mappings(self):
        d = {"_id": "id",
             "_Genre__name": "name",
             "_Genre__description": "description"}
        g = Genre.from_mongo_result(d)
        self.assertEqual(d["_id"], g.id)
        self.assertEqual(d["_Genre__name"], g.name)
        self.assertEqual(d["_Genre__description"], g.description)
        


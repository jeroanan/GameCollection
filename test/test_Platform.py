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

from Platform import Platform


class TestPlatform(unittest.TestCase):
    
    def test_from_dict(self):
        Platform.from_dict({"":""})

    def test_from_dict_returns_platform(self):
        result = Platform.from_dict({"":""})
        self.assertIsInstance(result, Platform)

    def test_from_dict_performs_mappings(self):
        d  = {"name": "name",
              "description": "description"}
        result = Platform.from_dict(d)
        self.assertEqual(d["name"], result.name)
        self.assertEqual(d["description"], result.description)

    def test_from_mongo_result_performs_mapping(self):
        """Initialise the mapper
        :param mongo_result: A MongoDB result. The following fields
        can currently be mapped:
          * _id
          * _Platform__name
          * _Platform__description
        """
        d = {"_id": "id",
             "_Platform__name": "name",
             "_Platform__description": "description"}
        p = Platform.from_mongo_result(d)
        self.assertEqual(d["_id"], p.id)
        self.assertEqual(d["_Platform__name"], p.name)
        self.assertEqual(d["_Platform__description"], p.description)
        

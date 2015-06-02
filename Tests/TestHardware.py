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

import unittest

from Hardware import Hardware


class TestHardware(unittest.TestCase):
    """Unit tests for the Hardware class"""

    def test_from_mongo_result_performs_mapping(self):
        """Mapping mongo result to Hardware object properly initialises object."""
        hd = {"_id": "id",
              "_Hardware__name": "name",
              "_Hardware__platform": "platform",
              "_Hardware__num_owned": 1,
              "_Hardware__num_boxed": 2,
              "_Hardware__notes": "notes"}
    
        h = Hardware.from_mongo_result(hd)
        self.assertEqual(hd["_id"], h.id)
        self.assertEqual(hd["_Hardware__name"], h.name)
        self.assertEqual(hd["_Hardware__platform"], h.platform)
        self.assertEqual(hd["_Hardware__num_owned"], h.num_owned)
        self.assertEqual(hd["_Hardware__num_boxed"], h.num_boxed)
        self.assertEqual(hd["_Hardware__notes"], h.notes)
        
    def test_from_dict_performs_mappings(self):
        """Mapping a dictionary to Hardware object properly initialises object"""
        hd = {
            "id": "id",
            "name": "name",
            "platform": "platform",
            "numcopies": 1,
            "numboxed": 2,
            "notes": "notes",
            "userid": "userid"
        }
        h = Hardware.from_dict(hd)
        self.assertEqual(hd["id"], h.id)
        self.assertEqual(hd["name"], h.name)
        self.assertEqual(hd["platform"], h.platform)
        self.assertEqual(hd["numcopies"], h.num_owned)
        self.assertEqual(hd["numboxed"], h.num_boxed)
        self.assertEqual(hd["notes"], h.notes)
        self.assertEqual(hd["userid"], h.user_id)

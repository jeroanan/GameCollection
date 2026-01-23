# Copyright (c) 2015 David Wilson
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

import Hardware as hw


class TestHardware(unittest.TestCase):
    """Unit tests for the Hardware class"""

    def test_from_mongo_result_performs_mapping(self):
        """Mapping mongo result to Hardware object properly initialises object."""

        hd = {
            "_id": "id",
            "_Hardware__name": "name",
            "_Hardware__platform": "platform",
            "_Hardware__num_owned": 1,
            "_Hardware__num_boxed": 2,
            "_Hardware__notes": "notes",
            "_Hardware__hardware_type": "ht"
        }
    
        h = hw.Hardware.from_mongo_result(hd)

        expected_mappings = {
            "_id": h.id,
            "_Hardware__name": h.name,
            "_Hardware__platform": h.platform,
            "_Hardware__num_owned": h.num_owned,
            "_Hardware__num_boxed": h.num_boxed,
            "_Hardware__notes": h.notes,
            "_Hardware__hardware_type": h.hardware_type
        }

        for k, v in expected_mappings.items():
            self.assertEqual(hd[k], v)
        
    def test_from_dict_performs_mappings(self):
        """Mapping a dictionary to Hardware object properly initialises object"""

        hd = {
            "id": "id",
            "name": "name",
            "platform": "platform",
            "numcopies": 1,
            "numboxed": 2,
            "notes": "notes",
            "userid": "userid",
            "hardwaretype": "ht"
        }

        h = hw.Hardware.from_dict(hd)

        expected_mappings = {
            "id": h.id,
            "name": h.name,
            "platform": h.platform,
            "numcopies": h.num_owned,
            "numboxed": h.num_boxed,
            "notes": h.notes,
            "userid": h.user_id,
            "hardwaretype": h.hardware_type
        }

        for k, v in expected_mappings.items():
            self.assertEqual(hd[k], v)

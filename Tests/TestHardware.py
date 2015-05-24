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
    
    def test_from_mongo_result_performs_mapping(self):
        """Mapping mongo result to Hardware object properly initialises User object."""
        hd = {"_id": "id",
              "_Hardware__name": "name",
              "_Hardware__num_owned": 1,
              "_Hardware__num_boxed": 2,
              "_Hardware__notes": "notes"}
    
        h = Hardware.from_mongo_result(hd)
        self.assertEqual(hd["_id"], h.id)
        self.assertEqual(hd["_Hardware__name"], h.name)
        self.assertEqual(hd["_Hardware__num_owned"], h.num_owned)
        self.assertEqual(hd["_Hardware__num_boxed"], h.num_boxed)
        self.assertEqual(hd["_Hardware__notes"], h.notes)
        

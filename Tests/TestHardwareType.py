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

import HardwareType as ht


class TestHardwareType(unittest.TestCase):

    def test_from_dict_performs_mappings(self):
        mappings = {"id": "id",
                    "name": "name",
                    "description": "description"}

        expected = {"id": mappings["id"],
                    "name": mappings["name"],
                    "description": mappings["description"]}

        hardware_type = ht.HardwareType.from_dict(mappings)
        
        list(map(lambda x: self.assertEqual(getattr(hardware_type, x), expected[x]), expected))

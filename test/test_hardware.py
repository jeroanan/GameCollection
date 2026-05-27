"""Unit tests for the Hardware class"""
# Copyright (c) 2015. 2026 David Wilson
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

import hardware as hw


class TestHardware(unittest.TestCase):
    """Unit tests for the Hardware class"""

    def test_from_dict_performs_mappings(self) -> None:
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

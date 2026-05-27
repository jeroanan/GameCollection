"""Unit tests for HardwareType class."""
# Copyright (c) David Wilson 2015, 2026
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

import hardware_type as ht


class TestHardwareType(unittest.TestCase):
    """Unit tests for HardwareType class."""

    def test_from_dict_performs_mappings(self) -> None:
        """Tests that from_dict performs correct mappings."""
        mappings = {"id": "id",
                    "name": "name",
                    "description": "description"}

        expected = {"id": mappings["id"],
                    "name": mappings["name"],
                    "description": mappings["description"]}

        hardware_type = ht.HardwareType.from_dict(mappings)

        list(map(lambda x: self.assertEqual(getattr(hardware_type, x), expected[x]), expected))

"""Tests for the Genre class"""
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
from genre import Genre

class TestGenre(unittest.TestCase):
    """Tests for the Genre class"""

    def test_from_dict_returns_genre(self) -> None:
        """Tests that from_dict returns a Genre instance"""
        g = Genre.from_dict({"": ""})
        self.assertIsInstance(g, Genre)

    def test_from_dict_does_mappings(self) -> None:
        """Tests that from_dict maps dictionary keys to Genre attributes"""
        d = {"name": "name",
             "description": "description",
             "id": "id"}
        g = Genre.from_dict(d)
        self.assertEqual(d["name"], g.name)
        self.assertEqual(d["description"], g.description)
        self.assertEqual(d["id"], g.id)

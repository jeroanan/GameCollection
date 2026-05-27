"""Unit tests for the Game class"""
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

from game import Game


class TestGame(unittest.TestCase):
    """Unit tests for the Game class"""

    def test_from_dict(self) -> None:
        """Test that mapping a game object from a dictionary is correct."""

        gd = {
            "id": "id",
            "datepurchased": "1/1/1990",
            "genre": "genre",
            "title": "Title",
            "numcopies": 1,
            "numboxed": 2,
            "nummanuals": 3,
            "platform": "Platform",
            "notes": "Notes"
        }

        g = Game.from_dict(gd)

        expected_mappings = {
            "id": g.id,
            "datepurchased": g.date_purchased,
            "genre": g.genre,
            "title": g.title,
            "numcopies": g.num_copies,
            "numboxed": g.num_boxed,
            "nummanuals": g.num_manuals,
            "platform": g.platform,
            "notes": g.notes
        }

        for k, v in expected_mappings.items():
            self.assertEqual(gd[k], v)

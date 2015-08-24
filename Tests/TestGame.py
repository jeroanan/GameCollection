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

import json
import unittest

from Game import Game


class TestGame(unittest.TestCase):
    """Unit tests for the Game class"""

    def test_from_mongo_result_performs_mapping(self):
        """Test that mapping a Game object from a MonoDB result is correct"""

        gd = {
            "_id": "id",
            "_Game__genre": "genre",
            "_Game__title": "title",
            "_Game__platform": "platform",
            "_Game__num_copies": 1,
            "_Game__num_boxed": 2,
            "_Game__num_manuals": 3,
            "_Game__notes": "notes",
            "_Game__date_purchased": "2015-05-23",
            "_Game__approximate_date_purchased": True
        }

        g = Game.from_mongo_result(gd)

        expected_mappings = {
            "_id": g.id,
            "_Game__title": g.title,
            "_Game__genre": g.genre,
            "_Game__platform": g.platform,
            "_Game__num_copies": g.num_copies,
            "_Game__num_boxed": g.num_boxed,
            "_Game__num_manuals": g.num_manuals,
            "_Game__notes": g.notes,
            "_Game__date_purchased": g.date_purchased,
            "_Game__approximate_date_purchased": g.approximate_date_purchased
        }
         
        for k,v in expected_mappings.items():
            self.assertEqual(gd[k], v)

    def test_from_dict(self):
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


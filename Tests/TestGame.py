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

from Game import Game


class TestGame(unittest.TestCase):
    
    def test_from_mongo_result_performs_mapping(self):
        gd = {"_id": "id",
              "_Game__title": "title",
              "_Game__platform": "platform",
              "_Game__num_copies": 1,
              "_Game__num_boxed": 2,
              "_Game__num_manuals": 3,
              "_Game__notes": "notes",
              "_Game__date_purchased": "2015-05-23",
              "_Game__approximate_date_purchased": True}

        g = Game.from_mongo_result(gd)
        self.assertEqual(gd["_id"], g.id)
        self.assertEqual(gd["_Game__title"], g.title)
        self.assertEqual(gd["_Game__platform"], g.platform)
        self.assertEqual(gd["_Game__num_copies"], g.num_copies)
        self.assertEqual(gd["_Game__num_boxed"], g.num_boxed)
        self.assertEqual(gd["_Game__num_manuals"], g.num_manuals)
        self.assertEqual(gd["_Game__notes"], g.notes)
        self.assertEqual(gd["_Game__date_purchased"], g.date_purchased)
        self.assertEqual(gd["_Game__approximate_date_purchased"], g.approximate_date_purchased)

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

from Interactors.Game.Params.GetGamesInteractorParams import GetGamesInteractorParams


class TestGetGamesInteractorParams(unittest.TestCase):
    """Unit tests for the GetGamesInteractorParams class"""

    def test_from_dict_maps_correctly(self):
        """Test that calling GetGamesInteractorParams.from dict correctly initialises
        GetGamesInteractorParams"""
        dictionary = {
            "number_of_games": 1,
            "sort_field": "field",
            "sort_direction": "backwards",
            "user_id": "user",
            "platform": "platform"
        }

        params = GetGamesInteractorParams.from_dict(dictionary)

        mappings = {
            "number_of_games": params.number_of_games,
            "sort_field": params.sort_field,
            "sort_direction": params.sort_direction,
            "user_id": params.user_id,
            "platform": params.platform
        }

        list(map(lambda m: self.assertEqual(dictionary[m], mappings[m]), mappings))



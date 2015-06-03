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

from Interactors.Hardware.Params.GetHardwareListInteractorParams import GetHardwareListInteractorParams

class TestGetHardwareInteractorParams(unittest.TestCase):
    """Unit tests for the GetHardwareListInteractorParams class"""

    def test_from_dict_maps_correctly(self):
        """Test that an instance of GetHardwareListInteractorParams can be initialised correctly
       from a dictionary"""
        dictionary = {"sort_field": "description",
                      "sort_direction": "backwards",
                      "user_id": "userid",
                      "number_of_items": 1337}

        p = GetHardwareListInteractorParams.from_dict(dictionary)

        mappings = {"sort_field": p.sort_field,
                    "sort_direction": p.sort_direction,
                    "user_id": p.user_id,
                    "number_of_items": p.number_of_items}

        list(map(lambda m: self.assertEqual(dictionary[m], mappings[m]), mappings))

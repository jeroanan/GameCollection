# Copyright (c) 2015 David Wilson
# This file is part of Icarus.

# Icarus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Icarus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Icarus.  If not, see <http://www.gnu.org/licenses/>

import unittest

from Hardware import Hardware
from Tests.Persistence.Mappers.MapTools import get_map_checker
from Persistence.Mappers.ResultToHardwareMapper import ResultToHardwareMapper


class TestResultToHardwareMapper(unittest.TestCase):

    def setUp(self):
        mongo_result = {"_id": "id", 
                        "_Hardware__name": "name", 
                        "_Hardware__platform": "platform",
                        "_Hardware__num_owned": "1",
                        "_Hardware__num_boxed": "2",
                        "_Hardware__notes": "notes"}
        target = ResultToHardwareMapper(mongo_result)
        self.__check_maps = get_map_checker(target)

    def test_mappings(self):
        mappings = {"id": "id",
                    "name": "name",
                    "platform": "platform",
                    "1": "num_owned",
                    "2": "num_boxed",
                    "notes": "notes"}
        for m in mappings:
            self.assertTrue(self.__check_maps(m, mappings[m]), "Failed to map {0}.".format(mappings[m]))
        

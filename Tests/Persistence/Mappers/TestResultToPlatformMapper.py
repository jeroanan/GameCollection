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
from Tests.Persistence.Mappers.MapTools import get_map_checker
from Persistence.Mappers.ResultToPlatformMapper import ResultToPlatformMapper
from Platform import Platform


class TestResultToPlatformMapper(unittest.TestCase):

    def setUp(self):
        self.__mongo_result = {"_id": "id", 
                               "_Platform__name": "Name", 
                               "_Platform__description": "Description"}
        self.__target = ResultToPlatformMapper(self.__mongo_result)
        self.__check_maps = get_map_checker(self.__target)

    def test_mappings(self):
        mappings = {"id": "id",
                    "Name": "name",
                    "Description": "description"}
        for m in mappings:
            self.assertTrue(self.__check_maps(m, mappings[m]), "Failed to map {0}.".format(mappings[m]))

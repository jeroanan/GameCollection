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
from Persistence.Mappers.ResultToHardwareMapper import ResultToHardwareMapper


class TestResultToHardwareMapper(unittest.TestCase):
    
    def setUp(self):
        self.__mongo_result = {"_id": "id", 
                               "_Hardware__name": "name", 
                               "_Hardware__platform": "platform",
                               "_Hardware__num_owned": "1",
                               "_Hardware__num_boxed": "2",
                               "_Hardware__notes": "notes"}
        self.__target = ResultToHardwareMapper(self.__mongo_result)

    def test_maps_id(self):
        self.__assert_field_maps("id", "id")

    def test_map_none_id_leaves_as_default(self):
        self.__assert_none_mapped_leaves_default("_id", "id")

    def test_maps_hardware_name(self):
        self.__assert_field_maps("name", "name")        

    def test_map_none_hardware_name_leaves_as_default(self):
        self.__assert_none_mapped_leaves_default("_Hardware__name", "name")

    def test_maps_platform(self):
        self.__assert_field_maps("platform", "platform")

    def test_map_none_platform_leaves_as_default(self):
        self.__assert_none_mapped_leaves_default("_Hardware__platform", "platform")

    def test_maps_num_owned(self):
        self.__assert_field_maps("1", "num_owned")

    def test_map_none_num_owned_leaves_as_default(self):
        self.__assert_none_mapped_leaves_default("_Hardware__num_owned", "num_owned")

    def test_map_num_boxed_maps_num_(self):
        self.__assert_field_maps("2", "num_boxed")

    def test_map_none_num_boxed_leaves_as_default(self):
        self.__assert_none_mapped_leaves_default("_Hardware__num_boxed", "num_boxed")

    def test_map_notes_maps_notes(self):
        self.__assert_field_maps("notes", "notes")
        
    def test_map_none_notes_leaves_as_default(self):
        self.__assert_none_mapped_leaves_default("_Hardware__notes", "notes")

    def __assert_field_maps(self, expected_value, field_name):
        mapped = self.__target.map()
        self.assertEqual(expected_value, getattr(mapped, field_name))

    def __assert_none_mapped_leaves_default(self, mongo_field_name, mapped_field_name):
        h = Hardware()
        del(self.__mongo_result[mongo_field_name])
        mapper = ResultToHardwareMapper(self.__mongo_result)
        mapped = mapper.map()
        self.assertEqual(getattr(h, mapped_field_name), getattr(mapped, mapped_field_name))

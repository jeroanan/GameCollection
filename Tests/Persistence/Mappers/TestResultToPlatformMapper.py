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
from Persistence.Mappers.ResultToPlatformMapper import ResultToPlatformMapper
from Platform import Platform


class TestResultToPlatformMapper(unittest.TestCase):

    def setUp(self):
        self.__mongo_result = {"_id": "id", 
                               "_Platform__name": "Name", 
                               "_Platform__description": "Description"}
        self.__target = ResultToPlatformMapper(self.__mongo_result)

    def test_maps_id(self):
        self.__assert_field_maps("id", "id")

    def test_map_none_id_leaves_as_default(self):
        self.__assert_none_mapped_leaves_default("_id", "id")

    def test_maps_name(self):        
        self.__assert_field_maps("Name", "name")

    def test_map_none_name_leaves_as_default(self):
        self.__assert_none_mapped_leaves_default("_Platform__name", "name")

    def test_maps_description(self):
        self.__assert_field_maps("Description", "description")

    def test_none_description_leaves_as_Default(self):
        self.__assert_none_mapped_leaves_default("_Platform__description", "description")

    def __assert_field_maps(self, expected_value, field_name):
        mapped = self.__target.map()
        self.assertEqual(expected_value, getattr(mapped, field_name))

    def __assert_none_mapped_leaves_default(self, mongo_field_name, mapped_field_name):
        h = Platform()
        del(self.__mongo_result[mongo_field_name])
        mapper = ResultToPlatformMapper(self.__mongo_result)
        mapped = mapper.map()
        self.assertEqual(getattr(h, mapped_field_name), getattr(mapped, mapped_field_name))

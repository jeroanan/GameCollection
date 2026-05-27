"""Provides unit tests for the MongoPersistence class."""
# Copyright (c) 2026 David Wilson
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
from unittest.mock import Mock
from logging import Logger
from pymongo import MongoClient 

from data.config import Config
from genre import Genre
from hardware_type import HardwareType
from persistence.mongo_persistence import MongoPersistence

class TestMongoPersistence(unittest.TestCase):
    """Unit tests for the MongoPersistence class."""
    def setUp(self) -> None:
        self.logger = Mock(Logger)
        self.config = Mock(Config)
        self.mongo_client = Mock(MongoClient)
        self.mongo_client.GamesCollection = Mock()
        self.mongo_persistence: MongoPersistence = MongoPersistence(
            logger=self.logger,
            config=self.config,
            mongo_client=self.mongo_client)

    def test_constructs(self) -> None:
        """Tests that the MongoPersistence constructs correctly."""
        self.assertIsNotNone(self.mongo_persistence)

    ## Genres

    def test_from_mongo_result_returns_genre(self) -> None:
        """Tests that from_mongo_result returns a Genre instance"""
        g = self.mongo_persistence.genre_from_mongo_result({"": ""})
        self.assertIsInstance(g, Genre)

    def test_genre_from_mongo_result_does_mappings(self) -> None:
        """Tests that from_mongo_result maps dictionary keys to Genre attributes"""
        d = {"_id": "id",
             "_Genre__name": "name",
             "_Genre__description": "description"}
        g = self.mongo_persistence.genre_from_mongo_result(d)
        self.assertEqual(d["_id"], g.id)
        self.assertEqual(d["_Genre__name"], g.name)
        self.assertEqual(d["_Genre__description"], g.description)

    def test_from_mongo_result_returns_hardware_type(self) -> None:
        """Tests that from_mongo_result returns a HardwareType instance."""
        hardware_type = self.mongo_persistence.hardware_type_from_mongo_result({"":""})
        self.assertIsInstance(hardware_type, HardwareType)

    def test_from_mongo_result_maps_correctly(self) -> None:
        """Tests that from_mongo_result performs correct mappings."""
        mongo_result = {"_id": "id",
                        "_HardwareType__name": "name",
                        "_HardwareType__description": "description"}

        expected = {"id": mongo_result["_id"],
                    "name": mongo_result["_HardwareType__name"],
                    "description": mongo_result["_HardwareType__description"]}

        hardware_type = self.mongo_persistence.hardware_type_from_mongo_result(mongo_result)

        list(map(lambda x: self.assertEqual(expected[x], getattr(hardware_type, x), x), expected))

    def test_hardware_from_mongo_result_performs_mapping(self) -> None:
        """Mapping mongo result to Hardware object properly initialises object."""

        hd = {
            "_id": "id",
            "_Hardware__name": "name",
            "_Hardware__platform": "platform",
            "_Hardware__num_owned": 1,
            "_Hardware__num_boxed": 2,
            "_Hardware__notes": "notes",
            "_Hardware__hardware_type": "ht"
        }

        h = self.mongo_persistence.hardware_from_mongo_result(hd)

        expected_mappings = {
            "_id": h.id,
            "_Hardware__name": h.name,
            "_Hardware__platform": h.platform,
            "_Hardware__num_owned": h.num_owned,
            "_Hardware__num_boxed": h.num_boxed,
            "_Hardware__notes": h.notes,
            "_Hardware__hardware_type": h.hardware_type
        }

        for k, v in expected_mappings.items():
            self.assertEqual(hd[k], v)

    def test_platform_from_mongo_result_performs_mapping(self) -> None:
        """Initialise the mapper
        :param mongo_result: A MongoDB result. The following fields
        can currently be mapped:
          * _id
          * _Platform__name
          * _Platform__description
        """
        d = {"_id": "id",
             "_Platform__name": "name",
             "_Platform__description": "description"}
        p = self.mongo_persistence.platform_from_mongo_result(d)
        self.assertEqual(d["_id"], p.id)
        self.assertEqual(d["_Platform__name"], p.name)
        self.assertEqual(d["_Platform__description"], p.description)

    def test_user_from_mongo_result_does_mapping(self) -> None:
        """Mongo result maps to User object"""
        ud = {"_id": "id",
              "_User__user_id": "user_id",
              "_User__password": "password"}
        user = self.mongo_persistence.user_from_mongo_result(ud)
        self.assertEqual(ud["_id"], user.id)
        self.assertEqual(ud["_User__user_id"], user.user_id)
        self.assertEqual(ud["_User__password"], user.password)

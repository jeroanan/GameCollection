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

from logging import Logger
from pymongo import MongoClient
import unittest
from unittest.mock import Mock

from Data.Config import Config;
from Persistence.MongoPersistence import MongoPersistence

class TestMongoPersistence(unittest.TestCase):

    def setUp(self):
        self.logger = Mock(Logger)
        self.config = Mock(Config)
        self.mongo_client = Mock(MongoClient)
        self.mongo_client.GamesCollection = Mock()
        self.mongo_persistence = MongoPersistence(logger=self.logger, config=self.config, mongo_client=self.mongo_client)

    def tearDown(self):
        self.mongo_persistence = None

    def test_constructs(self):
        self.assertIsNotNone(self.mongo_persistence)
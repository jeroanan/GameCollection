from logging import Logger
from unittest import TestCase
from unittest.mock import MagicMock

from pymongo import MongoClient

from data.config import Config
from persistence.mongo_persistence import MongoPersistence

class MongoTestBase(TestCase):
    """Base class for MongoPersistence tests."""
    def setUp(self) -> None:
        self.logger = MagicMock(Logger)
        self.config = MagicMock(Config)
        self.mongo_client = MagicMock(MongoClient)
        self.mongo_client.GamesCollection = MagicMock()

        self.mongo_persistence = MongoPersistence(
            logger=self.logger,
            config=self.config,
            mongo_client=self.mongo_client)

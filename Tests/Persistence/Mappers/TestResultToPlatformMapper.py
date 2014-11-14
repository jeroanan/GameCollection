import unittest
from Persistence.Mappers.ResultToPlatformMapper import ResultToPlatformMapper
from Platform import Platform


class TestResultToPlatformMapper(unittest.TestCase):
    def test_map_returns_platform(self):
        mongo_result = {"_id": "id", "_Platform__name": "Name", "_Platform__description": "Description"}
        target = ResultToPlatformMapper()
        platform = target.map(mongo_result)
        self.assertIsInstance(platform, Platform)
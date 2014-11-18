import unittest
from unittest.mock import Mock
from Interactors.GetPlatformInteractor import GetPlatformInteractor
from Interactors.Interactor import Interactor
from Persistence.MongoPersistence import MongoPersistence


class TestGetPlatformInteractor(unittest.TestCase):

    def setUp(self):
        self.__persistence = Mock(MongoPersistence)
        self.__target = GetPlatformInteractor()
        self.__target.persistence = self.__persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_get_platform(self):
        self.__target.execute(platform_id="platformId")
        self.assertTrue(self.__persistence.get_platform.called)



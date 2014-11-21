import unittest
from unittest.mock import Mock
from Interactors.Interactor import Interactor
from Interactors.UpdatePlatformInteractor import UpdatePlatformInteractor
from Persistence.MongoPersistence import MongoPersistence
from Platform import Platform


class TestUpdatePlatformInteractor(unittest.TestCase):

    def setUp(self):
        self.__target = UpdatePlatformInteractor()
        self.__persistence = Mock(MongoPersistence)
        self.__target.persistence = self.__persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute(self):
        self.__target.execute(platform=Platform())

    def test_execute_calls_persistence_update_platform(self):
        platform = Platform()
        self.__target.execute(platform)
        self.__persistence.update_platform.assert_called_with(platform)
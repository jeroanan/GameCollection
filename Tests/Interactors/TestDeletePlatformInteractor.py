import unittest
from unittest.mock import Mock
from Interactors.DeletePlatformInteractor import DeletePlatformInteractor
from Interactors.Interactor import Interactor
from Persistence.MongoPersistence import MongoPersistence
from Platform import Platform


class TestDeletePlatformInteractor(unittest.TestCase):

    def setUp(self):
        self.__target = DeletePlatformInteractor()
        self.__persistence = Mock(MongoPersistence)
        self.__target.persistence = self.__persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        platform = Platform()
        self.__target.execute(platform=platform)
        self.__persistence.delete_platform.assert_called_with(platform)

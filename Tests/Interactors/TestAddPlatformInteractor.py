import unittest
from unittest.mock import Mock
from Interactors.AddPlatformInteractor import AddPlatformInteractor
from Interactors.Interactor import Interactor
from Persistence.MongoPersistence import MongoPersistence
from Platform import Platform


class TestAddPlatformInteractor(unittest.TestCase):

    def setUp(self):
        self.__persistence = Mock(MongoPersistence)
        self.__target = AddPlatformInteractor()
        self.__target.persistence = self.__persistence

    def test_is_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence(self):
        self.__target.execute(Platform())
        self.assertTrue(self.__persistence.add_platform.called)
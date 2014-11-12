import unittest
from unittest.mock import Mock
from Interactors.Interactor import Interactor
from Persistence.MongoPersistence import MongoPersistence


class AddPlatformInteractor(Interactor):
    def execute(self, name, description):
        self.persistence.add_platform(name, description)


class TestAddPlatformInteractor(unittest.TestCase):

    def setUp(self):
        self.__persistence = Mock(MongoPersistence)
        self.__target = AddPlatformInteractor()
        self.__target.persistence = self.__persistence

    def test_is_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence(self):
        self.__target.execute("name", "description")
        self.assertTrue(self.__persistence.add_platform.called)
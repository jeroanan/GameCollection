import unittest
from unittest.mock import Mock

from Interactors.GetHardwareListInteractor import GetHardwareListInteractor
from Interactors.Interactor import Interactor
from Persistence.MongoPersistence import MongoPersistence


class TestGetHardwareListInteractor(unittest.TestCase):

    def setUp(self):
        self.__target = GetHardwareListInteractor()
        self.__persistence = Mock(MongoPersistence)
        self.__target.persistence = self.__persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute(self):
        self.__target.execute()

    def test_execute_calls_persistence(self):
        self.__target.execute()
        self.__persistence.get_hardware_list.assert_called_with()
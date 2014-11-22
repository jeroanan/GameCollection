import unittest
from unittest.mock import Mock
from Interactors.GetHardwareInteractor import GetHardwareDetailsInteractor
from Interactors.Interactor import Interactor
from Persistence.MongoPersistence import MongoPersistence


class TestGetHardwareDetailsInteractor(unittest.TestCase):

    def setUp(self):
        self.__persistence = Mock(MongoPersistence)
        self.__target = GetHardwareDetailsInteractor()
        self.__target.persistence = self.__persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        self.__target.execute(platform_id="platformid")
        self.__persistence.get_hardware_details.assert_called_with("platformid")
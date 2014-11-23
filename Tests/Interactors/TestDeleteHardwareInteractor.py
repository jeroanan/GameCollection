import unittest
from unittest.mock import Mock
from Interactors.DeleteHardwareInteractor import DeleteHardwareInteractor
from Interactors.Interactor import Interactor
from Persistence.MongoPersistence import MongoPersistence


class TestDeleteHardwareInteractor(unittest.TestCase):

    def setUp(self):
        self.__persistence = Mock(MongoPersistence)
        self.__target = DeleteHardwareInteractor()
        self.__target.persistence = self.__persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        hardwareid = "hardwareid"
        self.__target.execute(hardware_id=hardwareid)
        self.__persistence.delete_hardware.assert_called_with(hardwareid)

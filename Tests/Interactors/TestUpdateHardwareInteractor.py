import unittest
from unittest.mock import Mock
from Hardware import Hardware
from Interactors.Interactor import Interactor
from Interactors.UpdateHardwareInteractor import UpdateHardwareInteractor
from Persistence.MongoPersistence import MongoPersistence


class TestUpdateHardwareInteractor(unittest.TestCase):

    def setUp(self):
        self.__persistence = Mock(MongoPersistence)
        self.__target = UpdateHardwareInteractor()
        self.__target.persistence = self.__persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        hardware = Hardware()
        self.__target.execute(hardware=hardware)
        self.__persistence.update_hardware.assert_called_with(hardware)

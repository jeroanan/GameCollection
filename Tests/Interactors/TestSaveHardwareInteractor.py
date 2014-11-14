import unittest
from unittest.mock import Mock
from Hardware import Hardware
from Interactors.Interactor import Interactor
from Interactors.SaveHardwareInteractor import SaveHardwareInteractor
from Persistence.MongoPersistence import MongoPersistence


class TestSaveHardwareInteractor(unittest.TestCase):

    def setUp(self):
        self.__persistence = Mock(MongoPersistence)
        self.__target = SaveHardwareInteractor()
        self.__target.persistence = self.__persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence(self):
        hardware = Hardware()
        self.__target.execute(hardware)
        self.assertTrue(self.__persistence.save_hardware.called)

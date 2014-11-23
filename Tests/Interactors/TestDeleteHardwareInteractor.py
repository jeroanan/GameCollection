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

    def test_execute_with_none_hardware_id_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_with_empty_hardware_id_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, "")

    def test_execute_with_whitespace_hardware_id_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, " ")

    def test_execute_calls_persistence_method(self):
        hardwareid = "hardwareid"
        self.__target.execute(hardware_id=hardwareid)
        self.__persistence.delete_hardware.assert_called_with(hardwareid)

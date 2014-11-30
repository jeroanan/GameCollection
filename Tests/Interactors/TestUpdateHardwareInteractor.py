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
        hardware = self.__get_hardware()
        self.__target.execute(hardware=hardware)
        self.__persistence.update_hardware.assert_called_with(hardware)

    def test_execute_with_none_hardware_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_with_none_name_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_hardware(name=None))

    def test_execute_with_empty_name_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_hardware(name=""))

    def test_execute_with_whitespace_name_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_hardware(name=" "))

    def test_execute_with_none_platform_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_hardware(platform=None))

    def test_execute_with_empty_platform_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_hardware(platform=""))

    def test_execute_with_whitespace_platform_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_hardware(platform=" "))

    def test_execute_with_none_numowned_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_hardware(num_owned=None))

    def test_execute_with_string_numowned_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_hardware(num_owned="wrong"))

    def test_execute_with_none_numboxed_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_hardware(num_boxed=None))

    def test_execute_with_string_numboxed_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_hardware(num_boxed="wrong"))

    def __get_hardware(self, name="name", platform="platform", num_owned=0, num_boxed=0):
        hardware = Hardware()
        hardware.name = name
        hardware.platform = platform
        hardware.numowned = num_owned
        hardware.numboxed = num_boxed
        return hardware
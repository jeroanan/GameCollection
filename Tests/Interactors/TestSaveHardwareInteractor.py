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
        self.__target.execute(self.__get_hardware())
        self.assertTrue(self.__persistence.save_hardware.called)

    def test_execute_with_null_hardware_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_with_id_set_raises_value_error(self):
        self.__assert_value_error(self.__get_hardware(hardware_id="id"))

    def test_execute_with_none_name_raises_value_error(self):
        self.__assert_value_error(self.__get_hardware(name=None))

    def test_execute_with_empty_name_raises_value_error(self):
        self.__assert_value_error(self.__get_hardware(name=""))

    def test_execute_with_whitespace_name_raises_value_error(self):
        self.__assert_value_error(self.__get_hardware(name=" "))

    def test_execute_with_none_platform_raises_value_error(self):
        self.__assert_value_error(self.__get_hardware(platform=None))

    def test_execute_with_empty_platform_raises_value_error(self):
        self.__assert_value_error(self.__get_hardware(platform=""))

    def test_execute_with_whitespace_platform_name_raises_value_error(self):
        self.__assert_value_error(self.__get_hardware(platform=" "))

    def __assert_value_error(self, hardware):
        self.assertRaises(ValueError, self.__target.execute, hardware)

    def __get_hardware(self, hardware_id="", name="name", platform="platform"):
        hardware = Hardware()
        hardware.id = hardware_id
        hardware.name = name
        hardware.platform = platform
        return hardware
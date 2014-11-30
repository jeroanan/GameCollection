import unittest
from unittest.mock import Mock
from Interactors.Interactor import Interactor
from Interactors.UpdatePlatformInteractor import UpdatePlatformInteractor
from Persistence.MongoPersistence import MongoPersistence
from Platform import Platform


class TestUpdatePlatformInteractor(unittest.TestCase):

    def setUp(self):
        self.__target = UpdatePlatformInteractor()
        self.__persistence = Mock(MongoPersistence)
        self.__target.persistence = self.__persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_update_platform(self):
        platform = self.__get_platform()
        self.__target.execute(platform)
        self.__persistence.update_platform.assert_called_with(platform)

    def test_execute_with_none_platform_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_with_none_name_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_platform(name=None))

    def test_execute_with_empty_name_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_platform(name=""))

    def test_execute_with_whitespace_name_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_platform(name=" "))

    def __get_platform(self, name="name"):
        p = Platform()
        p.name = name
        return p
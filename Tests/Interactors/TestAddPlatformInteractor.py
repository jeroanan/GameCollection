import unittest
from unittest.mock import Mock
from Interactors.AddPlatformInteractor import AddPlatformInteractor
from Interactors.Interactor import Interactor
from Persistence.MongoPersistence import MongoPersistence
from Platform import Platform


class TestAddPlatformInteractor(unittest.TestCase):

    def setUp(self):
        self.__persistence = Mock(MongoPersistence)
        self.__target = AddPlatformInteractor()
        self.__target.persistence = self.__persistence

    def test_is_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_with_none_platform_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_with_non_blank_id_raises_value_error(self):
        platform = Platform()
        platform.id = "id"
        platform.name = "platform"
        self.assertRaises(ValueError, self.__target.execute, platform)

    def test_execute_with_none_platform_name_raises_value_error(self):
        platform = self.__get_platform(None)
        self.assertRaises(ValueError, self.__target.execute, platform)

    def test_execute_with_empty_platform_name_raises_value_error(self):
        platform = self.__get_platform(name="")
        self.assertRaises(ValueError, self.__target.execute, platform)

    def test_execute_with_whitespace_platform_name_raises_value_error(self):
        platform = self.__get_platform(name=" ")
        self.assertRaises(ValueError, self.__target.execute, platform)

    def test_execute_calls_persistence(self):
        platform = self.__get_platform(name="platform")
        self.__target.execute(platform)
        self.assertTrue(self.__persistence.add_platform.called)

    def __get_platform(self, name=""):
        platform = Platform()
        platform.name = name
        return platform
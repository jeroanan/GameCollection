import unittest
from unittest.mock import Mock
from Interactors.DeletePlatformInteractor import DeletePlatformInteractor
from Interactors.Interactor import Interactor
from Persistence.MongoPersistence import MongoPersistence
from Platform import Platform


class TestDeletePlatformInteractor(unittest.TestCase):

    def setUp(self):
        self.__target = DeletePlatformInteractor()
        self.__persistence = Mock(MongoPersistence)
        self.__target.persistence = self.__persistence

    def test_is_instance_of_interactor(self):
        self.assertIsInstance(self.__target, Interactor)

    def test_execute_calls_persistence_method(self):
        platform = Platform()
        platform.id = "id"
        self.__target.execute(platform=platform)
        self.__persistence.delete_platform.assert_called_with(platform)

    def test_execute_with_none_platform_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_with_none_id_raises_value_error(self):
        self.__assert_platform_id_invalid_value_throws_value_error(None)

    def test_execute_with_empty_id_raises_value_error(self):
        self.__assert_platform_id_invalid_value_throws_value_error("")

    def test_execute_with_whitespace_id_raises_value_error(self):
        self.__assert_platform_id_invalid_value_throws_value_error(" ")

    def __assert_platform_id_invalid_value_throws_value_error(self, platform_id):
        platform = Platform()
        platform.id = platform_id
        self.assertRaises(ValueError, self.__target.execute, platform)
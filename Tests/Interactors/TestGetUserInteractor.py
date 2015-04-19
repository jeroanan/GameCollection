import unittest
from unittest.mock import Mock

from AbstractPersistence import AbstractPersistence
from Interactors.Interactor import Interactor
from Interactors.User.GetUserInteractor import GetUserInteractor
from Tests.Interactors.InteractorTestBase import InteractorTestBase
from User import User
        

class TestGetUserInteractor(InteractorTestBase):
    
    def setUp(self):
        self.__persistence = Mock(AbstractPersistence)
        self.__target = GetUserInteractor()        
        self.__target.persistence = self.__persistence

    def test_is_interactor(self):
        self.assertIsInstance(self.__target, Interactor)
        
    def test_execute_with_null_user_raises_type_error(self):
        self.assertRaises(TypeError, self.__target.execute, None)

    def test_execute_with_empty_user_id_raises_value_error(self):
        self.assertRaises(ValueError, self.__target.execute, self.__get_user())

    def test_execute_with_user_id_gets_user_from_persistence(self):
        self.__target.execute(self.__get_user("userid"))
        self.assertTrue(self.__persistence.get_user.called)

    def __get_user(self, user_id="", password=""):
        u = User()
        u.user_id = user_id
        u.password = password
        return u

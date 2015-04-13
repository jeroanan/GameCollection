import unittest

from Persistence.Mappers.ResultToUserMapper import ResultToUserMapper
from User import User

class TestResultToUserMapper(unittest.TestCase):
    
    def setUp(self):
        self.__target = ResultToUserMapper()
  
    def test_map_returns_user_object(self):
        result = self.__target.map({})
        self.assertIsInstance(result, User)
    
    def test_map_id(self):
        id = "cba997ba-6033-a325-ec1b-e009b66a3b1b"
        result = self.__target.map({"_id": id})
        self.assertEqual(id, result.id)
        
    def test_map_user_id(self):
        user_id = "my_user"
        result = self.__target.map({"_User__user_id": user_id})
        self.assertEqual(user_id, result.user_id)

    def test_map_password(self):
        passwd = "mysupersecretpassword"
        result = self.__target.map({"_User__password": passwd})
        self.assertEqual(passwd, result.password)
    
    def test_map_empty_result_returns_empty_user(self):
        result = self.__target.map(None)
        self.assertEqual(User(), result)

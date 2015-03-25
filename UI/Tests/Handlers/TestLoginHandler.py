import unittest
from UI.Handlers.Handler import Handler
from UI.Handlers.LoginHandler import LoginHandler


class TestLoginHandler(unittest.TestCase):

    def setUp(self):
        self.__target = LoginHandler(None, None)

    def test_is_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page(self):
        self.__target.get_page()



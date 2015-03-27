import unittest
from unittest.mock import Mock
from UI.Handlers.Handler import Handler
from UI.Handlers.LoginHandler import LoginHandler
from UI.TemplateRenderer import TemplateRenderer


class TestLoginHandler(unittest.TestCase):

    def setUp(self):
        self.___renderer = Mock(TemplateRenderer)
        self.__target = LoginHandler(None, self.___renderer)

    def test_is_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page(self):
        self.__target.get_page(self.__get_args())

    def test_get_page_renders_login_screen(self):
        self.__target.get_page(self.__get_args())
        self.___renderer.render.assert_called_with("login.html")

    def __get_args(self):
        return {
            "userid": "user",
            "password": "password"
        }



from unittest.mock import Mock

from UI.Handlers.AddPlatformHandler.AddPlatformHandler import AddPlatformHandler
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerAddPlatform(WebServerTestBase):

    def setUp(self):
        super().setUp()
        self.__handler = Mock(AddPlatformHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)
        self.__platform_name = "name"
        self.__platform_description = "description"

    def test_addplatform_calls_handler_get_page(self):
        self.target.addplatform(**self.__get_params())
        self.__handler.get_page.assert_called_with(platform=(self.__get_params()))

    def __get_params(self):
        return {
            "name": self.__platform_name,
            "description": self.__platform_description
        }

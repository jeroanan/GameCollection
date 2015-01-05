from unittest.mock import Mock

from UI.Handlers.UpdatePlatformHandler.UpdatePlatformHandler import UpdatePlatformHandler
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerUpdatePlatform(WebServerTestBase):

    def setUp(self):
        super().setUp()
        self.__handler = Mock(UpdatePlatformHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_updateplatform_calls_handler_get_page(self):
        self.target.updateplatform(**self.__get_handler_params())
        self.__handler.get_page.assert_called_with(self.__get_handler_params())

    def __get_handler_params(self):
        return {
            "id": "id",
            "name": "name",
            "description": "description"
        }
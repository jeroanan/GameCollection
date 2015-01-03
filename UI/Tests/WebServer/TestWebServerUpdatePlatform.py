from unittest.mock import Mock
from UI.Handlers.UpdatePlatformHandler import UpdatePlatformHandler
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerUpdatePlatform(WebServerTestBase):

    def setUp(self):
        super().setUp()
        self.__handler = Mock(UpdatePlatformHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)
        self.__platform_id = "id"
        self.__platform_name = "name"
        self.__platform_description = "description"

    def test_updateplatform_calls_handler_get_page(self):
        self.target.updateplatform(id=self.__platform_id, name=self.__platform_name,
                                   description=self.__platform_description)

        self.__handler.get_page.assert_called_with(id=self.__platform_id, name=self.__platform_name,
                                                   description=self.__platform_description)
from unittest.mock import Mock
from UI.Handlers.DeletePlatformHandler import DeletePlatformHandler
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerDeletePlatform(WebServerTestBase):

    def setUp(self):
        super().setUp()
        self.__handler = Mock(DeletePlatformHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)
        self.__platform_id = "id"

    def test_deleteplatform_calls_handler_get_page(self):
        self.target.deleteplatform(**self.__get_args())
        self.__handler.get_page.assert_called_with(self.__get_args())

    def __get_args(self):
        return {
            "platformid": "id"
        }

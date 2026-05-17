"""Unit tests for the WebServer's DeletePlatform functionality."""
from unittest.mock import Mock
from test.web_server.web_server_test_base import WebServerTestBase
from ui.handlers.delete_platform_handler import DeletePlatformHandler


class TestWebServerDeletePlatform(WebServerTestBase):
    """Tests for the WebServer's DeletePlatform functionality."""

    def setUp(self):
        super().setUp()
        self.__handler = Mock(DeletePlatformHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_deleteplatform_calls_handler_get_page(self):
        """Tests that the DeletePlatform handler's get_page method is called correctly."""
        self.target.default(*("deleteplatform",), **self.__get_args())
        self.__handler.get_page.assert_called_with(self.__get_args())

    def __get_args(self):
        return {
            "platformid": "id"
        }

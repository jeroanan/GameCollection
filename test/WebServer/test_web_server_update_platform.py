"""Provides tests for the UpdatePlatformHandler in the WebServer module."""
from unittest.mock import Mock

from test.WebServer.web_server_test_base import WebServerTestBase
from ui.Handlers.update_platform_handler import UpdatePlatformHandler


class TestWebServerUpdatePlatform(WebServerTestBase):
    """Tests for the UpdatePlatformHandler in the WebServer module."""

    def setUp(self):
        super().setUp()
        self.__handler = Mock(UpdatePlatformHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_updateplatform_calls_handler_get_page(self):
        """Tests that the UpdatePlatformHandler's get_page method is called with correct
        parameters."""
        self.target.default(*("updateplatform",), **self.__get_handler_params())
        self.__handler.get_page.assert_called_with(self.__get_handler_params())

    def __get_handler_params(self):
        return {
            "id": "id",
            "name": "name",
            "description": "description"
        }

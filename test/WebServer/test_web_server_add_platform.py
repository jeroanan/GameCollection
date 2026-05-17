"""Provides tests for the WebServer AddPlatform functionality."""
from unittest.mock import Mock

from test.WebServer.web_server_test_base import WebServerTestBase
from ui.handlers.add_platform_handler import AddPlatformHandler


class TestWebServerAddPlatform(WebServerTestBase):
    """Tests for the WebServer AddPlatform functionality."""

    def setUp(self):
        super().setUp()
        self.__handler = Mock(AddPlatformHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)
        self.__platform_name = "name"
        self.__platform_description = "description"

    def test_addplatform_calls_handler_get_page(self):
        """tests that addplatform calls handler get_page"""
        self.target.default(*("addplatform",), **self.__get_params())
        self.__handler.get_page.assert_called_with(self.__get_params())

    def __get_params(self):
        return {
            "name": self.__platform_name,
            "description": self.__platform_description
        }

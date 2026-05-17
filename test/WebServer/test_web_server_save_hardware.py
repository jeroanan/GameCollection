"""Provides tests for WebServer SaveHardware functionality."""
from unittest.mock import Mock

from test.WebServer.web_server_test_base import WebServerTestBase
from ui.handlers.save_hardware_handler import SaveHardwareHandler


class TestWebServerSaveHardware(WebServerTestBase):
    """Tests for the WebServer SaveHardware functionality."""

    def setUp(self):
        super().setUp()
        self.__handler = Mock(SaveHardwareHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_savehardware_calls_handler_get_page(self):
        """Tests that the savehardware handler's get_page method is called with the correct
        parameters."""
        self.target.default(*("savehardware",), **self.__get_params())
        self.__handler.get_page.assert_called_with(self.__get_params())

    def __get_params(self):
        return {
            "name": "name",
            "platform": "platform",
            "numowned": 1,
            "numboxed": 2,
            "notes": "notes"
        }

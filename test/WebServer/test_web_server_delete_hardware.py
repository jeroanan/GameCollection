"""Tests for the WebServer's DeleteHardware functionality."""
from unittest.mock import Mock
from test.WebServer.web_server_test_base import WebServerTestBase
from ui.handlers.delete_hardware_handler import DeleteHardwareHandler


class TestWebServerDeleteHardware(WebServerTestBase):
    """Tests for the WebServer's DeleteHardware functionality."""

    def setUp(self):
        super().setUp()
        self.__handler = Mock(DeleteHardwareHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_delete_hardware_calls_handler(self):
        """Tests that the DeleteHardware handler's get_page method is called correctly."""
        self.target.default(*("deletehardware",), **self.__get_args())
        self.__handler.get_page.assert_called_with(self.__get_args())

    def __get_args(self):
        return {
            "hardwareid": "id"
        }

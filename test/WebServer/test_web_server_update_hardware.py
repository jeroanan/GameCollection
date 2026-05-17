"""Tests for WebServer UpdateHardware page."""
from unittest.mock import Mock

from test.WebServer.web_server_test_base import WebServerTestBase
from ui.Handlers.update_hardware_handler import UpdateHardwareHandler


class TestWebServerUpdateHardware(WebServerTestBase):
    """Tests for WebServer UpdateHardware page."""

    def setUp(self):
        super().setUp()
        self.__handler = Mock(UpdateHardwareHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_updatehardware_calls_handler_get_page(self):
        """Tests that the updatehardware handler's get_page method is called with the correct
        parameters."""
        self.target.default(*("updatehardware",), **self.__get_params())
        self.__handler.get_page.assert_called_with(self.__get_params())

    def __get_params(self):
        return {
            "id": "id",
            "name": "name",
            "platform": "platform",
            "numowned": 1,
            "numboxed": 0,
            "notes": "notes"
        }

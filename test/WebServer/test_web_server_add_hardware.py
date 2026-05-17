"""Provides unit tests for the WebServer's AddHardware functionality."""
from unittest.mock import Mock
from test.WebServer.web_server_test_base import WebServerTestBase
from ui.Handlers.add_hardware_handler import AddHardwareHandler


class TestWebServerAddHardware(WebServerTestBase):
    """Unit tests for the WebServer's AddHardware functionality."""

    def test_addhardware_calls_handler_get_page(self):
        """Tests that the AddHardware handler's get_page method is called correctly."""
        handler = Mock(AddHardwareHandler)
        self.target.handler_factory = self.get_handler_factory(handler)
        self.target.default(*("addhardware",))
        handler.get_page.assert_called_with({})

    def test_addhardware_extra_args(self):
        """Tests that extra arguments are passed correctly to the AddHardware handler."""
        self.target.default(*("addhardware",), **{"spam": "eggs"})

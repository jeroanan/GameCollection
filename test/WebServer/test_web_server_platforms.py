"""Tests for WebServer platforms page."""
from unittest.mock import Mock

from test.WebServer.web_server_test_base import WebServerTestBase
from ui.Handlers.AddPlatformHandler import AddPlatformHandler


class TestWebServerPlatforms(WebServerTestBase):
    """Tests for the platforms page of the web server UI."""

    def test_platforms_calls_handler_get_page(self):
        """Tests that the platforms page calls the handler's get_page method."""
        handler = Mock(AddPlatformHandler)
        self.target.handler_factory = self.get_handler_factory(handler)
        self.target.default(*("platforms",))
        handler.get_page.assert_called_with({})

    def test_platforms_extra_args(self):
        """Tests that extra arguments are passed to the handler's get_page method."""
        self.target.default(*("platforms",), **{"spam": "eggs"})

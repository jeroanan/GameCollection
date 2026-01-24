"""Provides tests for the WebServer UpdateGame page."""
from unittest.mock import Mock

from test.WebServer.web_server_test_base import WebServerTestBase
from UI.Handlers.UpdateGameHandler import UpdateGameHandler


class TestWebServerUpdateGame(WebServerTestBase):
    """Tests for the WebServer UpdateGame page."""

    def setUp(self):
        super().setUp()
        self.__handler = Mock(UpdateGameHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_updategame_calls_handler_get_page(self):
        """Tests that the updategame handler's get_page method is called with the correct
        parameters."""
        self.target.default(*("updategame",), **self.__get_params())
        self.__handler.get_page.assert_called_with(self.__get_params())

    def __get_params(self):
        p = {
            "id": "id",
            "title": "title",
            "platform": "platform",
            "numcopies": 1,
            "numboxed": 2,
            "nummanuals": 3,
            "notes": "notes"
        }
        return p

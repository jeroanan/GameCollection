"""Provides tests for the WebServer's AddGame functionality."""
from test.web_server.web_server_test_base import WebServerTestBase
from unittest.mock import Mock
from ui.handlers.add_game_handler import AddGameHandler


class TestWebServerAddGame(WebServerTestBase):
    """Tests for the WebServer's AddGame functionality."""

    def setUp(self):
        super().setUp()
        self.__handler = Mock(AddGameHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_add_game_calls_handler_get_page(self):
        """tests that addgame calls handler get_page"""
        self.target.default(*("addgame",), **{})
        self.__handler.get_page.assert_called_with({})

    def test_add_game_extra_args(self):
        """tests that addgame passes extra args to handler get_page"""
        self.target.default(*("addgame",), **{"spam": "eggs"})

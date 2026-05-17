"""Unit tests for WebServer DeleteGame page handler."""
from unittest.mock import Mock

from test.WebServer.web_server_test_base import WebServerTestBase
from ui.Handlers.delete_game_handler import DeleteGameHandler


class TestWebServerDeleteGame(WebServerTestBase):
    """Unit tests for WebServer DeleteGame page handler."""

    def setUp(self):
        super().setUp()
        self.__handler = Mock(DeleteGameHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_deletegame_calls_handler_get_page(self):
        """Tests that the DeleteGame handler's get_page method is called correctly."""
        self.target.default(*("deletegame",), **self.__get_args())
        self.__handler.get_page.assert_called_with(self.__get_args())

    def __get_args(self):
        return {
            "gameid": "id"
        }

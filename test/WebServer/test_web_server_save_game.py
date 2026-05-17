"""Tests for WebServer SaveGame page handling."""
from unittest.mock import Mock

from test.WebServer.web_server_test_base import WebServerTestBase
from ui.Handlers.save_game_handler import SaveGameHandler


class TestWebServerSaveGame(WebServerTestBase):
    """Tests for WebServer SaveGame page handling."""

    def setUp(self):
        super().setUp()
        self.__handler = Mock(SaveGameHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_savegame_calls_handler_get_page(self):
        """Tests that the savegame handler's get_page method is called with the correct
        parameters."""
        self.target.default(*("savegame",), **self.__get_args())
        self.__handler.get_page.assert_called_with(self.__get_args())

    def __get_args(self):
        return {
            "title": "title",
            "numcopies": 1,
            "numboxed": 2,
            "nummanuals": 3,
            "platform": "platform",
            "notes": "notes"
        }

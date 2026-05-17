"""Unit tests for WebServer EditGame page."""
from unittest.mock import Mock
from test.web_server.web_server_test_base import WebServerTestBase
from ui.handlers.edit_game_handler import EditGameHandler


class TestWebServerEditGame(WebServerTestBase):
    """Unit tests for WebServer EditGame page."""

    def setUp(self):
        super().setUp()
        self.__handler = Mock(EditGameHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_editgame_calls_handler_get_page(self):
        """Tests that the EditGame handler's get_page method is called correctly."""
        self.target.default(*("editgame",), **self.__get_args())
        self.__handler.get_page.assert_called_with(self.__get_args())

    def __get_args(self):
        return {
            "gameid": "id"
        }

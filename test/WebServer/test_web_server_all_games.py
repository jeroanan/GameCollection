"""Unit tests for the WebServer AllGames endpoint."""
from unittest.mock import Mock

from test.WebServer.web_server_test_base import WebServerTestBase
from UI.Handlers.AllGamesHandler import AllGamesHandler


class TestWebServerAllGames(WebServerTestBase):
    """Unit tests for the WebServer AllGames endpoint."""

    def setUp(self):
        super().setUp()
        self.__handler = Mock(AllGamesHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_allgames_calls_handler_get_page(self):
        """Tests that the AllGames endpoint calls the handler's get_page method."""
        self.target.default(*("allgames",), **self.__get_params())
        self.__handler.get_page.assert_called_with(self.__get_params())

    def __get_params(self):
        return {
            "gamesort": "title",
            "gamesortdir": "asc",
            "platform": "platform"
        }

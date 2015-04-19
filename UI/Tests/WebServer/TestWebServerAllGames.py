from unittest.mock import Mock

from UI.Handlers.AllGamesHandler import AllGamesHandler
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerAllGames(WebServerTestBase):

    def setUp(self):
        super().setUp()
        self.__handler = Mock(AllGamesHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_allgames_calls_handler_get_page(self):
        self.target.default(*("allgames",), **self.__get_params())
        self.__handler.get_page.assert_called_with(self.__get_params())

    def __get_params(self):
        return {
            "gamesort": "title",
            "gamesortdir": "asc",
            "platform": "platform"
        }

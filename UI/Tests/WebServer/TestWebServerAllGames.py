from unittest.mock import Mock
from UI.Handlers.AllGamesHandler import AllGamesHandler
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerAllGames(WebServerTestBase):

    def setUp(self):
        super().setUp()
        self.__handler = Mock(AllGamesHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)
        self.__sort_field = "title"
        self.__sort_dir = "asc"
        self.__platform = None

    def test_allgames_calls_handler_get_page(self):
        self.target.allgames(gamesort=self.__sort_field, gamesortdir=self.__sort_dir, platform=self.__platform)
        self.__handler.get_page.assert_called_with(sort_field=self.__sort_field, sort_direction=self.__sort_dir,
                                                   platform=self.__platform)

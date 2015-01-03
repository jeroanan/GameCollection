from unittest.mock import Mock
from UI.Handlers.DeleteGameHandler import DeleteGameHandler
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerDeleteGame(WebServerTestBase):

    def setUp(self):
        super().setUp()
        self.__handler = Mock(DeleteGameHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)
        self.__game_id = "id"

    def test_deletegame_calls_handler_get_page(self):
        self.target.deletegame(gameid=self.__game_id)
        self.__handler.get_page.assert_called_with(self.__game_id)
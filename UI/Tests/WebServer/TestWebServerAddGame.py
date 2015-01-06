from unittest.mock import Mock
from UI.Handlers.AddGameHandler import AddGameHandler
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerAddGame(WebServerTestBase):

    def setUp(self):
        super().setUp()
        self.__handler = Mock(AddGameHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_add_game_calls_handler_get_page(self):
        self.target.default(*("addgame",), **{})
        self.__handler.get_page.assert_called_with({})

    def test_add_game_extra_args(self):
        self.target.default(*("addgame",), **{"spam": "eggs"})

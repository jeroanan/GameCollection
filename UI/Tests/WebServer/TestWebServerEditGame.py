from unittest.mock import Mock
from UI.Handlers.EditGameHandler import EditGameHandler
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerEditGame(WebServerTestBase):

    def setUp(self):
        super().setUp()
        self.__handler = Mock(EditGameHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)
        self.__game_id = "id"

    def test_editgame_calls_handler_get_page(self):
        self.target.default(*("editgame",), **self.__get_args())
        self.__handler.get_page.assert_called_with(self.__get_args())

    def __get_args(self):
        return {
            "gameid": "id"
        }

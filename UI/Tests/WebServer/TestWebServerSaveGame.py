from unittest.mock import Mock

from UI.Handlers.SaveGameHandler import SaveGameHandler
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerSaveGame(WebServerTestBase):

    def setUp(self):
        super().setUp()
        self.__handler = Mock(SaveGameHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_savegame_calls_handler_get_page(self):
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
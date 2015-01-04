from unittest.mock import Mock

from UI.Handlers.UpdateGameHandler.UpdateGameHandler import UpdateGameHandler
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerUpdateGame(WebServerTestBase):

    def setUp(self):
        super().setUp()
        self.__handler = Mock(UpdateGameHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_updategame_calls_handler_get_page(self):
        self.target.updategame(**self.__get_params())

        self.__handler.get_page.assert_called_with(params=self.__get_params())

    def __get_params(self):
        p = {
            "id": "id",
            "title": "title",
            "platform": "platform",
            "numcopies": 1,
            "numboxed": 2,
            "nummanuals": 3,
            "notes": "notes"
        }
        return p
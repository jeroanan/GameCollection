from unittest.mock import Mock

from UI.Handlers.IndexHandler.IndexHandler import IndexHandler
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerIndex(WebServerTestBase):
    def setUp(self):
        super().setUp()
        self.__handler = Mock(IndexHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_index_calls_handler_get_page(self):
        self.target.default(*(), **self.__get_args())
        self.__handler.get_page.assert_called_with(self.__get_args())

    def __get_args(self):
        return {
            "gamesort": "title",
            "gamesortdirection": "asc",
            "hardwaresort": "name",
            "hardwaresortdirection": "asc"
        }


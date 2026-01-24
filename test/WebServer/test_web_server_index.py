"""Unit tests for the WebServer IndexHandler."""
from unittest.mock import Mock

from test.WebServer.web_server_test_base import WebServerTestBase
from UI.Handlers.IndexHandler import IndexHandler


class TestWebServerIndex(WebServerTestBase):
    """Unit tests for the WebServer IndexHandler."""
    def setUp(self):
        super().setUp()
        self.__handler = Mock(IndexHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_index_calls_handler_get_page(self):
        """Tests that the index handler's get_page method is called with the correct parameters."""
        self.target.default(*(), **self.__get_args())
        self.__handler.get_page.assert_called_with(self.__get_args())

    def __get_args(self):
        return {
            "gamesort": "title",
            "gamesortdirection": "asc",
            "hardwaresort": "name",
            "hardwaresortdirection": "asc"
        }

"""Unit tests for the WebServer Search page."""
from unittest.mock import Mock

from test.WebServer.web_server_test_base import WebServerTestBase
from ui.handlers.search_handler import SearchHandler


class TestWebServerSearch(WebServerTestBase):
    """Unit tests for the WebServer Search page."""

    def setUp(self):
        super().setUp()
        self.__handler = Mock(SearchHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_search_calls_handler_get_page(self):
        """Tests that the search handler's get_page method is called with the correct parameters."""
        self.target.default(*("search",), **self.__get_params())
        self.__handler.get_page.assert_called_with(self.__get_params())

    def __get_params(self):
        return {
            "searchterm": "search",
            "gamesort": "",
            "gamesortdir": "asc"
        }

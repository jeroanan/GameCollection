from unittest.mock import Mock

from UI.Handlers.SearchHandler import SearchHandler
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerSearch(WebServerTestBase):

    def setUp(self):
        super().setUp()
        self.__handler = Mock(SearchHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)
        self.__search_term = "search"
        self.__game_sort = ""
        self.__sort_dir = "asc"

    def test_search_calls_handler_get_page(self):
        self.target.default(*("search",), **self.__get_params())
        self.__handler.get_page.assert_called_with(self.__get_params())

    def __get_params(self):
        return {
            "searchterm": "search",
            "gamesort": "",
            "gamesortdir": "asc"
        }


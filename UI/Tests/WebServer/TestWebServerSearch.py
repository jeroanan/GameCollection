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
        self.target.search(searchterm=self.__search_term, gamesort=self.__game_sort, gamesortdir=self.__sort_dir)
        self.__handler.get_page.assert_called_with(search_term=self.__search_term, sort_field=self.__game_sort,
                                                   sort_dir=self.__sort_dir)

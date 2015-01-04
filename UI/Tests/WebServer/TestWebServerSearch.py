from unittest.mock import Mock
from UI.Handlers.SearchHandler.SearchHandler import SearchHandler
from UI.Handlers.SearchHandler.SearchHandlerParams import SearchHandlerParams
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
        self.__handler.get_page.assert_called_with(params=self.__get_params())

    def __get_params(self):
        p = SearchHandlerParams()
        p.search_term = self.__search_term
        p.sort_field = self.__game_sort
        p.sort_direction = self.__sort_dir
        return p


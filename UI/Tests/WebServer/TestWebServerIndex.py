from unittest.mock import Mock
from UI.Handlers.IndexHandler.IndexHandler import IndexHandler
from UI.Handlers.IndexHandler.IndexHandlerParams import IndexHandlerParams
from UI.Tests.WebServer.WebServerTestBase import WebServerTestBase


class TestWebServerIndex(WebServerTestBase):
    def setUp(self):
        super().setUp()
        self.__game_sort_field = "title"
        self.__game_sort_direction = "asc"
        self.__hardware_sort_field = "name"
        self.__hardware_sort_direction = "asc"
        self.__handler = Mock(IndexHandler)
        self.target.handler_factory = self.get_handler_factory(self.__handler)

    def test_index_calls_handler_get_page(self):
        self.target.index(gamesort=self.__game_sort_field, gamesortdir=self.__game_sort_direction,
                          hardwaresort=self.__hardware_sort_field, hardwaresortdir=self.__hardware_sort_direction)

        self.__handler.get_page.assert_called_with(self.__get_params())

    def __get_params(self):
        params = IndexHandlerParams()
        params.game_sort = self.__game_sort_field
        params.game_sort_direction = self.__game_sort_direction
        params.hardware_sort = self.__hardware_sort_field
        params.hardware_sort_direction = self.__hardware_sort_direction
        return params


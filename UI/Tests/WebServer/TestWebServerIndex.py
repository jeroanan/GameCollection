from unittest.mock import Mock
from UI.Handlers.IndexHandler import IndexHandler
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

        self.__handler.get_page.assert_called_with(game_sort=self.__game_sort_field,
                                                   game_sort_direction=self.__game_sort_direction,
                                                   hardware_sort=self.__hardware_sort_field,
                                                   hardware_sort_direction=self.__hardware_sort_direction)

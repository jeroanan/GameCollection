import unittest
from unittest.mock import Mock

from Interactors.InteractorFactory import InteractorFactory
from Interactors.SearchInteractor import SearchInteractor
from UI.Handlers.Handler import Handler
from UI.Handlers.SearchHandler.SearchHandler import SearchHandler
from UI.TemplateRenderer import TemplateRenderer


class TestSearchHandler(unittest.TestCase):
    def setUp(self):
        self.__interactor = Mock(SearchInteractor())
        self.__interactor.execute = Mock(return_value=[])
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = SearchHandler(self.__interactor_factory, self.__renderer)

    def test_is_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_execute_interactor(self):
        self.__get_page()
        self.__interactor.execute.assert_called_with(search_term="search", sort_field="title", sort_dir="asc")

    def test_get_page_calls_render_method(self):
        self.__get_page()
        self.__renderer.render.assert_called_with(template="search.html", title="Search Results", games=[],
                                                  search_term="search", query="searchterm=search",
                                                  game_sort_field="title", game_sort_direction="asc")

    def __get_page(self):
        self.__target.get_page(params=self.__get_params())

    def __get_params(self):
        return {
            "searchterm": "search",
            "gamesort": "title",
            "gamesortdir": "asc"
        }

    def test_get_page_with_empty_params(self):
        self.__target.get_page({"": ""})
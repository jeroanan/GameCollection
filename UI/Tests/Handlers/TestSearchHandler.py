import unittest
from unittest.mock import Mock
from Interactors.InteractorFactory import InteractorFactory
from Interactors.SearchInteractor import SearchInteractor
from UI.Handlers.Handler import Handler
from UI.Handlers.SearchHandler import SearchHandler
from UI.TemplateRenderer import TemplateRenderer


class TestSearchHandler(unittest.TestCase):

    def setUp(self):
        self.__interactor = Mock(SearchInteractor())
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = SearchHandler(self.__interactor_factory, self.__renderer)

    def test_is_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_execute_interactor(self):
        self.__target.get_page(search_term="search")
        self.__interactor.execute.assert_called_with("search")

    def test_get_page_calls_render_method(self):
        self.__target.get_page(search_term="search")
        self.assertTrue(self.__renderer.render.called)



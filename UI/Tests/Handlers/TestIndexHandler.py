import unittest
from unittest.mock import Mock
from Interactors.GetGamesInteractor import GetGamesInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.Handler import Handler
from UI.Handlers.IndexHandler import IndexHandler
from UI.TemplateRenderer import TemplateRenderer


class TestIndexHandler(unittest.TestCase):

    def setUp(self):
        self.__interactor = Mock(GetGamesInteractor)
        self.__renderer = Mock(TemplateRenderer)
        self.__create_index_handler()

    def __create_index_handler(self):
        factory = Mock(InteractorFactory)
        factory.create = Mock(return_value=self.__interactor)
        self.__target = IndexHandler(factory, self.__renderer)

    def test_get_page_executes_interactor(self):
        self.__target.get_page()
        self.assertTrue(self.__interactor.execute.called)

    def test_get_page_calls_renderer(self):
        self.__target.get_page()
        self.assertTrue(self.__renderer.render.called)

    def test_is_type_of_handler(self):
        self.assertIsInstance(self.__target, Handler)


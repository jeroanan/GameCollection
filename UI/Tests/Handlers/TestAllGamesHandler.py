import unittest
from unittest.mock import Mock
from Interactors.GetGamesInteractor import GetGamesInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.AllGamesHandler import AllGamesHandler
from UI.Handlers.Handler import Handler
from UI.TemplateRenderer import TemplateRenderer


class TestAllGamesHandler(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.__interactor = Mock(GetGamesInteractor)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = AllGamesHandler(self.__interactor_factory, self.__renderer)

    def test_is_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_calls_interactor_factory(self):
        self.__target.get_page()
        self.__interactor_factory.create.assert_called_with("GetGamesInteractor")

    def test_page_executes_interactor_with_title_sort_order(self):
        self.__target.get_page()
        self.__interactor.execute.assert_called_with(sort_field="title")

    def test_get_page_calls_renderer(self):
        self.__target.get_page()
        self.assertTrue(self.__renderer.render.called)
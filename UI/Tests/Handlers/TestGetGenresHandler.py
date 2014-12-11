import unittest
from unittest.mock import Mock

from Interactors.GetGenresInteractor import GetGenresInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.GetGenresHandler import GetGenresHandler
from UI.Handlers.Handler import Handler
from UI.TemplateRenderer import TemplateRenderer


class TestGetGenresHandler(unittest.TestCase):

    def setUp(self):
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(GetGenresInteractor)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = GetGenresHandler(self.__interactor_factory, self.__renderer)

    def test_is_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_executes_interactor(self):
        self.__target.get_page()
        self.__interactor.execute.assert_called_with()

    def test_get_page_calls_renderer(self):
        self.__target.get_page()
        self.assertTrue(self.__renderer.render.called)

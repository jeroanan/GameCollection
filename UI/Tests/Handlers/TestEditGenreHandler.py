import unittest
from unittest.mock import Mock
from Interactors.GetGenreInteractor import GetGenreInteractor

from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.EditGenreHandler import EditGenreHandler
from UI.Handlers.Handler import Handler
from UI.TemplateRenderer import TemplateRenderer


class TestEditGenreHandler(unittest.TestCase):

    def setUp(self):
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(GetGenreInteractor)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = EditGenreHandler(self.__interactor_factory, self.__renderer)

    def test_is_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page(self):
        self.__target.get_page(genre_id="id")

    def test_get_page_executes_interactor(self):
        self.__target.get_page(genre_id="id")
        self.__interactor.execute.assert_called_with("id")

    def test_get_page_calls_renderer(self):
        self.__target.get_page(genre_id="id")
        self.assertTrue(self.__renderer.render.called)

import unittest
from unittest.mock import Mock
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.Handler import Handler
from UI.TemplateRenderer import TemplateRenderer


class UpdateGenreHandler(Handler):

    def get_page(self, name, description):
        interactor = self.interactor_factory.create("UpdateGenreInteractor")


class TestUpdateGenreHandler(unittest.TestCase):

    def setUp(self):
        renderer = Mock(TemplateRenderer)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__target = UpdateGenreHandler(self.__interactor_factory, renderer)

    def test_is_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page(self):
        self.__target.get_page(name="name", description="description")

    def test_get_page_calls_interactor_factory(self):
        self.__target.get_page(name="name", description="description")
        self.__interactor_factory.create.assert_called_with("UpdateGenreInteractor")
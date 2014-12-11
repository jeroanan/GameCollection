import unittest
from unittest.mock import Mock
import cherrypy
from Genre import Genre
from Interactors.AddGenreInteractor import AddGenreInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.Handler import Handler
from UI.TemplateRenderer import TemplateRenderer


class AddGenreHandler(Handler):

    def get_page(self, name, description):
        genre = Genre()
        genre.name = name
        genre.description = description
        interactor = self.interactor_factory.create("AddGenreInteractor")
        interactor.execute(genre)
        raise cherrypy.HTTPRedirect("/genres")


class TestAddGenreHandler(unittest.TestCase):

    def setUp(self):
        renderer = Mock(TemplateRenderer)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(AddGenreInteractor)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = AddGenreHandler(self.__interactor_factory, renderer)

    def test_is_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_executes_interactor(self):
        try:
            self.__target.get_page(name="name", description="description")
        except cherrypy.HTTPRedirect:
            pass
        self.assertTrue(self.__interactor.execute.called)

    def test_get_page_raises_redirect(self):
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, name="name", description="description")


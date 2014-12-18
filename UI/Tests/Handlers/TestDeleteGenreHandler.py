import unittest
from unittest.mock import Mock
import cherrypy
from Interactors.DeleteGenreInteractor import DeleteGenreInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.DeleteGenreHandler import DeleteGenreHandler
from UI.Handlers.Handler import Handler
from UI.TemplateRenderer import TemplateRenderer


class TestDeleteGenreHandler(unittest.TestCase):

    def setUp(self):
        renderer = Mock(TemplateRenderer)
        self.__interactor = Mock(DeleteGenreInteractor)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = DeleteGenreHandler(self.__interactor_factory, renderer)

    def test_is_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_executes_interactor(self):
        try:
            self.__target.get_page(genre_id="id")
        except cherrypy.HTTPRedirect:
            pass
        self.__interactor.execute.assert_called_with("id")

    def test_get_page_causes_redirect(self):
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, "id")

import unittest
from unittest.mock import Mock
import cherrypy
from Interactors.InteractorFactory import InteractorFactory
from Interactors.UpdateGenreInteractor import UpdateGenreInteractor
from UI.Handlers.Handler import Handler
from UI.Handlers.UpdateGenreHandler import UpdateGenreHandler
from UI.TemplateRenderer import TemplateRenderer


class TestUpdateGenreHandler(unittest.TestCase):

    def setUp(self):
        renderer = Mock(TemplateRenderer)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(UpdateGenreInteractor)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = UpdateGenreHandler(self.__interactor_factory, renderer)

    def test_is_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_executes_interactor(self):
        try:
            self.__target.get_page(id="id", name="name", description="description")
        except cherrypy.HTTPRedirect:
            pass
        self.assertTrue(self.__interactor.execute.called)

    def test_get_page_does_redirect(self):
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, id="id", name="name",
                          description="description")
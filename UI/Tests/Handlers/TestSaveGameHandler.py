import unittest
from unittest.mock import Mock
import cherrypy
from Interactors.AddGameInteractor import AddGameInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.Handler import Handler
from UI.Handlers.SaveGameHandler import SaveGameHandler
from UI.TemplateRenderer import TemplateRenderer


class TestSaveGameHandler(unittest.TestCase):

    def setUp(self):
        renderer = Mock(TemplateRenderer)
        interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(AddGameInteractor)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = SaveGameHandler(interactor_factory, renderer)

    def test_get_page_executes_interactor(self):
        try:
            self.__target.get_page(title=None, numcopies=None, numboxed=None, nummanuals=None, platform=None)
        except cherrypy.HTTPRedirect:
            pass
        self.assertTrue(self.__interactor.execute.called)

    def test_get_page_raises_http_redirect(self):
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, None, None, None, None, None)

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)
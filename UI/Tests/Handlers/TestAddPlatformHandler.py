import unittest
from unittest.mock import Mock
import cherrypy
from Interactors.AddPlatformInteractor import AddPlatformInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.AddPlatformHandler import AddPlatformHandler
from UI.Handlers.Handler import Handler
from UI.TemplateRenderer import TemplateRenderer


class TestAddPlatformHandler(unittest.TestCase):

    def setUp(self):
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(AddPlatformInteractor)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        renderer = Mock(TemplateRenderer)
        self.__target = AddPlatformHandler(self.__interactor_factory, renderer)

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_gat_page_calls_interactor_execute(self):
        try:
            self.__target.get_page(name=None, description=None)
        except cherrypy.HTTPRedirect:
            pass
        self.assertTrue(self.__interactor.execute.called)

    def test_get_page_raises_http_redirect(self):
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, None, None)
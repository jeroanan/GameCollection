import unittest
from unittest.mock import Mock
import cherrypy
from Interactors.InteractorFactory import InteractorFactory
from Tests.Interactors.DeleteGameInteractor import DeleteGameInteractor
from UI.Handlers.DeleteGameHandler import DeleteGameHandler
from UI.Handlers.Handler import Handler
from UI.TemplateRenderer import TemplateRenderer


class TestDeleteGameHandler(unittest.TestCase):

    def setUp(self):
        renderer = Mock(TemplateRenderer)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(DeleteGameInteractor)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = DeleteGameHandler(self.__interactor_factory, renderer)

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_calls_interactor_execute(self):
        try:
            self.__target.get_page(gameid="id")
        except cherrypy.HTTPRedirect:
            pass
        self.assertTrue(self.__interactor.execute.called)

    def test_get_page_does_redirect(self):
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, "id")
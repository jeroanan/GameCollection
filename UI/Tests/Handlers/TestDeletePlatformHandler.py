import unittest
from unittest.mock import Mock
import cherrypy
from Interactors.DeletePlatformInteractor import DeletePlatformInteractor
from Interactors.InteractorFactory import InteractorFactory
from Platform import Platform
from UI.Handlers.DeletePlatformHandler import DeletePlatformHandler
from UI.Handlers.Handler import Handler
from UI.TemplateRenderer import TemplateRenderer


class TestDeletePlatformHandler(unittest.TestCase):

    def setUp(self):
        renderer = Mock(TemplateRenderer)
        self.__interactor = Mock(DeletePlatformInteractor)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = DeletePlatformHandler(interactor_factory, renderer)

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_executes_interactor(self):
        try:
            self.__target.get_page(self.__get_params())
        except cherrypy.HTTPRedirect:
            pass
        self.__interactor.execute.assert_called_with(self.__get_platform())

    def __get_platform(self):
        p = Platform()
        p.id = "id"
        return p

    def test_get_page_redirects(self):
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, self.__get_params())

    def __get_params(self):
        return {
            "platformid": "id"
        }

    def test_get_page_with_empty_params(self):
        try:
            self.__target.get_page({"": ""})
        except cherrypy.HTTPRedirect:
            pass
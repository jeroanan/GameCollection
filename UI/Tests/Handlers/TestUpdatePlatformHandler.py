import unittest
from unittest.mock import Mock
import cherrypy
from Interactors.InteractorFactory import InteractorFactory
from Platform import Platform
from Tests.Interactors.TestUpdatePlatformInteractor import UpdatePlatformInteractor
from UI.Handlers.Handler import Handler
from UI.Handlers.UpdatePlatformHandler.UpdatePlatformHandler import UpdatePlatformHandler
from UI.Handlers.UpdatePlatformHandler.UpdatePlatformHandlerParams import UpdatePlatformHandlerParams
from UI.TemplateRenderer import TemplateRenderer


class TestUpdatePlatformHandler(unittest.TestCase):

    def setUp(self):
        interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(UpdatePlatformInteractor)
        interactor_factory.create = Mock(return_value=self.__interactor)
        renderer = Mock(TemplateRenderer)
        self.__target = UpdatePlatformHandler(interactor_factory, renderer)

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_executes_interactor(self):
        try:
            self.__target.get_page(params=self.__get_params())
        except cherrypy.HTTPRedirect:
            pass
        self.__interactor.execute.assert_called_with(platform=self.__get_platform())

    def __get_platform(self):
        p = Platform()
        self.__populate(p)
        return p

    def test_get_page_causes_redirect(self):
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, self.__get_params())

    def __get_params(self):
        p = UpdatePlatformHandlerParams()
        self.__populate(p)
        return p

    def __populate(self, platform):
        platform.id = "id"
        platform.name = "name"
        platform.description = "description"
        return platform
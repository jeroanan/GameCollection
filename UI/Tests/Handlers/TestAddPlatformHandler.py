import unittest
from unittest.mock import Mock

import cherrypy

from Interactors.Platform.AddPlatformInteractor import AddPlatformInteractor
from Interactors.InteractorFactory import InteractorFactory
from Platform import Platform
from UI.Handlers.AddPlatformHandler import AddPlatformHandler
from UI.Handlers.Handler import Handler
from UI.TemplateRenderer import TemplateRenderer


class TestAddPlatformHandler(unittest.TestCase):

    def setUp(self):
        interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(AddPlatformInteractor)
        interactor_factory.create = Mock(return_value=self.__interactor)
        renderer = Mock(TemplateRenderer)
        self.__target = AddPlatformHandler(interactor_factory, renderer)
        self.__platform_name = "name"
        self.__platform_description = "description"

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_gat_page_calls_interactor_execute(self):
        self.__get_page()
        self.__interactor.execute.assert_called_with(self.__get_platform())

    def __get_platform(self):
        platform = Platform()
        platform.name = self.__platform_name
        platform.description = self.__platform_description
        return platform

    def __get_page(self):
        params = self.__get_args()
        try:
            self.__target.get_page(platform=params)
        except cherrypy.HTTPRedirect:
            pass

    def __get_args(self):
        return {
            "name": self.__platform_name,
            "description": self.__platform_description
        }

    def test_get_page_raises_http_redirect(self):
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, self.__get_args())

    def test_get_page_with_empty_args(self):
        try:
            self.__target.get_page({"": ""})
        except cherrypy.HTTPRedirect:
            pass
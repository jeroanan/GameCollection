import unittest
from unittest.mock import Mock

import cherrypy

from Interactors import InteractorFactory
from Interactors.Interactor import Interactor
from UI.Handlers.Handler import Handler
from UI.Handlers.HandlerFactory import HandlerFactory
from UI.TemplateRenderer import TemplateRenderer
from UI.WebServer import WebServer


class TestWebServer(unittest.TestCase):

    def setUp(self):
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(Interactor)
        self.__interactor.execute = Mock()
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = WebServer(self.__interactor_factory, self.__renderer)
        self.__handler_factory = Mock(HandlerFactory)
        self.__handler = Mock(Handler)
        self.__handler_factory.create = Mock(return_value=self.__handler)
        self.__target.handler_factory = self.__handler_factory

    def test_instantiate_without_renderer_uses_default(self):
        t = WebServer(self.__interactor_factory)
        self.assertIsInstance(t.renderer, TemplateRenderer)

    def test_index_calls_handler_get_page(self):
        self.__target.index()
        self.assertTrue(self.__handler.get_page.called)

    def test_add_game_calls_handler_get_page(self):
        self.__target.addgame()
        self.assertTrue(self.__handler.get_page.called)

    def test_savegame_calls_handler_get_page(self):
        self.__target.savegame(None, None, None, None)
        self.assertTrue(self.__handler.get_page.called)

    def test_addhardware_calls_renderer(self):
        self.__target.addhardware()
        self.assertTrue(self.__renderer.render.called)

    def test_platforms_calls_renderer(self):
        self.__target.platforms()
        self.assertTrue(self.__renderer.render.called)

    def test_platforms_calls_interactor_factory(self):
        self.__target.platforms()
        self.assertTrue(self.__interactor_factory.create.called)

    def test_platforms_calls_interactor_execute(self):
        self.__target.platforms()
        self.assertTrue(self.__interactor.execute.called)

    def test_addplatform_calls_interactor_factory(self):
        try:
            self.__target.addplatform("name", "description")
        except cherrypy.HTTPRedirect:
            pass
        self.assertTrue(self.__interactor_factory.create.called)

    def test_addplatform_calls_interactor_execute(self):
        try:
            self.__target.addplatform("name", "description")
        except cherrypy.HTTPRedirect:
            pass
        self.assertTrue(self.__interactor.execute.called)

    def test_addplatform_does_redirect(self):
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.addplatform, "name", "description")

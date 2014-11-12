import unittest
from unittest.mock import Mock

import cherrypy

from Interactors import InteractorFactory
from Interactors.Interactor import Interactor
from UI.TemplateRenderer import TemplateRenderer
from UI.WebServer import WebServer


class TestWebServer(unittest.TestCase):

    def setUp(self):
        self.__factory = Mock(InteractorFactory)
        self.__interactor = Mock(Interactor)
        self.__interactor.execute = Mock()
        self.__factory.create = Mock(return_value=self.__interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = WebServer(self.__factory, self.__renderer)

    def test_instantiate_without_renderer_uses_default(self):
        t = WebServer(self.__factory)
        self.assertIsInstance(t.renderer, TemplateRenderer)

    def test_index_calls_interactor_execute(self):
        self.__target.index()
        self.assertTrue(self.__interactor.execute.called)

    def test_index_calls_renderer(self):
        self.__target.index()
        self.assertTrue(self.__renderer.render.called)

    def test_addgame_calls_renderer(self):
        self.__target.addgame()
        self.assertTrue(self.__renderer.render.called)

    def test_savegame_does_redirect(self):
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.savegame, None, None, None, None)

    def test_savegame_calls_interactor_factory(self):
        try:
            self.__target.savegame(None, None, None, None)
        except cherrypy.HTTPRedirect:
            pass
        self.assertTrue(self.__factory.create.called)

    def test_savegame_calls_interactor_execute(self):
        try:
            self.__target.savegame(None, None, None, None)
        except cherrypy.HTTPRedirect:
            pass
        self.assertTrue(self.__interactor.execute.called)

    def test_addhardware_calls_renderer(self):
        self.__target.addhardware()
        self.assertTrue(self.__renderer.render.called)

    def test_platforms_calls_renderer(self):
        self.__target.platforms()
        self.assertTrue(self.__renderer.render.called)

    def test_platforms_calls_interactor_factory(self):
        self.__target.platforms()
        self.assertTrue(self.__factory.create.called)

    def test_platforms_calls_interactor_execute(self):
        self.__target.platforms()
        self.assertTrue(self.__interactor.execute.called)

    def test_addplatform(self):
        self.__target.addplatform("name", "description")
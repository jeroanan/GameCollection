import unittest
from unittest.mock import Mock
import cherrypy

from Interactors import InteractorFactory
from UI.TemplateRenderer import TemplateRenderer
from UI.WebServer import WebServer


class TestWebServer(unittest.TestCase):
    def setUp(self):
        self.__interactor_factory = Mock(InteractorFactory)

    def test_instantiate_without_renderer_uses_default(self):
        t = WebServer(self.__interactor_factory)
        self.assertIsInstance(t.renderer, TemplateRenderer)

    def test_invalid_path_raises_404(self):
        t = WebServer(self.__interactor_factory)
        self.assertRaises(cherrypy.NotFound, t.default, ("bananas",))

"""Unit tests for the WebServer module."""
import unittest
from unittest.mock import Mock
import cherrypy

from interactors import interactor_factory
from UI.template_renderer import TemplateRenderer
from UI.web_server import WebServer


class TestWebServer(unittest.TestCase):
    """Unit tests for the WebServer module."""
    def setUp(self):
        self.__interactor_factory = Mock(interactor_factory)

    def test_instantiate_without_renderer_uses_default(self):
        """Tests that the WebServer uses the default TemplateRenderer when none is provided."""
        t = WebServer(self.__interactor_factory)
        self.assertIsInstance(t.renderer, TemplateRenderer)

    def test_invalid_path_raises_404(self):
        """Tests that an invalid path raises a 404 Not Found error."""
        t = WebServer(self.__interactor_factory)
        self.assertRaises(cherrypy.NotFound, t.default, ("bananas",))

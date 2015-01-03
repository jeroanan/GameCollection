import unittest
from unittest.mock import Mock

from Interactors import InteractorFactory
from UI.TemplateRenderer import TemplateRenderer
from UI.WebServer import WebServer


class TestWebServer(unittest.TestCase):
    def setUp(self):
        self.__interactor_factory = Mock(InteractorFactory)

    def test_instantiate_without_renderer_uses_default(self):
        t = WebServer(self.__interactor_factory)
        self.assertIsInstance(t.renderer, TemplateRenderer)
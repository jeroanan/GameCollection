import unittest
from unittest.mock import Mock
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.AddGameHandler import AddGameHandler
from UI.Handlers.Handler import Handler
from UI.TemplateRenderer import TemplateRenderer


class TestAddGameHandler(unittest.TestCase):

    def setUp(self):
        interactor_factory = Mock(InteractorFactory)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = AddGameHandler(interactor_factory, self.__renderer)

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_calls_renderer(self):
        self.__target.get_page()
        self.assertTrue(self.__renderer.render.called)
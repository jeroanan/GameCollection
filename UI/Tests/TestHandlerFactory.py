import unittest
from unittest.mock import Mock
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.Exceptions.UnrecognisedHandlerException import UnrecognisedHandlerException
from UI.Handlers.HandlerFactory import HandlerFactory
from UI.Handlers.IndexHandler import IndexHandler
from UI.TemplateRenderer import TemplateRenderer


class TestHandlerFactory(unittest.TestCase):

    def setUp(self):
        interactor_factory = Mock(InteractorFactory)
        renderer = Mock(TemplateRenderer)
        self.__target = HandlerFactory(interactor_factory, renderer)

    def test_create_with_unrecognised_type_string_throws_unrecognised_handler_exception(self):
        self.assertRaises(UnrecognisedHandlerException, self.__target.create, "UnrecognisedHandlerType")

    def test_create_index_handler_returns_index_handler(self):
        handler = self.__target.create("IndexHandler")
        self.assertIsInstance(handler, IndexHandler)

import unittest
from unittest.mock import Mock

from Data.Config import Config
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.HandlerFactory import HandlerFactory
from UI.TemplateRenderer import TemplateRenderer
from UI.WebServer import WebServer


class WebServerTestBase(unittest.TestCase):
    def setUp(self):
        self.__interactor_factory = Mock(InteractorFactory)
        self.__renderer = Mock(TemplateRenderer)
        self.__handler_factory = Mock(HandlerFactory)
        self.__config = Mock(Config)

        self.target = WebServer(interactor_factory=self.__interactor_factory, renderer=self.__renderer,
                                config=self.__config)

        self.target.handler_factory = self.__handler_factory

    def get_handler_factory(self, handler):
        handler_factory = Mock(HandlerFactory)
        handler_factory.create = Mock(return_value=handler)
        return handler_factory
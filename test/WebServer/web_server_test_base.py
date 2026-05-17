"""Base class for webserver tests."""
import unittest
from unittest.mock import Mock

from data.config import Config
from interactors.interactor_factory import InteractorFactory
from ui.Handlers.handler_factory import HandlerFactory
from ui.template_renderer import TemplateRenderer
from ui.web_server import WebServer


class WebServerTestBase(unittest.TestCase):
    """Base class for webserver tests."""
    def setUp(self):
        self.__interactor_factory = Mock(InteractorFactory)
        self.__renderer = Mock(TemplateRenderer)
        self.__handler_factory = Mock(HandlerFactory)
        self.__config = Mock(Config)

        self.target = WebServer(
            interactor_factory=self.__interactor_factory,
            renderer=self.__renderer,
            config=self.__config)

        self.target.handler_factory = self.__handler_factory

    def get_handler_factory(self, handler):
        """Returns a mocked handler factory that returns the given handler."""
        handler_factory = Mock(HandlerFactory)
        handler_factory.create = Mock(return_value=handler)
        return handler_factory

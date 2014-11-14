import unittest
from unittest.mock import Mock
from Interactors.GetPlatformsInteractor import GetPlatformsInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.AddHardwareHandler import AddHardwareHandler
from UI.Handlers.Handler import Handler
from UI.TemplateRenderer import TemplateRenderer


class TestAddHardwareHandler(unittest.TestCase):

    def setUp(self):
        self.__renderer = Mock(TemplateRenderer)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__platforms_interactor = Mock(GetPlatformsInteractor)
        self.__interactor_factory.create = Mock(return_value=self.__platforms_interactor)
        self.__target = AddHardwareHandler(self.__interactor_factory, self.__renderer)

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_calls_renderer(self):
        self.__target.get_page()
        self.assertTrue(self.__renderer.render.called)

    def test_get_page_calls_interactor_factory(self):
        self.__target.get_page()
        self.__interactor_factory.create.assert_called_with("GetPlatformsInteractor")

    def test_get_page_calls_interactor_execute(self):
        self.__target.get_page()
        self.__platforms_interactor.execute.assert_called_with()
import unittest
from unittest.mock import Mock
from Interactors.GetHardwareInteractor import GetHardwareDetailsInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.EditHardwareHandler import EditHardwareHandler
from UI.Handlers.Handler import Handler
from UI.TemplateRenderer import TemplateRenderer


class TestEditHardwareHandler(unittest.TestCase):

    def setUp(self):
        self.__interactor = Mock(GetHardwareDetailsInteractor)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = EditHardwareHandler(self.__interactor_factory, self.__renderer)

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_executes_interactor(self):
        self.__target.get_page(hardware_id="hardwareid")
        self.__interactor.execute.assert_called_with("hardwareid")

    def test_get_page_calls_renderer(self):
        self.__target.get_page(hardware_id="hardwareid")
        self.assertTrue(self.__renderer.render.called)

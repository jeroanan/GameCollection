import unittest
from unittest.mock import Mock
from Interactors.GetHardwareInteractor import GetHardwareDetailsInteractor
from Interactors.GetPlatformsInteractor import GetPlatformsInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.EditHardwareHandler import EditHardwareHandler
from UI.Handlers.Handler import Handler
from UI.TemplateRenderer import TemplateRenderer


class TestEditHardwareHandler(unittest.TestCase):

    def setUp(self):
        self.__get_hardware_details_interactor = Mock(GetHardwareDetailsInteractor)
        self.__get_platforms_interactor = Mock(GetPlatformsInteractor)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor_factory.create = Mock(side_effect=self.__interactors())
        self.__renderer = Mock(TemplateRenderer)
        self.__target = EditHardwareHandler(self.__interactor_factory, self.__renderer)

    def __interactors(self):
        return [self.__get_hardware_details_interactor, self.__get_platforms_interactor]

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_executes_get_hardware_interactor(self):
        self.__target.get_page("hardwareid")
        self.__get_hardware_details_interactor.execute.assert_called_with("hardwareid")

    def test_get_page_executes_get_platform_interactor(self):
        self.__target.get_page("hardwareid")
        self.__get_platforms_interactor.execute.assert_called_with()

    def test_get_page_calls_renderer(self):
        self.__target.get_page(hardware_id="hardwareid")
        self.assertTrue(self.__renderer.render.called)

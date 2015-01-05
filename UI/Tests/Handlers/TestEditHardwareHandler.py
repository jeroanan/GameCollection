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
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(side_effect=self.__interactors())
        self.__renderer = Mock(TemplateRenderer)
        self.__target = EditHardwareHandler(interactor_factory, self.__renderer)

    def __interactors(self):
        return [self.__get_hardware_details_interactor, self.__get_platforms_interactor]

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_executes_get_hardware_interactor(self):
        self.__get_page()
        self.__get_hardware_details_interactor.execute.assert_called_with("hardwareid")

    def test_get_page_executes_get_platform_interactor(self):
        self.__get_page()
        self.__get_platforms_interactor.execute.assert_called_with()

    def test_get_page_calls_renderer(self):
        self.__get_page()
        self.assertTrue(self.__renderer.render.called)

    def __get_page(self):
        self.__target.get_page(self.__get_args())

    def __get_args(self):
        return {
            "hardwareid": "hardwareid"
        }

    def test_get_page_empty_args(self):
        self.__target.get_page({"": ""})
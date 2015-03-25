import unittest
from unittest.mock import Mock

from Hardware import Hardware
from Interactors.Hardware.GetHardwareListInteractor import GetHardwareListInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.AllHardwareHandler import AllHardwareHandler
from UI.Handlers.Handler import Handler
from UI.TemplateRenderer import TemplateRenderer


class TestAllHardwareHandler(unittest.TestCase):

    def setUp(self):
        interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(GetHardwareListInteractor())
        self.__hardware = [Hardware()]
        self.__interactor.execute = Mock(return_value=self.__hardware)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = AllHardwareHandler(interactor_factory, self.__renderer)

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_calls_interactor(self):
        self.__target.get_page({"": ""})
        self.__interactor.execute.assert_called_with(sort_field="name", sort_direction="asc")

    def test_get_page_calls_renderer(self):
        self.__target.get_page({"": ""})
        self.__renderer.render.assert_called_with("allhardware.html",
                                                  hardware=self.__hardware, title="All Hardware",
                                                  hw_sort_field="name", hw_sort_dir="asc")

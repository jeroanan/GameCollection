import unittest
from unittest.mock import Mock

import cherrypy

from Hardware import Hardware
from Interactors.InteractorFactory import InteractorFactory
from Interactors.Hardware.SaveHardwareInteractor import SaveHardwareInteractor
from UI.Handlers.Handler import Handler
from UI.Handlers.SaveHardwareHandler import SaveHardwareHandler
from UI.TemplateRenderer import TemplateRenderer


class TestSaveHardwareHandler(unittest.TestCase):

    def setUp(self):
        renderer = Mock(TemplateRenderer)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(SaveHardwareInteractor)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = SaveHardwareHandler(self.__interactor_factory, renderer)

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_executes_save_hardware_interactor(self):
        try:
            self.__target.get_page(params=self.__get_params())
        except cherrypy.HTTPRedirect:
            pass
        self.__interactor.execute.assert_called_with(hardware=self.__get_hardware())

    def __get_hardware(self):
        h = Hardware()
        h.name = "name"
        h.platform = "platform"
        h.num_owned = 1
        h.num_boxed = 2
        h.notes = "notes"
        return h

    def test_get_page_does_redirect(self):
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, params=self.__get_params())

    def __get_params(self):
        return {
            "name": "name",
            "platform": "platform",
            "numowned": 1,
            "numboxed": 2,
            "notes": "notes"
        }
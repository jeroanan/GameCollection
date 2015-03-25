import unittest
from unittest.mock import Mock

import cherrypy

from Interactors.Hardware.DeleteHardwareInteractor import DeleteHardwareInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.DeleteHardwareHandler import DeleteHardwareHandler
from UI.Handlers.Handler import Handler
from UI.TemplateRenderer import TemplateRenderer


class TestDeleteHardwareHandler(unittest.TestCase):

    def setUp(self):
        renderer = Mock(TemplateRenderer)
        self.__interactor = Mock(DeleteHardwareInteractor)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = DeleteHardwareHandler(interactor_factory, renderer)

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_executes_interactor(self):
        try:
            self.__get_page()
        except cherrypy.HTTPRedirect:
            pass
        self.__interactor.execute.assert_called_with("hardwareid")

    def __get_page(self):
        self.__target.get_page(self.__get_args())

    def test_get_page_causes_redirect(self):
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, self.__get_args())

    def __get_args(self):
        return {
            "hardwareid": "hardwareid"
        }

    def test_get_page_empty_args(self):
        try:
            self.__target.get_page({"": ""})
        except cherrypy.HTTPRedirect:
            pass
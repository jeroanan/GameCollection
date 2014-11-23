import unittest
from unittest.mock import Mock
import cherrypy
from Interactors.DeleteHardwareInteractor import DeleteHardwareInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.DeleteHardwareHandler import DeleteHardwareHandler
from UI.Handlers.Handler import Handler
from UI.TemplateRenderer import TemplateRenderer


class TestDeleteHardwareHandler(unittest.TestCase):

    def setUp(self):
        renderer = Mock(TemplateRenderer)
        self.__interactor = Mock(DeleteHardwareInteractor)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = DeleteHardwareHandler(self.__interactor_factory, renderer)

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_calls_interactor_factory(self):
        try:
            self.__target.get_page(hardware_id="hardwareid")
        except cherrypy.HTTPRedirect:
            pass
        self.__interactor_factory.create.assert_called_with("DeleteHardwareInteractor")

    def test_get_page_executes_interactor(self):
        hardwareid = "hardwareid"
        try:
            self.__target.get_page(hardware_id=hardwareid)
        except cherrypy.HTTPRedirect:
            pass
        self.__interactor.execute.assert_called_with(hardwareid)

    def test_get_page_causes_redirect(self):
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, "hardwareid")

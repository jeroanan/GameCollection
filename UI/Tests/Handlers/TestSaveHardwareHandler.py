import unittest
from unittest.mock import Mock
import cherrypy
from Interactors.InteractorFactory import InteractorFactory
from Interactors.SaveHardwareInteractor import SaveHardwareInteractor
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
            self.__target.get_page(name="name", platform="platform", numowned="0", numboxed="0")
        except cherrypy.HTTPRedirect:
            pass
        self.assertTrue(self.__interactor.execute.called)

    def test_get_page_does_redirect(self):
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, name="name", platform="platform", numowned="0",
                          numboxed="0")

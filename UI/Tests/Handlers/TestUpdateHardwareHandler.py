import unittest
from unittest.mock import Mock
import cherrypy
from Interactors.InteractorFactory import InteractorFactory
from Interactors.UpdateHardwareInteractor import UpdateHardwareInteractor
from UI.Handlers.Handler import Handler
from UI.Handlers.UpdateHardwareHandler import UpdateHardwareHandler
from UI.TemplateRenderer import TemplateRenderer


class TestUpdateHardwareHandler(unittest.TestCase):

    def setUp(self):
        self.__interactor = Mock(UpdateHardwareInteractor)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = UpdateHardwareHandler(self.__interactor_factory, self.__renderer)

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_executes_interactor(self):
        try:
            self.__target.get_page(id="id", name="name", platform="platform", numowned=1, numboxed=0)
        except cherrypy.HTTPRedirect:
            pass
        self.assertTrue(self.__interactor.execute.called)

    def test_get_page_causes_redirect(self):
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, id="id", name="name", platform="platform",
                          numowned=1, numboxed=0)
import unittest
from unittest.mock import Mock
import cherrypy
from Hardware import Hardware
from Interactors.InteractorFactory import InteractorFactory
from Interactors.UpdateHardwareInteractor import UpdateHardwareInteractor
from UI.Handlers.Handler import Handler
from UI.Handlers.UpdateHardwareHandler.UpdateHardwareHandler import UpdateHardwareHandler
from UI.Handlers.UpdateHardwareHandler.UpdateHardwareHandlerParams import UpdateHardwareHandlerParams
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
            self.__target.get_page(params=self.__get_params())
        except cherrypy.HTTPRedirect:
            pass
        self.__interactor.execute.assert_called_with(self.__get_hardware())

    def __get_hardware(self):
        return self.__populate(Hardware())

    def test_get_page_causes_redirect(self):
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, params=self.__get_params())

    def __get_params(self):
        return self.__populate(UpdateHardwareHandlerParams())

    def __populate(self, h):
        h.id = "id"
        h.name = "name"
        h.platform = "platform"
        h.num_owned = 1
        h.num_boxed = 0
        h.notes = ""
        return h
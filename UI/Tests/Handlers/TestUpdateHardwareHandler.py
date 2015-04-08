import unittest
from unittest.mock import Mock

import cherrypy

from Hardware import Hardware
from Interactors.InteractorFactory import InteractorFactory
from Interactors.Hardware.UpdateHardwareInteractor import UpdateHardwareInteractor
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.Handler import Handler
from UI.Handlers.Session.Session import Session
from UI.Handlers.UpdateHardwareHandler import UpdateHardwareHandler
from UI.TemplateRenderer import TemplateRenderer


class TestUpdateHardwareHandler(unittest.TestCase):

    def setUp(self):
        self.__interactor = Mock(UpdateHardwareInteractor)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=self.__interactor)
        renderer = Mock(TemplateRenderer)
        self.__target = UpdateHardwareHandler(interactor_factory, renderer)
        self.__target.session = Mock(Session)

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_executes_interactor(self):
        self.__target.get_page(params=self.__get_params())
        self.__interactor.execute.assert_called_with(self.__get_hardware())
    
    def test_get_page_with_null_hardware_name_returns_empty_string(self):
        p = self.__get_params()
        del p["name"]
        result = self.__target.get_page(p)
        self.assertEqual("", result)

    def test_gert_page_with_empty_hardware_name_returns_empty_string(self):
        p = self.__get_params()
        p["name"] = ""
        result = self.__target.get_page(p)
        self.assertEqual("", result)

    def test_get_page_with_null_platform_returns_empty_string(self):
        p = self.__get_params()
        del p["platform"]
        result = self.__target.get_page(p)
        self.assertEqual("", result)

    def test_get_page_with_session_not_set_raises_session_not_set_exception(self):
        self.__target.session = None
        self.assertRaises(SessionNotSetException, self.__target.get_page, self.__get_params())

    def test_get_page_not_logged_in_redirects_to_home_page(self):
        session = Mock(Session)
        session.get_value = Mock(return_value="")
        self.__target.session = session
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, self.__get_params())

    def __get_hardware(self):
        h = Hardware()
        h.id = "id"
        h.name = "name"
        h.platform = "platform"
        h.num_owned = 1
        h.num_boxed = 0
        h.notes = ""
        return h

    def __get_params(self):
        return {
            "id": "id",
            "name": "name",
            "platform": "platform",
            "numcopies": 1,
            "numboxed": 0,
            "notes": ""
        }

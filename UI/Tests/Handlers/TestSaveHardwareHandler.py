import unittest
from unittest.mock import Mock

import cherrypy

from Hardware import Hardware
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from Interactors.Hardware.SaveHardwareInteractor import SaveHardwareInteractor
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.Session.Session import Session
from UI.Handlers.SaveHardwareHandler import SaveHardwareHandler
from UI.TemplateRenderer import TemplateRenderer


class TestSaveHardwareHandler(unittest.TestCase):

    def setUp(self):
        renderer = Mock(TemplateRenderer)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(SaveHardwareInteractor)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = SaveHardwareHandler(self.__interactor_factory, renderer)
        self.__target.session = Mock(Session)

    def test_is_instance_of_authenticated_handler(self):
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_get_page_executes_save_hardware_interactor(self):
        self.__target.get_page(params=self.__get_params())        
        self.__interactor.execute.assert_called_with(hardware=self.__get_hardware())

    def __get_hardware(self):
        h = Hardware()
        h.name = "name"
        h.platform = "platform"
        h.num_owned = 1
        h.num_boxed = 2
        h.notes = "notes"
        return h

    def test_null_name_returns_empty_string(self):
        self.__assert_missing_param_returns_empty_string("name")
        
    def test_empty_name_returns_empty_string(self):
        self.__assert_empty_param_returns_empty_string("name")

    def test_null_platform_returns_empty_string(self):
        self.__assert_missing_param_returns_empty_string("platform")

    def test_empty_platform_returns_empty_string(self):
        self.__assert_empty_param_returns_empty_string("platform")

    def test_null_number_owned_returns_empty_string(self):
        self.__assert_missing_param_returns_empty_string("numowned")

    def test_empty_number_owned_returns_empty_string(self):
        self.__assert_empty_param_returns_empty_string("numowned")

    def __assert_missing_param_returns_empty_string(self, param_name):
        p = self.__get_params()
        del p[param_name]
        result = self.__target.get_page(p)
        self.assertEqual("", result)

    def __assert_empty_param_returns_empty_string(self, param_name):
        p = self.__get_params()
        p[param_name] = ""
        result = self.__target.get_page(p)
        self.assertEqual("", result)

    def test_session_not_set_raises_session_not_set_exception(self):
        self.__target.session = None
        self.assertRaises(SessionNotSetException, self.__target.get_page, self.__get_params())

    def test_not_logged_in_redirects_to_home_page(self):
        session = Mock(Session)
        session.get_value = Mock(return_value="")
        self.__target.session = session
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, self.__get_params())

    def __get_params(self):
        return {
            "name": "name",
            "platform": "platform",
            "numowned": 1,
            "numboxed": 2,
            "notes": "notes"
        }

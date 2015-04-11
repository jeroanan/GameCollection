import unittest
from unittest.mock import Mock

import cherrypy

from Interactors.Hardware.DeleteHardwareInteractor import DeleteHardwareInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.DeleteHardwareHandler import DeleteHardwareHandler
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.Session.Session import Session
from UI.TemplateRenderer import TemplateRenderer


class TestDeleteHardwareHandler(unittest.TestCase):

    def setUp(self):
        renderer = Mock(TemplateRenderer)
        self.__interactor = Mock(DeleteHardwareInteractor)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = DeleteHardwareHandler(interactor_factory, renderer)
        self.__target.session = Mock(Session)

    def test_is_instance_of_authenticated_handler(self):
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_null_hardwareid_returns_empty_string(self):
        a = self.__get_args()
        del a["hardwareid"]
        result = self.__target.get_page(a)
        self.assertEqual("", result)

    def test_empty_hardwareid_returns_empty_string(self):
        a = self.__get_args()
        a["hardwareid"] = ""
        result = self.__target.get_page(a)
        self.assertEqual("", result)

    def test_interactor_raises_exception_returns_empty_string(self):
        def boom(hardware_id):
            raise Exception("ouch!")
        
        interactor = Mock(DeleteHardwareInteractor)
        interactor.execute = Mock(side_effect=boom)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=interactor)
        self.__target = DeleteHardwareHandler(interactor_factory, None)
        self.__target.session = Mock(Session)

        result = self.__target.get_page(self.__get_args())
        self.assertEqual("", result)

    def test_session_not_set_raises_session_not_set_exception(self):
        self.__target.session = None
        self.assertRaises(SessionNotSetException, self.__target.get_page, self.__get_args())
            
    def test_not_logged_in_redirects_to_home_page(self):
        session = Mock(Session)
        session.get_value = Mock(return_value="")
        self.__target.session = session
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, self.__get_args())

    def __get_args(self):
        return {
            "hardwareid": "hardwareid"
        }


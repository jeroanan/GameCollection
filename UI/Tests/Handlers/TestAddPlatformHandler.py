import unittest
from unittest.mock import Mock

import cherrypy

from Interactors.Platform.AddPlatformInteractor import AddPlatformInteractor
from Interactors.InteractorFactory import InteractorFactory
from Platform import Platform
from UI.Handlers.AddPlatformHandler import AddPlatformHandler
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.Session.Session import Session
from UI.TemplateRenderer import TemplateRenderer


class TestAddPlatformHandler(unittest.TestCase):

    def setUp(self):
        interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(AddPlatformInteractor)
        interactor_factory.create = Mock(return_value=self.__interactor)
        renderer = Mock(TemplateRenderer)
        self.__target = AddPlatformHandler(interactor_factory, renderer)
        self.__target.session = Mock(Session) 
        self.__platform_name = "name"
        self.__platform_description = "description"

    def test_is_instance_of_authenticated_handler(self):
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_calls_interactor_execute(self):
        self.__get_page()
        self.__interactor.execute.assert_called_with(self.__get_platform())

    def __get_platform(self):
        platform = Platform()
        platform.name = self.__platform_name
        platform.description = self.__platform_description
        return platform

    def __get_page(self):
        params = self.__get_args()
        self.__target.get_page(params)

    def test_platform_null_name_returns_empty_string(self):
        p = self.__get_args()
        del p["name"]
        result = self.__target.get_page(p)
        self.assertEqual("", result)

    def test_platform_empty_name_returns_empty_string(self):
        p = self.__get_args()
        p["name"] = ""
        result = self.__target.get_page(p)
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
            "name": self.__platform_name,
            "description": self.__platform_description
        }


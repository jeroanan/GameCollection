import unittest
from unittest.mock import Mock

import cherrypy

from Interactors.InteractorFactory import InteractorFactory
from Platform import Platform
from Tests.Interactors.Platform.TestUpdatePlatformInteractor import UpdatePlatformInteractor #TODO: Move
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException 
from UI.Handlers.Handler import Handler
from UI.Handlers.Session.Session import Session
from UI.Handlers.UpdatePlatformHandler import UpdatePlatformHandler
from UI.TemplateRenderer import TemplateRenderer


class TestUpdatePlatformHandler(unittest.TestCase):

    def setUp(self):
        interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(UpdatePlatformInteractor)
        interactor_factory.create = Mock(return_value=self.__interactor)
        renderer = Mock(TemplateRenderer)
        self.__target = UpdatePlatformHandler(interactor_factory, renderer)
        self.__target.session = Mock(Session)

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_executes_interactor(self):
        self.__get_page()
        self.__interactor.execute.assert_called_with(platform=self.__get_platform())

    def __get_platform(self):
        p = Platform()
        p.id = "id"
        p.name = "name"
        p.description = "description"
        return p
    
    def test_null_platform_returns_empty_string(self):
        result = self.__target.get_page(None)
        self.assertEqual("", result)        

    def test_null_id_returns_empty_string(self):
        self.__assert_missing_param_returns_empty_string("id")

    def test_empty_id_returns_empty_string(self):
        self.__assert_empty_param_returns_empty_string("id")

    def test_null_name_returns_empty_string(self):
        self.__assert_missing_param_returns_empty_string("name")

    def test_empty_name_returns_empty_string(self):
        self.__assert_empty_param_returns_empty_string("name")

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

    def test_interactor_throws_exception_returns_empty_string(self):
        def boom(platform):
            raise Exception("Boom!")

        self.__interactor.execute = Mock(side_effect=boom)
        self.__target.interactor = self.__interactor
        result = self.__get_page()
        self.assertEqual("", result)

    def test_session_not_set_raises_session_not_set_exception(self):
        self.__target.session = None
        self.assertRaises(SessionNotSetException, self.__get_page)
    
    def test_not_logged_in_redirects_to_home_page(self):
        session = Mock(Session)
        session.get_value = Mock(return_value="")
        self.__target.session = session
        self.assertRaises(cherrypy.HTTPRedirect, self.__get_page)

    def __get_page(self):
        return self.__target.get_page(self.__get_params())

    def __get_params(self):
        return {
            "id": "id",
            "name": "name",
            "description": "description"
        }



import unittest
from unittest.mock import Mock

import cherrypy

from Interactors.Platform.DeletePlatformInteractor import DeletePlatformInteractor
from Interactors.InteractorFactory import InteractorFactory
from Platform import Platform
from UI.Handlers.DeletePlatformHandler import DeletePlatformHandler
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.Session.Session import Session
from UI.TemplateRenderer import TemplateRenderer


class TestDeletePlatformHandler(unittest.TestCase):

    def setUp(self):
        renderer = Mock(TemplateRenderer)
        self.__interactor = Mock(DeletePlatformInteractor)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = DeletePlatformHandler(interactor_factory, renderer)
        self.__target.session = Mock(Session)

    def test_is_instance_of_authenticated_handler(self):
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_executes_interactor(self):
        self.__get_page()
        self.__interactor.execute.assert_called_with("id")

    def test_null_id_returns_empty_string(self):
        p = self.__get_params()
        del p["platformid"]
        result = self.__target.get_page(p)
        self.assertEqual("", result)

    def test_empty_id_returns_empty_string(self):
        p = self.__get_params()
        p["platformid"] = ""
        result = self.__target.get_page(p)
        self.assertEqual("", result)

    def test_interactor_throws_exception_returns_empty_string(self):
        def boom(platform):
            raise Exception("boom")

        interactor = Mock(DeletePlatformInteractor)
        interactor.execute = Mock(side_effect=boom)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=interactor)
        target = DeletePlatformHandler(interactor_factory, None)
        target.session = Mock(Session)
        target.get_page(self.__get_params())

    def test_session_not_set_raises_session_not_set_exception(self):
        self.__target.session = None
        self.assertRaises(SessionNotSetException, self.__get_page)

    def test_not_logged_in_redirects_to_home_page(self):
        session = Mock(Session)
        session.get_value = Mock(return_value="")
        self.__target.session = session
        self.assertRaises(cherrypy.HTTPRedirect, self.__get_page)
        

    def __get_page(self):
        self.__target.get_page(self.__get_params())

    def __get_params(self):
        return {
            "platformid": "id"
        }


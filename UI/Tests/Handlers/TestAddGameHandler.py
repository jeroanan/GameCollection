import cherrypy
import unittest
from unittest.mock import Mock

from Interactors.Platform.GetPlatformsInteractor import GetPlatformsInteractor
from Interactors.InteractorFactory import InteractorFactory
from Platform import Platform
from UI.Handlers.AddGameHandler import AddGameHandler
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.Handler import Handler
from UI.Handlers.Session.Session import Session
from UI.TemplateRenderer import TemplateRenderer


class TestAddGameHandler(unittest.TestCase):

    def setUp(self):
        self.__platforms = [Platform()]
        interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(GetPlatformsInteractor)
        self.__interactor.execute = Mock(return_value=self.__platforms)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = AddGameHandler(interactor_factory, self.__renderer)
        session = Mock(Session)
        self.__target.session = session

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_calls_renderer(self):
        self.__target.get_page({})
        self.__renderer.render.assert_called_with("addgame.html", title="Add Game", platforms=self.__platforms)

    def test_get_page_session_is_none_raises_session_not_set_exception(self):
        self.__target.session = None
        self.assertRaises(SessionNotSetException, self.__target.get_page, {})

    def test_get_page_not_logged_in_redirects_to_login_page(self):
        self.__target.session = None
        session = Mock(Session)
        session.get_value = Mock(return_value="")
        self.__target.session = session
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, {})

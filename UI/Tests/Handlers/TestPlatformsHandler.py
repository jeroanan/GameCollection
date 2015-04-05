import cherrypy
import unittest
from unittest.mock import Mock

from Interactors.Platform.GetPlatformsInteractor import GetPlatformsInteractor
from Interactors.Platform.GetSuggestedPlatformsInteractor import GetSuggestedPlatformsInteractor
from Interactors.InteractorFactory import InteractorFactory
from Platform import Platform
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.Handler import Handler
from UI.Handlers.PlatformsHandler import PlatformsHandler
from UI.Handlers.Session.Session import Session
from UI.TemplateRenderer import TemplateRenderer


class TestPlatformsHandler(unittest.TestCase):

    def setUp(self):        
        self.__platforms = [Platform()]
        self.__suggested_platforms = [Platform(), Platform()]
        self.__get_platforms_interactor = Mock(GetPlatformsInteractor)
        self.__get_platforms_interactor.execute = Mock(return_value=self.__platforms)
        self.__get_suggested_platforms_interactor = Mock(GetSuggestedPlatformsInteractor)
        self.__get_suggested_platforms_interactor.execute = Mock(return_value=self.__suggested_platforms)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(side_effect=self.__interactor_factory_create())
        self.__renderer = Mock(TemplateRenderer)
        self.__target = PlatformsHandler(interactor_factory, self.__renderer)
        session = Mock(Session)
        self.__target.session = session

    def __interactor_factory_create(self):
        return [self.__get_platforms_interactor, self.__get_suggested_platforms_interactor]

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_calls_renderer(self):
        self.__get_page()
        self.__renderer.render.assert_called_with("platforms.html", title="Manage Platforms", 
                                                  platforms=self.__platforms, 
                                                  suggested_platforms=self.__suggested_platforms)
        
    def test_get_page_session_not_set_raises_session_not_set_exception(self):
        self.__target.session = None
        self.assertRaises(SessionNotSetException, self.__get_page)
        
    def test_get_page_not_logged_in_redirects_to_login_page(self):
        self.__target.session = None
        session = Mock(Session)
        session.get_value = Mock(return_value="")
        self.__target.session = session
        self.assertRaises(cherrypy.HTTPRedirect, self.__get_page)

    def __get_page(self):
        self.__target.get_page({})

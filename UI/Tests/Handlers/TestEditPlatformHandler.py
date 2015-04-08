import cherrypy
import unittest
from unittest.mock import Mock

from Interactors.Platform.GetPlatformInteractor import GetPlatformInteractor
from Interactors.InteractorFactory import InteractorFactory
from Platform import Platform
from UI.Handlers.EditPlatformHandler import EditPlatformHandler
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.Handler import Handler
from UI.Handlers.Session.Session import Session
from UI.TemplateRenderer import TemplateRenderer


class TestEditPlatformHandler(unittest.TestCase):

    def setUp(self):
        self.__platform = Platform()
        interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(GetPlatformInteractor)
        self.__interactor.execute = Mock(return_value=self.__platform)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__renderer.render = Mock(return_value="some html")
        self.__target = EditPlatformHandler(interactor_factory, self.__renderer)
        session = Mock(Session)
        self.__target.session = session

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_calls_renderer(self):
        self.__target.get_page(self.__get_args())
        self.__renderer.render.assert_called_with("editplatform.html", platform=self.__platform, title="Edit Platform")

    def test_with_null_platformid_returns_empty_string(self):
        p = self.__get_args()
        del p["platformid"]
        result = self.__target.get_page(p)
        self.assertEqual("", result)

    def test_with_empty_platformid_returns_empty_string(self):
        p = self.__get_args()
        p["platformid"] = ""
        result = self.__target.get_page(p)
        self.assertEqual("", result)

    def test_interactor_raises_exception_returns_empty_string(self):
        def ker_boom(platform_id):
            raise Exception("Betcha didn't see that coming!")
        
        interactor = Mock(GetPlatformInteractor)
        interactor.execute = Mock(side_effect=ker_boom)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=interactor)
        renderer = Mock(TemplateRenderer)
        renderer.render = Mock(return_value="Some html")
        target = EditPlatformHandler(interactor_factory, renderer)
        target.session = Mock(Session)

        target.interactor = interactor
        result = target.get_page(self.__get_args())
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
            "platformid": "platformid"
        }


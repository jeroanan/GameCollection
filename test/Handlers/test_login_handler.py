"""Provides unit tests for the LoginHandler class"""
import unittest
from unittest.mock import Mock
import cherrypy
from UI.Handlers.Handler import Handler
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.LoginHandler import LoginHandler
from UI.Handlers.Session.Session import Session
from UI.TemplateRenderer import TemplateRenderer


class TestLoginHandler(unittest.TestCase):
    """Unit tests for the LoginHandler class"""

    def setUp(self):
        self.__renderer = Mock(TemplateRenderer)
        session = Mock(Session)
        session.get_value = Mock(return_value="")
        self.__target = LoginHandler(None, self.__renderer)
        self.__target.session = session

    def test_is_handler(self):
        """Test that LoginHandler is derived from Handler"""
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_renders_login_screen(self):
        """Test that calling LoginHandler.get_page causes the login page to be rendered"""
        self.__target.get_page(self.__get_args())
        self.__renderer.render.assert_called_with("login.html")

    def test_get_page_no_session_raises_session_not_set_exception(self):
        """Test that calling LoginHandler.get_page with no session set raises 
        SessionNotSetException"""
        target = LoginHandler(None, self.__renderer)
        self.assertRaises(SessionNotSetException, target.get_page, self.__get_args())

    def test_get_page_user_logged_in_redirects_to_home_page(self):
        """Test that calling LoginHandler.get_page when a user is already logged in causes a
        redirect to the home page"""
        def get_value(key):
            if key == "user_id":
                return "user"
            return None

        target = LoginHandler(None, self.__renderer)
        session = Mock(Session)
        session.get_value = Mock(side_effect=get_value)
        target.session = session
        self.assertRaises(cherrypy.HTTPRedirect, target.get_page, self.__get_args)

    def __get_args(self):
        return {}

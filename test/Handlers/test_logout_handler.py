"""Provides unit tests for LogoutHandler"""
import unittest
from unittest.mock import Mock
import cherrypy

from ui.Cookies.Cookies import Cookies
from ui.handlers.authenticated_handler import AuthenticatedHandler
from ui.handlers.logout_handler import LogoutHandler
from ui.handlers.Exceptions.CookiesNotSetException import CookiesNotSetException
from ui.handlers.Exceptions.SessionNotSetException import SessionNotSetException
from ui.handlers.Session.Session import Session

class TestLogoutHandler(unittest.TestCase):
    """Unit tests for the LogoutHandler class"""

    def setUp(self):
        self.__cookies = Mock(Cookies)
        self.__session = Mock(Session)
        self.__target = LogoutHandler(None, None)
        self.__target.session = self.__session
        self.__target.cookies = self.__cookies

    def test_is_handler(self):
        """Test that LogoutHandler is derived from AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_get_page_with_session_not_set_raises_session_not_set_exception(self):
        """Test that calling LogoutHandler.get_page with no session set raises
        SessionNotSetException"""
        self.__target.session = None
        self.assertRaises(SessionNotSetException, self.__target.get_page, {})

    def test_get_page_with_cookies_not_set_raises_session_not_set_exception(self):
        """Test that calling LogoutHandler.get_page with no cookies set raises
        CookiesNotSetException"""
        self.__target.cookies = None
        self.assertRaises(CookiesNotSetException, self.__target.get_page, {})

    def test_get_page_clears_session_status_cookie(self):
        """Test that calling LogoutHandler.get_page clears the session_status cookie"""
        self.__get_page()
        self.__cookies.clear_cookie.assert_any_call("session_status")

    def test_get_page_clears_user_id_cookie(self):
        """Test that calling LogoutHandler.get_page clears the user_id cookie"""
        self.__get_page()
        self.__cookies.clear_cookie.assert_any_call("user_id")

    def test_get_page_expires_session(self):
        """Test that calling LogoutHandler.get_page expires the session"""
        self.__get_page()
        self.assertTrue(self.__session.expire.called)

    def test_get_page_redirects_to_home(self):
        """Test that calling LogoutHandler.get_page causes a redirect to the home page"""
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, {})

    def __get_page(self):
        try:
            self.__target.get_page({})
        except cherrypy.HTTPRedirect:
            pass

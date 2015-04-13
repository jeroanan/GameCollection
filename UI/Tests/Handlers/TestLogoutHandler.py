import cherrypy
import unittest
from unittest.mock import Mock

from UI.Cookies.Cookies import Cookies
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.LogoutHandler import LogoutHandler
from UI.Handlers.Exceptions.CookiesNotSetException import CookiesNotSetException
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.Session.Session import Session

class TestLogoutHandler(unittest.TestCase):

    def setUp(self):
        self.__cookies = Mock(Cookies)
        self.__session = Mock(Session)
        self.__target = LogoutHandler(None, None)        
        self.__target.session = self.__session
        self.__target.cookies = self.__cookies

    def test_is_handler(self):
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_get_page_with_session_not_set_raises_session_not_set_exception(self):
        self.__target.session = None
        self.assertRaises(SessionNotSetException, self.__target.get_page, {})

    def test_get_page_with_cookies_not_set_raises_session_not_set_exception(self):
        self.__target.cookies = None
        self.assertRaises(CookiesNotSetException, self.__target.get_page, {})
        
    def test_get_page_clears_session_status_cookie(self):
        self.__get_page()
        self.__cookies.clear_cookie.assert_any("session_status")

    def test_get_page_clears_user_id_cookie(self):
        self.__get_page()
        self.__cookies.clear_cookie.assert_any("user_id")
        
    def test_get_page_expires_session(self):
        self.__get_page()
        self.assertTrue(self.__session.expire.called)

    def test_get_page_redirects_to_home(self):
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, {})

    def __get_page(self):
        try:
            self.__target.get_page({})
        except cherrypy.HTTPRedirect:
            pass

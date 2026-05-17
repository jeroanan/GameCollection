"""Provides unit tests for the SearchHandler class"""
import unittest
from unittest.mock import Mock
import cherrypy

from interactors.interactor_factory import InteractorFactory
from interactors.search.search_interactor import SearchInteractor
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.SearchHandler import SearchHandler
from UI.Handlers.Session.Session import Session
from UI.template_renderer import TemplateRenderer


class TestSearchHandler(unittest.TestCase):
    """Unit tests for the SearchHandler class"""
    def setUp(self):
        interactor = Mock(SearchInteractor())
        interactor.execute = Mock(return_value=[])
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = SearchHandler(interactor_factory, self.__renderer)
        self.__target.session = Mock(Session)

    def test_is_authenticated_handler(self):
        """Test that SearchHandler is an instance of AuthenticatedHandler"""
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_calls_render_method(self):
        """Test that calling SearchHandler.get_page causes TemplateRenderer.render to be called
        correctly"""
        self.__get_page()
        self.__renderer.render.assert_called_with(
            template="search.html",
            title="Search Results",
            games=[],
            search_term="search",
            query="searchterm=search",
            game_sort_field="title",
            game_sort_direction="asc")

    def test_no_session_raises_session_not_set_error(self):
        """Test that calling SearchHandler.get_page with no session set raises
        SessionNotSetException"""
        self.__target.session = None
        self.assertRaises(SessionNotSetException, self.__get_page)

    def test_not_logged_in_redirects_to_home_page(self):
        """Test that calling SearchHandler.get_page when no user is logged in causes a redirect
        to the home page"""
        self.__target.session = None
        session = Mock(Session)
        session.get_value = Mock(return_value="")
        self.__target.session = session
        self.assertRaises(cherrypy.HTTPRedirect, self.__get_page)

    def __get_page(self):
        self.__target.get_page(params=self.__get_params())

    def __get_params(self):
        return {
            "searchterm": "search",
            "gamesort": "title",
            "gamesortdir": "asc"
        }

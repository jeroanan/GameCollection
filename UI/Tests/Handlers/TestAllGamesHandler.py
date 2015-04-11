import cherrypy
import unittest
from unittest.mock import Mock

from Game import Game
from Interactors.Game import GetGamesInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.AllGamesHandler import AllGamesHandler
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.Session.Session import Session
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.TemplateRenderer import TemplateRenderer


class TestAllGamesHandler(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.__games = [Game()]
        self.__get_games_interactor = Mock(GetGamesInteractor)
        self.__get_games_interactor.execute = Mock(return_value=self.__games)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(side_effect=self.__get_interactors())
        self.__renderer = Mock(TemplateRenderer)
        self.__target = AllGamesHandler(interactor_factory, self.__renderer)
        self.__target.session = Mock(Session)

    def __get_interactors(self):
        return [self.__get_games_interactor]

    def test_is_authenticated_handler(self):
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_get_page_calls_renderer(self):
        self.__get_page()
        self.__renderer.render.assert_called_with("allgames.html", games=self.__games, title="All Games", 
                                                  game_sort_field="title", game_sort_dir="asc", platform="platform", 
                                                  query="platform=platform")
        self.assertTrue(self.__renderer.render.called)

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
            "gamesort": "title",
            "gamesortdir": "asc",
            "platform": "platform"
        }

import cherrypy
import unittest
from unittest.mock import Mock

from Game import Game
from Interactors.Game import GetGamesInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.Session.Session import Session
from UI.Handlers.SortGamesHandler import SortGamesHandler
from UI.TemplateRenderer import TemplateRenderer


class TestSortGamesHandler(unittest.TestCase):

    def setUp(self):
        self.__interactor = Mock(GetGamesInteractor)
        self.__games = [Game()]
        self.__interactor.execute = Mock(return_value=self.__games)
        interactor_factory = Mock(InteractorFactory)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__renderer = Mock(TemplateRenderer)
        self.__target = SortGamesHandler(interactor_factory, self.__renderer)
        self.__target.session = Mock(Session)

    def test_is_authenticated_handler(self):
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_get_page_calls_renderer(self):
        args = self.__get_args()
        self.__target.get_page(args)
        self.__renderer.render.assert_called_with("games.html", games=self.__games,
                                                  game_sort_field=args["field"], game_sort_dir=args["sortdir"])

    def test_session_not_set_raises_session_not_set_exception(self):
        self.__target.session = None
        self.assertRaises(SessionNotSetException, self.__target.get_page, self.__get_args())

    def test_not_logged_in_redirects_to_home_page(self):
        session = Mock(Session)
        session.get_value = Mock(return_value="")
        self.__target.session = session
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, self.__get_args())

    def __get_args(self):
        return {"field": "title", "sortdir": "asc", "numrows": 2}

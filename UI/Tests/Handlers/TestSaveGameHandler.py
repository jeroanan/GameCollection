import cherrypy
import unittest
from unittest.mock import Mock

from Game import Game
from Interactors.Game.AddGameInteractor import AddGameInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.SaveGameHandler import SaveGameHandler
from UI.Handlers.Session.Session import Session
from UI.TemplateRenderer import TemplateRenderer


class TestSaveGameHandler(unittest.TestCase):

    def setUp(self):
        renderer = Mock(TemplateRenderer)
        interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(AddGameInteractor)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = SaveGameHandler(interactor_factory, renderer)
        session = Mock(Session)
        session.get_value = Mock(return_value="1234")
        self.__target.session = session
        self.__title = "title"
        self.__num_copies = 1
        self.__num_boxed = 2
        self.__num_manuals = 3
        self.__platform = "platform"
        self.__notes = "notes"

    def test_get_page_executes_interactor(self):
        self.__get_page()
        self.__interactor.execute.assert_called_with(game=self.__get_game(), user_id="1234")

    def __get_game(self):
        game = Game()
        game.title = self.__title
        game.num_copies = self.__num_copies
        game.num_boxed = self.__num_boxed
        game.num_manuals = self.__num_manuals
        game.platform = self.__platform
        game.notes = self.__notes
        return game

    def test_is_instance_of_authenticated_handler(self):
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_null_title_returns_empty_string(self):
        p = self.__get_args()
        del p["title"]
        result = self.__target.get_page(p)
        self.assertEqual("", result)

    def test_empty_title_returns_empty_string(self):
        p = self.__get_args()
        p["title"] = ""
        result = self.__target.get_page(p)
        self.assertEqual("", result)
        
    def test_null_platform_returns_empty_string(self):
        self.__assert_missing_param_returns_empty_string("platform")

    def __assert_missing_param_returns_empty_string(self, param_name):
        p = self.__get_args()
        del p[param_name]
        result = self.__target.get_page(p)
        self.assertEqual("", result)        

    def test_session_not_set_raises_session_not_set_exception(self):
        self.__target.session = None
        self.assertRaises(SessionNotSetException, self.__get_page)

    def test_not_logged_in_redirects_to_home_page(self):
        session = Mock(Session)
        session.get_value = Mock(return_value="")
        self.__target.session = session
        self.assertRaises(cherrypy.HTTPRedirect, self.__get_page)

    def __get_page(self):
        self.__target.get_page(params=self.__get_args())

    def __get_args(self):
        return {
            "title": self.__title,
            "numcopies": self.__num_copies,
            "numboxed": self.__num_boxed,
            "nummanuals": self.__num_manuals,
            "platform": self.__platform,
            "notes": self.__notes
        }

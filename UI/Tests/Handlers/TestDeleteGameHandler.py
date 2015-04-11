import cherrypy
import unittest
from unittest.mock import Mock

from Game import Game
from Interactors.Game.DeleteGameInteractor import DeleteGameInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.DeleteGameHandler import DeleteGameHandler
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.Handlers.Session.Session import Session
from UI.TemplateRenderer import TemplateRenderer


class TestDeleteGameHandler(unittest.TestCase):

    def setUp(self):
        renderer = Mock(TemplateRenderer)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(DeleteGameInteractor)
        self.__interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = DeleteGameHandler(self.__interactor_factory, renderer)
        self.__target.session = Mock(Session)

    def test_is_instance_of_authenticated_handler(self):
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_calls_interactor_execute(self):
        def get_game():
            g = Game()
            g.id = "id"
            return g

        self.__target.get_page(self.__get_args())
        self.__interactor.execute.assert_called_with(get_game())

    def test_no_id_returns_empty_string(self):
        p = self.__get_args()
        del p["gameid"]
        result = self.__target.get_page(p)
        self.assertEqual("", result)

    def test_empty_id_returns_empty_string(self):
        p = self.__get_args(id="")
        result = self.__target.get_page(p)
        self.assertEqual("", result)        

    def test_session_not_set_raises_session_not_set_exception(self):
        self.__target.session = None
        self.assertRaises(SessionNotSetException, self.__target.get_page, self.__get_args())

    def test_not_logged_in_redirects_to_home_page(self):
        self.__target.session = None
        session = Mock(Session)
        session.get_value = Mock(return_value="")
        self.__target.session = session
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, self.__get_args())
        
    def __get_args(self, id="id"):
        return {
            "gameid": id
        }


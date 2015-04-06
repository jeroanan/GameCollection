import cherrypy
import unittest
from unittest.mock import Mock

from AbstractPersistence import AbstractPersistence
from Game import Game
from Interactors.Exceptions.PersistenceException import PersistenceException
from Interactors.InteractorFactory import InteractorFactory
from Interactors.Game.UpdateGameInteractor import UpdateGameInteractor
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.Handler import Handler
from UI.Handlers.Session.Session import Session
from UI.Handlers.UpdateGameHandler import UpdateGameHandler
from UI.TemplateRenderer import TemplateRenderer


class TestUpdateGameHandler(unittest.TestCase):
    def setUp(self):
        renderer = Mock(TemplateRenderer)
        interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(UpdateGameInteractor)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = UpdateGameHandler(interactor_factory, renderer)
        self.__target.session = Mock(Session)

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_calls_interactor_execute(self):
        self.__target.get_page(params=self.__get_params())
        self.__interactor.execute.assert_called_with(game=self.__get_game())
        
    def __get_game(self):
        g = Game()
        g.id = "id"
        g.title = "title"
        g.num_copies = 1
        g.num_boxed = 2
        g.num_manuals = 3
        g.platform = "platform"
        g.notes = "notes"
        return g

    def test_no_session_raises_session_not_set_error(self):
        self.__target.session = None        
        self.assertRaises(SessionNotSetException, self.__target.get_page, self.__get_params())

    def test_no_title_gives_empty_string(self):
        self.__assert_missing_param_gives_empty_string("title")

    def test_empty_title_gives_empty_string(self):
        result = self.__target.get_page(self.__get_params(title=""))
        self.assertEqual("", result)

    def test_no_platform_gives_empty_string(self):
        self.__assert_missing_param_gives_empty_string("platform")

    def test_empty_platform_gives_empty_string(self):
        result = self.__target.get_page(self.__get_params(platform=""))
        self.assertEqual("", result)

    def test_persistence_exception_gives_empty_string(self):        

        def init_target():
            def update_game(game):
                raise PersistenceException

            p = Mock(AbstractPersistence)
            interactor = Mock(UpdateGameInteractor)
            interactor.execute = Mock(side_effect=update_game)
            interactor_factory = Mock(InteractorFactory)
            interactor_factory.create = Mock(return_value=interactor)
            target = UpdateGameHandler(interactor_factory, Mock(TemplateRenderer))
            target.session = Mock(Session)
            return target
        
        result = init_target().get_page(self.__get_params())
        self.assertEqual("", result)

    def __assert_missing_param_gives_empty_string(self, param_name):
        p = self.__get_params()
        del p[param_name]
        result = self.__target.get_page(p)
        self.assertEqual("", result)

    def test_not_logged_in_redirects_to_home_page(self):
        self.__target.session = None
        session = Mock(Session)
        session.get_value = Mock(return_value="")
        self.__target.session = session
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, self.__get_params())

    def __get_params(self, title="title", platform="platform"):
        return {
            "id": "id",
            "title": title,
            "numcopies": 1,
            "numboxed": 2,
            "nummanuals": 3,
            "platform": platform,
            "notes": "notes"
        }


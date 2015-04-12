import cherrypy
import unittest
from unittest.mock import Mock

from Game import Game
from Interactors.Game.GetGameInteractor import GetGameInteractor
from Interactors.Platform.GetPlatformsInteractor import GetPlatformsInteractor
from Interactors.InteractorFactory import InteractorFactory
from Platform import Platform
from UI.Handlers.Exceptions.SessionNotSetException import SessionNotSetException
from UI.Handlers.Session.Session import Session
from UI.Handlers.EditGameHandler import EditGameHandler
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler
from UI.TemplateRenderer import TemplateRenderer


class TestEditGameHandler(unittest.TestCase):

    def setUp(self):        
        
        def init_get_game_interactor():
            i = Mock(GetGameInteractor)
            i.execute = Mock(return_value=self.__game)
            return i

        def init_get_platforms_interactor():
            i = Mock(GetPlatformsInteractor)
            i.execute = Mock(return_value=self.__platforms)
            return i

        def init_interactor_factory():
            def get_interactor():
                return [get_game_interactor, get_platforms_interactor]

            factory = Mock(InteractorFactory)
            factory.create = Mock(side_effect=get_interactor())
            return factory

        self.__game = self.__get_game()
        self.__platforms = [Platform]
        self.__renderer = Mock(TemplateRenderer)
        get_game_interactor = init_get_game_interactor()
        get_platforms_interactor = init_get_platforms_interactor()
        interactor_factory = init_interactor_factory()
        self.__target = EditGameHandler(interactor_factory, self.__renderer)
        self.__target.session = Mock(Session)
        self.__target.session.get_value = Mock(return_value="1234")

    def __get_game(self):
        g = Game()
        g.title = "Game"
        g.platform = "Platform"
        return g        

    def test_is_instance_of_authenticated_handler(self):
        self.assertIsInstance(self.__target, AuthenticatedHandler)

    def test_calls_renderer(self):

        def make_page_title():
            g = self.__get_game()
            return "{title} ({platform})".format(title=g.title, platform=g.platform)        

        self.__get_page()

        self.__renderer.render.assert_called_with("editgame.html", game=self.__game, title=make_page_title(), 
                                                  platforms=self.__platforms, game_found=True)    

    def test_no_session_raises_session_not_set_error(self):
        self.__target.session = None
        self.assertRaises(SessionNotSetException, self.__get_page)
        
    def test_not_logged_in_redirects_to_home_page(self):
        self.__target.session = None
        session = Mock(Session)
        session.get_value = Mock(return_value="")
        self.__target.session = session
        self.assertRaises(cherrypy.HTTPRedirect, self.__get_page)

    def __get_page(self):
        self.__target.get_page({"gameid": "game_id"})

    def test_with_empty_args(self):
        self.__target.get_page({"": ""})


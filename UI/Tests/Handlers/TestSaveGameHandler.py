import unittest
from unittest.mock import Mock
import cherrypy
from Game import Game
from Interactors.AddGameInteractor import AddGameInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.Handler import Handler
from UI.Handlers.SaveGameHandler.SaveGameHandler import SaveGameHandler
from UI.Handlers.SaveGameHandler.SaveGameHandlerParams import SaveGameHandlerParams
from UI.TemplateRenderer import TemplateRenderer


class TestSaveGameHandler(unittest.TestCase):

    def setUp(self):
        renderer = Mock(TemplateRenderer)
        interactor_factory = Mock(InteractorFactory)
        self.__interactor = Mock(AddGameInteractor)
        interactor_factory.create = Mock(return_value=self.__interactor)
        self.__target = SaveGameHandler(interactor_factory, renderer)
        self.__title = "title"
        self.__num_copies = 1
        self.__num_boxed = 2
        self.__num_manuals = 3
        self.__platform = "platform"
        self.__notes = "notes"

    def test_get_page_executes_interactor(self):
        self.__get_page()
        self.__interactor.execute.assert_called_with(game=self.__get_game())

    def __get_page(self):
        try:
            self.__target.get_page(params=self.__get_params())
        except cherrypy.HTTPRedirect:
            pass

    def test_get_page_raises_http_redirect(self):
        self.assertRaises(cherrypy.HTTPRedirect, self.__target.get_page, params=self.__get_params())

    def __get_params(self):
        params = SaveGameHandlerParams()
        params.title = self.__title
        params.num_copies = self.__num_copies
        params.num_boxed = self.__num_boxed
        params.num_manuals = self.__num_manuals
        params.platform = self.__platform
        params.notes = self.__notes
        return params

    def __get_game(self):
        game = Game()
        game.title = self.__title
        game.num_copies = self.__num_copies
        game.num_boxed = self.__num_boxed
        game.num_manuals = self.__num_manuals
        game.platform = self.__platform
        game.notes = self.__notes
        return game

    def test_is_instance_of_handler(self):
        self.assertIsInstance(self.__target, Handler)
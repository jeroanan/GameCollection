import unittest
from unittest.mock import Mock

from Game import Game
from Interactors.Game.AddGameInteractor import AddGameInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.Handler import Handler
from UI.Handlers.SaveGameHandler.SaveGameHandler import SaveGameHandler
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

    def test_get_page_with_empty_params(self):
        self.__target.get_page({"": ""})
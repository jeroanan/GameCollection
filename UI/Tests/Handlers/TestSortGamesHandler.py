import unittest
from unittest.mock import Mock

from Game import Game
from Interactors.Game import GetGamesInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.Handler import Handler
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

    def test_is_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_get_page_executes_interactor(self):
        args = self.__get_args()
        self.__target.get_page(args)
        self.__interactor.execute.assert_called_with(args["field"], args["sortdir"], args["numrows"])

    def test_get_page_calls_renderer(self):
        args = self.__get_args()
        self.__target.get_page(args)
        self.__renderer.render.assert_called_with("games.html", games=self.__games,
                                                  game_sort_field=args["field"], game_sort_dir=args["sortdir"])

    def __get_args(self):
        return {"field": "title", "sortdir": "asc", "numrows": 2}
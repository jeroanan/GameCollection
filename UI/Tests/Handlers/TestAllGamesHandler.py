import unittest
from unittest.mock import Mock
from Interactors.CountGamesInteractor import CountGamesInteractor
from Interactors.GetGamesInteractor import GetGamesInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.AllGamesHandler import AllGamesHandler
from UI.Handlers.Handler import Handler
from UI.TemplateRenderer import TemplateRenderer


class TestAllGamesHandler(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.__get_games_interactor = Mock(GetGamesInteractor)
        self.__count_games_interactor = Mock(CountGamesInteractor)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor_factory.create = Mock(side_effect=self.__get_interactors())
        self.__renderer = Mock(TemplateRenderer)
        self.__target = AllGamesHandler(self.__interactor_factory, self.__renderer)

    def __get_interactors(self):
        return [self.__get_games_interactor, self.__count_games_interactor]

    def test_is_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_page_executes_get_games_interactor(self):
        self.__get_page()
        self.__get_games_interactor.execute.assert_called_with(sort_field="title", sort_direction="asc", platform=None)

    def test_get_page_executes_count_games_interactor(self):
        self.__get_page()
        self.__count_games_interactor.execute.assert_called_with()

    def test_get_page_calls_renderer(self):
        self.__get_page()
        self.assertTrue(self.__renderer.render.called)

    def __get_page(self, sort_field="title", sort_direction="asc", platform=None):
        self.__target.get_page(sort_field=sort_field, sort_direction=sort_direction, platform=platform)
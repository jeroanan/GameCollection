import unittest
from unittest.mock import Mock
from Interactors.GetGamesInteractor import GetGamesInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.AllGamesHandler.AllGamesHandler import AllGamesHandler
from UI.Handlers.AllGamesHandler.AllGamesHandlerParams import AllGamesHandlerParams
from UI.Handlers.Handler import Handler
from UI.TemplateRenderer import TemplateRenderer


class TestAllGamesHandler(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.__get_games_interactor = Mock(GetGamesInteractor)
        self.__get_games_interactor.execute = Mock(return_value=[])
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor_factory.create = Mock(side_effect=self.__get_interactors())
        self.__renderer = Mock(TemplateRenderer)
        self.__target = AllGamesHandler(self.__interactor_factory, self.__renderer)

    def __get_interactors(self):
        return [self.__get_games_interactor]

    def test_is_handler(self):
        self.assertIsInstance(self.__target, Handler)

    def test_page_executes_get_games_interactor(self):
        self.__get_page()
        self.__get_games_interactor.execute.assert_called_with(sort_field="title", sort_direction="asc",
                                                               platform="platform")

    def test_get_page_calls_renderer(self):
        self.__get_page()
        self.assertTrue(self.__renderer.render.called)

    def __get_page(self):
        self.__target.get_page(params=self.__get_params())

    def __get_params(self, sort_field="title", sort_direction="asc", platform="platform"):
        p = AllGamesHandlerParams()
        p.sort_field = sort_field
        p.sort_direction = sort_direction
        p.platform = platform
        return p
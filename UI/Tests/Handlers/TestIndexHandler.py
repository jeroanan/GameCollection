import unittest
from unittest.mock import Mock
from Data.Config import Config

from Interactors.GetHardwareListInteractor import GetHardwareListInteractor
from Interactors.GetGamesInteractor import GetGamesInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.Handler import Handler
from UI.Handlers.IndexHandler import IndexHandler
from UI.TemplateRenderer import TemplateRenderer


class TestIndexHandler(unittest.TestCase):

    def setUp(self):
        self.__get_games_interactor = Mock(GetGamesInteractor)
        self.__get_hardware_list_interactor = Mock(GetHardwareListInteractor)
        self.__renderer = Mock(TemplateRenderer)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor_factory.create = Mock(side_effect=self.__get_interactors())
        self.__config = Mock(Config)
        self.__config.get = Mock(return_value=0)
        self.__target = IndexHandler(self.__interactor_factory, self.__renderer, self.__config)

    def __get_interactors(self):
        return [self.__get_games_interactor, self.__get_hardware_list_interactor]

    def test_get_page_with_none_game_sort_executes_interactor_with_correct_parameters(self):
        self.__get_page()
        self.__get_games_interactor.execute.assert_called_with(sort_field="title", number_of_games=0,
                                                               sort_direction="asc")

    def test_get_page_executes_get_hardware_list_interactor(self):
        self.__get_page()
        self.assertTrue(self.__get_hardware_list_interactor.execute.called)

    def test_get_page_gets_number_of_games_config_setting(self):
        self.__get_page()
        self.__config.get.assert_called_with("front-page-games")

    def test_get_page_calls_renderer(self):
        self.__get_page()
        self.assertTrue(self.__renderer.render.called)

    def test_get_page_uses_default_sort_options(self):
        self.__get_page(game_sort=None, game_sort_direction=None)
        self.__get_games_interactor.execute.assert_called_with(sort_field="title", number_of_games=0,
                                                               sort_direction="asc")

    def __get_page(self, game_sort="title", game_sort_direction="asc"):
        self.__target.get_page(game_sort=game_sort, game_sort_direction=game_sort_direction)

    def test_is_type_of_handler(self):
        self.assertIsInstance(self.__target, Handler)


import unittest
from unittest.mock import Mock

from Data.Config import Config
from Interactors.CountGamesInteractor import CountGamesInteractor
from Interactors.GetHardwareListInteractor import GetHardwareListInteractor
from Interactors.GetGamesInteractor import GetGamesInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.Handler import Handler
from UI.Handlers.IndexHandler.IndexHandler import IndexHandler
from UI.TemplateRenderer import TemplateRenderer


class TestIndexHandler(unittest.TestCase):

    def setUp(self):
        self.__get_games_interactor = Mock(GetGamesInteractor)
        self.__count_games_interactor = Mock(CountGamesInteractor)
        self.__get_hardware_list_interactor = Mock(GetHardwareListInteractor)
        self.__renderer = Mock(TemplateRenderer)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor_factory.create = Mock(side_effect=self.__get_interactors())
        self.__config = Mock(Config)
        self.__config.get = Mock(return_value=0)
        self.__target = IndexHandler(self.__interactor_factory, self.__renderer, self.__config)

    def __get_interactors(self):
        return [self.__get_games_interactor, self.__get_hardware_list_interactor, self.__count_games_interactor]

    def test_get_page_executes_get_games_interactor_with_correct_parameters(self):
        self.__get_page()
        self.__get_games_interactor.execute.assert_called_with(sort_field="title", number_of_games=0,
                                                               sort_direction="asc")

    def test_get_page_executes_get_hardware_list_interactor_with_correct_parameters(self):
        self.__get_page()
        self.__get_hardware_list_interactor.execute.assert_called_with(sort_field="name", sort_direction="asc")

    def test_get_page_gets_number_of_games_config_setting(self):
        self.__get_page()
        self.__config.get.assert_called_with("front-page-games")

    def test_get_page_calls_renderer(self):
        self.__get_page()
        self.assertTrue(self.__renderer.render.called)

    def test_get_page_uses_default_sort_options_for_games(self):
        self.__get_page(game_sort=None, game_sort_direction=None)
        self.__get_games_interactor.execute.assert_called_with(sort_field="title", number_of_games=0,
                                                               sort_direction="asc")

    def test_get_page_uses_default_sort_options_for_hardware(self):
        self.__get_page(hardware_sort=None, hardware_sort_direction=None)
        self.__get_hardware_list_interactor.execute.assert_called_with(sort_field="name", sort_direction="asc")

    def test_get_page_gets_count_games_interactor_from_interactor_factory(self):
        self.__get_page()
        self.__interactor_factory.create.assert_called_with("CountGamesInteractor")

    def test_get_page_executes_count_games_interactor(self):
        self.__get_page()
        self.__count_games_interactor.execute.assert_called_with()

    def test_get_page_with_no_params(self):
        self.__target.get_page({"": ""})

    def __get_page(self, game_sort="title", game_sort_direction="asc", hardware_sort="name",
                   hardware_sort_direction="asc"):
        args = {
            "gamesort":  game_sort,
            "gamesortdir": game_sort_direction,
            "hardwaresort": hardware_sort,
            "hardwaresortdir": hardware_sort_direction
        }

        self.__target.get_page(args)

    def test_is_type_of_handler(self):
        self.assertIsInstance(self.__target, Handler)


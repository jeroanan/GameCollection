import unittest
from unittest.mock import Mock

from Data.Config import Config
from Game import Game
from Hardware import Hardware
from Interactors.Game.CountGamesInteractor import CountGamesInteractor
from Interactors.Hardware.GetHardwareListInteractor import GetHardwareListInteractor
from Interactors.Game.GetGamesInteractor import GetGamesInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.Handler import Handler
from UI.Handlers.IndexHandler import IndexHandler
from UI.TemplateRenderer import TemplateRenderer


class TestIndexHandler(unittest.TestCase):

    def setUp(self):
        self.__games = [Game()]
        self.__hardware = [Hardware()]
        self.__get_games_interactor = Mock(GetGamesInteractor)
        self.__get_games_interactor.execute = Mock(return_value=self.__games)
        self.__count_games_interactor = Mock(CountGamesInteractor)
        self.__count_games_interactor.execute = Mock(return_value=0)
        self.__get_hardware_list_interactor = Mock(GetHardwareListInteractor)
        self.__get_hardware_list_interactor.execute = Mock(return_value=self.__hardware)
        self.__renderer = Mock(TemplateRenderer)
        self.__interactor_factory = Mock(InteractorFactory)
        self.__interactor_factory.create = Mock(side_effect=self.__get_interactors())
        self.__config = Mock(Config)
        self.__config.get = Mock(return_value=0)
        self.__target = IndexHandler(self.__interactor_factory, self.__renderer, self.__config)

    def __get_interactors(self):
        return [self.__get_games_interactor, self.__get_hardware_list_interactor, self.__count_games_interactor]

    def test_get_page_gets_number_of_games_config_setting(self):
        self.__get_page(self.__get_args())
        self.__config.get.assert_called_with("front-page-games")

    def test_get_page_calls_renderer(self):
        params = {"gamesort": "title"}
        args = self.__get_args()
        self.__get_page(args)
        self.__renderer.render.assert_called_with("index.html", games=self.__games, hardware=self.__hardware,
                                                  title="Games Collection", game_sort_field=args["gamesort"], 
                                                  game_sort_dir=args["gamesortdir"], hw_sort_field=args["hardwaresort"], 
                                                  number_of_games=0, hw_sort_dir=args["hardwaresortdir"])

    def test_get_page_uses_default_sort_options_for_games(self):
        self.__get_page(self.__get_args(game_sort=None, game_sort_direction=None))
        self.__get_games_interactor.execute.assert_called_with(sort_field="title", number_of_games=0,
                                                               sort_direction="asc")

    def test_get_page_uses_default_sort_options_for_hardware(self):
        self.__get_page(self.__get_args(hardware_sort=None, hardware_sort_direction=None))
        self.__get_hardware_list_interactor.execute.assert_called_with(sort_field="name", sort_direction="asc")

    def __get_page(self, args):
        self.__target.get_page(args)

    def __get_args(self, game_sort="title", game_sort_direction="asc", hardware_sort="name",
                   hardware_sort_direction="asc"):
        return {
            "gamesort":  game_sort,
            "gamesortdir": game_sort_direction,
            "hardwaresort": hardware_sort,
            "hardwaresortdir": hardware_sort_direction
        }

    def test_is_type_of_handler(self):
        self.assertIsInstance(self.__target, Handler)

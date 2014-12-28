from UI.Handlers.Handler import Handler


class IndexHandler(Handler):

    def __init__(self, interactor_factory, renderer, config):
        super().__init__(interactor_factory, renderer)
        self.__config = config
        self.__game_sort = None
        self.__game_sort_dir = None
        self.__hardware_sort = None
        self.__hardware_sort_dir = None

    def get_page(self, game_sort, game_sort_direction, hardware_sort, hardware_sort_direction):
        self.__hardware_sort = hardware_sort
        self.__hardware_sort_dir = hardware_sort_direction
        self.__init_sorting(game_sort, game_sort_direction, hardware_sort, hardware_sort_direction)
        games = self.__get_games()
        hardware = self.__get_hardware()
        number_of_games = self.__count_games()
        return self.renderer.render("index.html", games=games, hardware=hardware, title="Games Collection",
                                    game_sort_field=self.__game_sort, game_sort_direction=self.__game_sort_dir,
                                    hardware_sort_field=self.__hardware_sort, number_of_games=number_of_games,
                                    hardware_sort_direction=self.__hardware_sort_dir)

    def __init_sorting(self, game_sort, game_sort_direction, hardware_sort, hardware_sort_direction):
        self.__init_game_sorting(game_sort, game_sort_direction)
        self.__init_hardware_sorting(hardware_sort, hardware_sort_direction)

    def __init_game_sorting(self, game_sort, game_sort_direction):
        self.__game_sort = self.set_if_null(game_sort, "title")
        self.__game_sort_dir = self.set_if_null(game_sort_direction, "asc")

    def __init_hardware_sorting(self, hardware_sort, hardware_sort_direction):
        self.__hardware_sort = self.set_if_null(hardware_sort, "name")
        self. __hardware_sort_dir = self.set_if_null(hardware_sort_direction, "asc")

    def __get_games(self):
        get_games_interactor = self.interactor_factory.create("GetGamesInteractor")
        number_of_games = self.__config.get("front-page-games")
        games = get_games_interactor.execute(number_of_games=number_of_games, sort_field=self.__game_sort,
                                             sort_direction=self.__game_sort_dir)
        return games

    def __get_hardware(self):
        get_hardware_list_interactor = self.interactor_factory.create("GetHardwareListInteractor")
        hardware = get_hardware_list_interactor.execute(sort_field=self.__hardware_sort,
                                                        sort_direction=self.__hardware_sort_dir)
        return hardware

    def __count_games(self):
        count_games_interactor = self.interactor_factory.create("CountGamesInteractor")
        number_of_games = count_games_interactor.execute()
        return number_of_games

from UI.Handlers.Handler import Handler


class IndexHandler(Handler):

    def __init__(self, interactor_factory, renderer, config):
        super().__init__(interactor_factory, renderer)
        self.__config = config
        self.__game_sort = None
        self.__game_sort_dir = None
        self.__hardware_sort = None
        self.__hardware_sort_dir = None

    def get_page(self, args):
        self.__init_sorting(args)

        return self.renderer.render("index.html", games=(self.__get_games()), hardware=(self.__get_hardware()),
                                    title="Games Collection", game_sort_field=self.__game_sort,
                                    game_sort_direction=self.__game_sort_dir, hardware_sort_field=self.__hardware_sort,
                                    number_of_games=(self.__count_games()),
                                    hardware_sort_direction=self.__hardware_sort_dir)

    def __init_sorting(self, args):
        self.__init_game_sorting(args)
        self.__init_hardware_sorting(args)

    def __init_game_sorting(self, args):
        default_sort_field = "title"
        default_sort_direction = "asc"
        self.__game_sort = self.set_if_null(args.get("gamesort", default_sort_field), default_sort_field)
        self.__game_sort_dir = self.set_if_null(args.get("gamesortdir", default_sort_direction),
                                                default_sort_direction)

    def __init_hardware_sorting(self, args):
        default_sort_field = "name"
        default_sort_direction = "asc"
        self.__hardware_sort = self.set_if_null(args.get("hardwaresort", default_sort_field), default_sort_field)
        self. __hardware_sort_dir = self.set_if_null(args.get("hardwaresortdir", default_sort_direction),
                                                     default_sort_direction)

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
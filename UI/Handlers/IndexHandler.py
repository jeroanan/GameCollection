from UI.Handlers.Handler import Handler


class IndexHandler(Handler):

    def __init__(self, interactor_factory, renderer, config):
        super().__init__(interactor_factory, renderer)
        self.__config = config

    def get_page(self, game_sort, game_sort_direction):
        game_sort, game_sort_direction = self.init_sorting(game_sort, game_sort_direction)
        games = self.__get_games(game_sort, game_sort_direction)
        hardware = self.__get_hardware()
        return self.renderer.render("index.html", games=games, hardware=hardware, title="Games Collection",
                                    game_sort_field=game_sort, game_sort_direction=game_sort_direction)

    def init_sorting(self, game_sort, game_sort_direction):
        game_sort = self.__set_if_null(game_sort, "title")
        game_sort_direction = self.__set_if_null(game_sort_direction, "asc")
        return game_sort, game_sort_direction

    def __set_if_null(self, variable, value):
        if variable is None:
            return value
        return variable

    def __get_games(self, game_sort, game_sort_direction):
        get_games_interactor = self.interactor_factory.create("GetGamesInteractor")
        number_of_games = self.__config.get("front-page-games")
        games = get_games_interactor.execute(number_of_games=number_of_games, sort_field=game_sort,
                                             sort_direction=game_sort_direction)
        return games

    def __get_hardware(self):
        get_hardware_list_interactor = self.interactor_factory.create("GetHardwareListInteractor")
        hardware = get_hardware_list_interactor.execute()
        return hardware

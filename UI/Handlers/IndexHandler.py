from UI.Handlers.Handler import Handler


class IndexHandler(Handler):

    def __init__(self, interactor_factory, renderer, config):
        super().__init__(interactor_factory, renderer)
        self.__config = config

    def get_page(self, game_sort=None):
        games = self.__get_games(game_sort)
        hardware = self.__get_hardware()
        return self.renderer.render("index.html", games=games, hardware=hardware, title="Games Collection")

    def __get_games(self, game_sort):
        get_games_interactor = self.interactor_factory.create("GetGamesInteractor")
        number_of_games = self.__config.get("front-page-games")
        if game_sort is None:
            game_sort = "title"
        games = get_games_interactor.execute(number_of_games=number_of_games, sort_field=game_sort)
        return games

    def __get_hardware(self):
        get_hardware_list_interactor = self.interactor_factory.create("GetHardwareListInteractor")
        hardware = get_hardware_list_interactor.execute()
        return hardware

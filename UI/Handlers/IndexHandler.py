from UI.Handlers.Handler import Handler


class IndexHandler(Handler):

    def __init__(self, interactor_factory, renderer, config):
        super().__init__(interactor_factory, renderer)
        self.__config = config

    def get_page(self):
        get_games_interactor = self.interactor_factory.create("GetGamesInteractor")
        get_hardware_list_interactor = self.interactor_factory.create("GetHardwareListInteractor")
        games = get_games_interactor.execute(number_of_games=self.__config.get("front-page-games"))
        hardware = get_hardware_list_interactor.execute()
        return self.renderer.render("index.html", games=games, hardware=hardware, title="Games Collection")

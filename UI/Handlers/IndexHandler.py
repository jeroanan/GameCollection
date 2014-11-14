from UI.Handlers.Handler import Handler


class IndexHandler(Handler):

    def get_page(self):
        get_games_interactor = self.interactor_factory.create("GetGamesInteractor")
        get_hardware_list_interactor = self.interactor_factory.create("GetHardwareListInteractor")
        games = get_games_interactor.execute()
        hardware = get_hardware_list_interactor.execute()
        return self.renderer.render("index.html", games=games, hardware=hardware, title="Games Collection")

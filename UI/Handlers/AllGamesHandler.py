from UI.Handlers.Handler import Handler


class AllGamesHandler(Handler):

    def get_page(self):
        interactor = self.interactor_factory.create("GetGamesInteractor")
        games = interactor.execute(sort_field="title")
        return self.renderer.render("allgames.html", games=games, title="All Games")

from UI.Handlers.Handler import Handler


class IndexHandler(Handler):

    def get_page(self):
        interactor = self.interactor_factory.create("GetGamesInteractor")
        games = interactor.execute()
        return self.renderer.render("index.html", games=games, title="Games Collection")

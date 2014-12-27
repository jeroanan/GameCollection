from UI.Handlers.Handler import Handler


class EditGameHandler(Handler):

    def get_page(self, game_id):
        get_game_interactor = self.interactor_factory.create("GetGameInteractor")
        game = get_game_interactor.execute(game_id)
        platform_interactor = self.interactor_factory.create("GetPlatformsInteractor")
        platforms = platform_interactor.execute()
        pageTitle = "{title} ({platform})".format(title=game.title, platform=game.platform)
        return self.renderer.render("editgame.html", game=game, title=pageTitle, platforms=platforms)
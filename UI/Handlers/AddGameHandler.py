from UI.Handlers.Handler import Handler


class AddGameHandler(Handler):

    def get_page(self, args):
        self.check_session()
        self.redirect_if_not_logged_in()
        platform_interactor = self.interactor_factory.create("GetPlatformsInteractor")
        platforms = platform_interactor.execute()
        return self.renderer.render("addgame.html", title="Add Game", platforms=platforms)

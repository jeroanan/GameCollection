from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class AddGameHandler(AuthenticatedHandler):

    def get_page(self, args):
        super().get_page(args)
        platform_interactor = self.interactor_factory.create("GetPlatformsInteractor")
        platforms = platform_interactor.execute()
        return self.renderer.render("addgame.html", title="Add Game", platforms=platforms)

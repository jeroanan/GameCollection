from UI.Handlers.Handler import Handler


class PlatformsHandler(Handler):

    def get_page(self):
        interactor = self.interactor_factory.create("GetPlatformsInteractor")
        platforms = interactor.execute()
        return self.renderer.render("platforms.html", title="Manage Platforms", platforms=platforms)

from UI.Handlers.Handler import Handler


class PlatformsHandler(Handler):

    def get_page(self):
        get_platforms = self.interactor_factory.create("GetPlatformsInteractor")
        get_suggested_platforms = self.interactor_factory.create("GetSuggestedPlatformsInteractor")
        platforms = get_platforms.execute()
        suggested_platforms = get_suggested_platforms.execute()
        return self.renderer.render("platforms.html", title="Manage Platforms", platforms=platforms,
                                    suggested_platforms=suggested_platforms)


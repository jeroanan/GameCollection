from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class AddHardwareHandler(AuthenticatedHandler):

    def get_page(self, args):
        super().get_page(args)
        platforms_interactor = self.interactor_factory.create("GetPlatformsInteractor")
        platforms = platforms_interactor.execute()
        return self.renderer.render("addhardware.html", title="Add Hardware", platforms=platforms)

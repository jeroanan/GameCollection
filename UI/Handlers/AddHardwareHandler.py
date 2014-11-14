from UI.Handlers.Handler import Handler


class AddHardwareHandler(Handler):

    def get_page(self):
        platforms_interactor = self.interactor_factory.create("GetPlatformsInteractor")
        platforms = platforms_interactor.execute()
        return self.renderer.render("addhardware.html", title="Add Hardware", platforms=platforms)
from UI.Handlers.Handler import Handler


class EditPlatformHandler(Handler):
    def get_page(self, platform_id):
        interactor = self.interactor_factory.create("GetPlatformInteractor")
        platform = interactor.execute(platform_id)
        return self.renderer.render("editplatform.html", platform=platform, title="Edit Platform")

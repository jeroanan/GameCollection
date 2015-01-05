from UI.Handlers.Handler import Handler


class EditPlatformHandler(Handler):
    def get_page(self, args):
        interactor = self.interactor_factory.create("GetPlatformInteractor")
        platform = interactor.execute(args.get("platformid", ""))
        return self.renderer.render("editplatform.html", platform=platform, title="Edit Platform")

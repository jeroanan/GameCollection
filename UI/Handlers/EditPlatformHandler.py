from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class EditPlatformHandler(AuthenticatedHandler):

    def get_page(self, args):
        super().get_page(args)
        if not self.validate_params(args, ["platformid"]):
            return ""
        interactor = self.interactor_factory.create("GetPlatformInteractor")
        try:
            platform = interactor.execute(args.get("platformid", ""))
        except:
            return ""
        return self.renderer.render("editplatform.html", platform=platform, title="Edit Platform")


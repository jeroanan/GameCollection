"""Handler for editing a platform."""
from ui.Handlers.authenticated_handler import AuthenticatedHandler


class EditPlatformHandler(AuthenticatedHandler):
    """Handler for editing a platform."""

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

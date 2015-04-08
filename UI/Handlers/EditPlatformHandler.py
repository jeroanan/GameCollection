from UI.Handlers.Handler import Handler


class EditPlatformHandler(Handler):
    def get_page(self, args):
        self.check_session()
        self.redirect_if_not_logged_in()
        if not self.__validate_args(args):
            return ""
        interactor = self.interactor_factory.create("GetPlatformInteractor")
        try:
            platform = interactor.execute(args.get("platformid", ""))
        except:
            return ""
        return self.renderer.render("editplatform.html", platform=platform, title="Edit Platform")

    def __validate_args(self, args):
        return "platformid" in args and args["platformid"] != ""


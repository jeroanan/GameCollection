from UI.Handlers.Handler import Handler


class DeleteHardwareHandler(Handler):

    def get_page(self, args):
        self.check_session()
        self.redirect_if_not_logged_in()

        if not self.__validate_args(args):
            return ""

        interactor = self.interactor_factory.create("DeleteHardwareInteractor")
        try:            
            interactor.execute(args.get("hardwareid", ""))
        except:
            return ""

    def __validate_args(self, args):
        return "hardwareid" in args and args["hardwareid"] != ""

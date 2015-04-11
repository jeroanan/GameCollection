from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class DeleteHardwareHandler(AuthenticatedHandler):

    def get_page(self, args):
        super().get_page(args)
        
        if not self.validate_params(args, ["hardwareid"]):
            return ""

        interactor = self.interactor_factory.create("DeleteHardwareInteractor")
        try:            
            interactor.execute(args.get("hardwareid", ""))
        except:
            return ""

from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class DeleteHardwareHandler(AuthenticatedHandler):

    """Handles Delete Hardware requests.
    This is really intended to be used as an ajax request rather than a webpage, so
    it doesn't give much in the way of user feedback. If the user is not currently logged
    in then it will redirect to the homepage.
    param args: A dictionary containing the key "hardwareid". hardwareid contains the uuid 
    of the item of hardware to be deleted.
    returns: If hardwareid is blank or there is an error then an empty string. Else None.
    """
    def get_page(self, args):
        super().get_page(args)
        
        if not self.validate_params(args, ["hardwareid"]):
            return ""

        interactor = self.interactor_factory.create("DeleteHardwareInteractor")
        try:            
            interactor.execute(args.get("hardwareid", ""), self.session.get_value("user_id"))
        except:
            return ""

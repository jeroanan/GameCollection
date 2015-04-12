import cherrypy
from Hardware import Hardware
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class UpdateHardwareHandler(AuthenticatedHandler):

    """Handles Hardware Update requests (i.e. new values to save to a hardware record).
    This is really intended to be used as an ajax request rather than a webpage, so
    it doesn't give much in the way of user feedback. If the user is not currently logged
    in then it will redirect to the homepage.
    param params: A dictionary comprised of the following keys:
                  + id -- The uuid of the item of hardware to save.
                  + name -- The name of the item of hardware. Mandatory.
                  + platform -- The plaform of the item of hardware. Mandatory.
                  + numcopies -- The number of copies owned of the item of hardware.
                  + numboxed -- The number of boxed copies owned of the item of hardware.
                  + notes -- Miscellaneous notes added by the user.
    returns: If one of the mandatory args keys is omitted then an empty string. Else None.
    """
    def get_page(self, params):
        super().get_page(params)
        if not self.validate_params(params, ["name", "platform"]):
            return ""
        interactor = self.interactor_factory.create("UpdateHardwareInteractor")
        interactor.execute(self.__get_hardware(params), self.session.get_value("user_id"))

    def __get_hardware(self, params):
        hardware = Hardware()
        hardware.id = params.get("id", "")
        hardware.name = params.get("name", "")
        hardware.platform = params.get("platform", "")
        hardware.num_owned = params.get("numcopies", 0)
        hardware.num_boxed = params.get("numboxed", 0)
        hardware.notes = params.get("notes")
        return hardware

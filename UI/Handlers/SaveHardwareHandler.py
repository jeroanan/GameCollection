import cherrypy
from Hardware import Hardware
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class SaveHardwareHandler(AuthenticatedHandler):

    def get_page(self, params):
        super().get_page(params)
        if not self.validate_params(params, ["name", "platform", "numowned"]):
            return ""
        interactor = self.interactor_factory.create("SaveHardwareInteractor")
        hardware = self.__get_hardware(params)
        interactor.execute(hardware=hardware)

    def __get_hardware(self, params):
        hardware = Hardware()
        hardware.name = params.get("name", "")
        hardware.platform = params.get("platform", "")
        hardware.num_owned = params.get("numowned", "")
        hardware.num_boxed = params.get("numboxed", "")
        hardware.notes = params.get("notes", "")
        return hardware

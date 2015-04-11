import cherrypy
from Hardware import Hardware
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class UpdateHardwareHandler(AuthenticatedHandler):

    def get_page(self, params):
        super().get_page(params)
        if not self.validate_params(params, ["name", "platform"]):
            return ""
        interactor = self.interactor_factory.create("UpdateHardwareInteractor")
        interactor.execute(self.__get_hardware(params))

    def __get_hardware(self, params):
        hardware = Hardware()
        hardware.id = params.get("id", "")
        hardware.name = params.get("name", "")
        hardware.platform = params.get("platform", "")
        hardware.num_owned = params.get("numcopies", 0)
        hardware.num_boxed = params.get("numboxed", 0)
        hardware.notes = params.get("notes")
        return hardware

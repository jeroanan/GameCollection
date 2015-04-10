import cherrypy
from Hardware import Hardware
from UI.Handlers.Handler import Handler


class SaveHardwareHandler(Handler):

    def get_page(self, params):
        self.check_session()
        self.redirect_if_not_logged_in()
        if not self.__validate_params(params):
            return ""
        interactor = self.interactor_factory.create("SaveHardwareInteractor")
        hardware = self.__get_hardware(params)
        interactor.execute(hardware=hardware)

    def __validate_params(self, params):
        fields = ["name", "platform", "numowned"]
        invalid_fields = sum(map(lambda x: x not in params or params[x] == "", fields))
        return invalid_fields == 0

    def __get_hardware(self, params):
        hardware = Hardware()
        hardware.name = params.get("name", "")
        hardware.platform = params.get("platform", "")
        hardware.num_owned = params.get("numowned", "")
        hardware.num_boxed = params.get("numboxed", "")
        hardware.notes = params.get("notes", "")
        return hardware

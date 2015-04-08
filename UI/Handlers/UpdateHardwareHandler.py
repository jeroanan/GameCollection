import cherrypy
from Hardware import Hardware
from UI.Handlers.Handler import Handler


class UpdateHardwareHandler(Handler):

    def get_page(self, params):
        self.check_session()
        self.redirect_if_not_logged_in()
        if not self.__validate_args(params):
            return ""
        interactor = self.interactor_factory.create("UpdateHardwareInteractor")
        interactor.execute(self.__get_hardware(params))

    def __validate_args(self, args):
        arg_names = ["name", "platform"]
        valid_args = sum(map(lambda x: args.get(x, "") != "", arg_names))
        return len(arg_names)==valid_args

    def __get_hardware(self, params):
        hardware = Hardware()
        hardware.id = params.get("id", "")
        hardware.name = params.get("name", "")
        hardware.platform = params.get("platform", "")
        hardware.num_owned = params.get("numcopies", 0)
        hardware.num_boxed = params.get("numboxed", 0)
        hardware.notes = params.get("notes")
        return hardware

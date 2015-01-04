import cherrypy
from Hardware import Hardware
from UI.Handlers.Handler import Handler


class SaveHardwareHandler(Handler):

    def get_page(self, params):
        interactor = self.interactor_factory.create("SaveHardwareInteractor")
        hardware = self.__get_hardware(params)
        interactor.execute(hardware=hardware)
        raise cherrypy.HTTPRedirect("/")

    def __get_hardware(self, params):
        hardware = Hardware()
        hardware.name = params["name"]
        hardware.platform = params["platform"]
        hardware.num_owned = params["numowned"]
        hardware.num_boxed = params["numboxed"]
        hardware.notes = params["notes"]
        return hardware

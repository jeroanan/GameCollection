import cherrypy
from Hardware import Hardware
from UI.Handlers.Handler import Handler


class UpdateHardwareHandler(Handler):

    def get_page(self, params):
        interactor = self.interactor_factory.create("UpdateHardwareInteractor")
        interactor.execute(self.__get_hardware(params))
        raise cherrypy.HTTPRedirect("/")

    def __get_hardware(self, params):
        hardware = Hardware()
        hardware.id = params.id
        hardware.name = params.name
        hardware.platform = params.platform
        hardware.num_owned = params.num_owned
        hardware.num_boxed = params.num_boxed
        hardware.notes = params.notes
        return hardware

import cherrypy
from Hardware import Hardware
from UI.Handlers.Handler import Handler


class UpdateHardwareHandler(Handler):

    def get_page(self, id, name, platform, numowned, numboxed, notes):
        interactor = self.interactor_factory.create("UpdateHardwareInteractor")
        hardware = Hardware()
        hardware.id = id
        hardware.name = name
        hardware.platform = platform
        hardware.num_owned = numowned
        hardware.num_boxed = numboxed
        hardware.notes = notes

        interactor.execute(hardware)
        raise cherrypy.HTTPRedirect("/")

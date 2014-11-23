import cherrypy
from Hardware import Hardware
from UI.Handlers.Handler import Handler


class UpdateHardwareHandler(Handler):

    def get_page(self, id, name, platform, numowned, numboxed):
        interactor = self.interactor_factory.create("UpdateHardwareInteractor")
        hardware = Hardware()
        hardware.id = id
        hardware.name = name
        hardware.platform = platform
        hardware.numowned = numowned
        hardware.numboxed = numboxed

        interactor.execute(hardware)
        raise cherrypy.HTTPRedirect("/")

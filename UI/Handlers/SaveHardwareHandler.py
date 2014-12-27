import cherrypy
from Hardware import Hardware
from UI.Handlers.Handler import Handler


class SaveHardwareHandler(Handler):

    def get_page(self, name, platform, numowned, numboxed, notes):
        interactor = self.interactor_factory.create("SaveHardwareInteractor")
        hardware = Hardware()
        hardware.name = name
        hardware.platform = platform
        hardware.numowned = numowned
        hardware.numboxed = numboxed
        hardware.notes = notes
        interactor.execute(hardware)
        raise cherrypy.HTTPRedirect("/")

import cherrypy
from Hardware import Hardware
from UI.Handlers.Handler import Handler


class SaveHardwareHandler(Handler):

    def get_page(self, name, platform, numowned, numboxed):
        interactor = self.interactor_factory.create("SaveHardwareInteractor")
        hardware = Hardware()
        hardware.name = name
        hardware.platform = platform
        hardware.numowned = numowned
        hardware.numboxed = numboxed
        interactor.execute(hardware)
        raise cherrypy.HTTPRedirect("/")

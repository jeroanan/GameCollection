import cherrypy
from UI.Handlers.Handler import Handler


class DeleteHardwareHandler(Handler):

    def get_page(self, hardware_id):
        interactor = self.interactor_factory.create("DeleteHardwareInteractor")
        interactor.execute(hardware_id)
        raise cherrypy.HTTPRedirect("/")

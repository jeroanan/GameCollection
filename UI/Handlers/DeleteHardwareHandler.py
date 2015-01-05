import cherrypy
from UI.Handlers.Handler import Handler


class DeleteHardwareHandler(Handler):

    def get_page(self, args):
        interactor = self.interactor_factory.create("DeleteHardwareInteractor")
        interactor.execute(args.get("hardwareid", ""))
        raise cherrypy.HTTPRedirect("/")

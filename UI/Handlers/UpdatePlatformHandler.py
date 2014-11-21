import cherrypy
from UI.Handlers.Handler import Handler


class UpdatePlatformHandler(Handler):

    def get_page(self, id, name, description):
        interactor = self.interactor_factory.create("UpdatePlatformInteractor")
        interactor.execute()
        raise cherrypy.HTTPRedirect("/platforms")

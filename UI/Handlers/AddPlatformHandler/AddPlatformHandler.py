import cherrypy
from Platform import Platform
from UI.Handlers.Handler import Handler


class AddPlatformHandler(Handler):

    def get_page(self, platform):
        interactor = self.interactor_factory.create("AddPlatformInteractor")
        p = Platform()
        p.name = platform.name
        p.description = platform.description
        interactor.execute(p)
        raise cherrypy.HTTPRedirect("/platforms")
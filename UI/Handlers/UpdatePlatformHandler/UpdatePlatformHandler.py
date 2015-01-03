import cherrypy
from Platform import Platform
from UI.Handlers.Handler import Handler


class UpdatePlatformHandler(Handler):

    def get_page(self, params):
        interactor = self.interactor_factory.create("UpdatePlatformInteractor")
        platform = Platform()
        platform.id = params.id
        platform.name = params.name
        platform.description = params.description
        interactor.execute(platform=platform)
        raise cherrypy.HTTPRedirect("/platforms")

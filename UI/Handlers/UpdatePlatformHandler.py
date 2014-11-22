import cherrypy
from Platform import Platform
from UI.Handlers.Handler import Handler


class UpdatePlatformHandler(Handler):

    def get_page(self, id, name, description):
        interactor = self.interactor_factory.create("UpdatePlatformInteractor")
        platform = Platform()
        platform.id = id
        platform.name = name
        platform.description = description
        interactor.execute(platform)
        raise cherrypy.HTTPRedirect("/platforms")

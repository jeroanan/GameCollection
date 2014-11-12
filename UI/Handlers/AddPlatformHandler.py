import cherrypy
from Platform import Platform
from UI.Handlers.Handler import Handler


class AddPlatformHandler(Handler):

    def get_page(self, name, description):
        interactor = self.interactor_factory.create("AddPlatformInteractor")
        platform = Platform()
        platform.name = name
        platform.description = description
        interactor.execute(platform)
        raise cherrypy.HTTPRedirect("/platforms")
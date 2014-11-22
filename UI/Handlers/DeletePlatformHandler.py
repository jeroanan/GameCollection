import cherrypy
from Platform import Platform
from UI.Handlers.Handler import Handler


class DeletePlatformHandler(Handler):

    def get_page(self, platformid):
        interactor = self.interactor_factory.create("DeletePlatformInteractor")
        platform = Platform()
        platform.id = platformid
        interactor.execute(platform)
        raise cherrypy.HTTPRedirect("/platforms")

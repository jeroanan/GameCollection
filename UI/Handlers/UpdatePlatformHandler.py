import cherrypy
from Platform import Platform
from UI.Handlers.Handler import Handler


class UpdatePlatformHandler(Handler):

    def get_page(self, params):
        interactor = self.interactor_factory.create("UpdatePlatformInteractor")
        platform = self.__get_platform(params)
        interactor.execute(platform=platform)
        raise cherrypy.HTTPRedirect("/platforms")

    def __get_platform(self, params):
        platform = Platform()
        platform.id = params.get("id", "")
        platform.name = params.get("name", "")
        platform.description = params.get("description", "")
        return platform

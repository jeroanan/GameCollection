import cherrypy
from Platform import Platform
from UI.Handlers.Handler import Handler


class DeletePlatformHandler(Handler):

    def get_page(self, params):
        interactor = self.interactor_factory.create("DeletePlatformInteractor")
        interactor.execute(self.__get_platform(params))
        raise cherrypy.HTTPRedirect("/platforms")

    def __get_platform(self, params):
        platform = Platform()
        platform.id = params.get("platformid", "")
        return platform

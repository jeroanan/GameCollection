import cherrypy
from Platform import Platform
from UI.Handlers.Handler import Handler


class DeletePlatformHandler(Handler):

    def get_page(self, params):
        interactor = self.interactor_factory.create("DeletePlatformInteractor")
        interactor.execute(params.get("platformid", params.get("id", "")))
        raise cherrypy.HTTPRedirect("/platforms")


import cherrypy
from Platform import Platform
from UI.Handlers.Handler import Handler


class AddPlatformHandler(Handler):

    def get_page(self, platform):        
        if not self.__validate_args(platform):
            return ""
        interactor = self.interactor_factory.create("AddPlatformInteractor")
        p = Platform()
        p.name = platform.get("name", "")
        p.description = platform.get("description", "")
        interactor.execute(p)
        raise cherrypy.HTTPRedirect("/platforms")

    def __validate_args(self, args):
        return "name" in args and args["name"] != ""
            

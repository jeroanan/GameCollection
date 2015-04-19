import cherrypy
from Platform import Platform
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class AddPlatformHandler(AuthenticatedHandler):

    def get_page(self, args):        
        super().get_page(args)
        if not self.validate_params(args, ["name"]):
            return ""
        interactor = self.interactor_factory.create("AddPlatformInteractor")        
        interactor.execute(self.__get_platform(args))

    def __get_platform(self, args):
        p = Platform()
        p.name = args.get("name", "")
        p.description = args.get("description", "")
        return p

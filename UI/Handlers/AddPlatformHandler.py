import cherrypy
from Platform import Platform
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class AddPlatformHandler(AuthenticatedHandler):

    def get_page(self, args):        
        super().get_page(args)
        if not self.validate_params(args, ["name"]):
            return ""
        interactor = self.interactor_factory.create("AddPlatformInteractor")        
        interactor.execute(Platform.from_dict(args))

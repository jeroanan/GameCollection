from Platform import Platform
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class UpdatePlatformHandler(AuthenticatedHandler):

    def get_page(self, params):
        super().get_page(params)
        if not self.__validate_params(params):
            return ""
        
        interactor = self.interactor_factory.create("UpdatePlatformInteractor")
        platform = self.__get_platform(params)
        try:
            interactor.execute(platform=platform)
        except:
            return ""

    def __validate_params(self, params):
        if params is None:
            return False
        return self.validate_params(params, ["id", "name"])

    def __get_platform(self, params):
        platform = Platform()
        platform.id = params.get("id", "")
        platform.name = params.get("name", "")
        platform.description = params.get("description", "")
        return platform

    

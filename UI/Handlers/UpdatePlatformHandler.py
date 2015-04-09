from Platform import Platform
from UI.Handlers.Handler import Handler


class UpdatePlatformHandler(Handler):

    def get_page(self, params):
        self.check_session()
        self.redirect_if_not_logged_in()
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
        param_names = ["id", "name"]
        invalid_params = sum(map(lambda x: x not in params or params[x] == "", param_names))
        return invalid_params == 0

    def __get_platform(self, params):
        platform = Platform()
        platform.id = params.get("id", "")
        platform.name = params.get("name", "")
        platform.description = params.get("description", "")
        return platform

    

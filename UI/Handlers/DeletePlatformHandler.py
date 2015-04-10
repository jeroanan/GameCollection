from Platform import Platform
from UI.Handlers.Handler import Handler


class DeletePlatformHandler(Handler):

    def get_page(self, params):
        self.check_session()
        self.redirect_if_not_logged_in()
        if not self.__validate_params(params):
            return ""
        interactor = self.interactor_factory.create("DeletePlatformInteractor")
        try:
            interactor.execute(params.get("platformid", params.get("id", "")))
        except:
            return ""

    def __validate_params(self, params):
        return "platformid" in params and params["platformid"] != ""

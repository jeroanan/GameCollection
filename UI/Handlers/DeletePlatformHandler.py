from Platform import Platform
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class DeletePlatformHandler(AuthenticatedHandler):

    def get_page(self, params):
        super().get_page(params)
        
        if not self.validate_params(params, ["platformid"]):
            return ""

        interactor = self.interactor_factory.create("DeletePlatformInteractor")
        try:
            interactor.execute(params.get("platformid", params.get("id", "")))
        except:
            return ""

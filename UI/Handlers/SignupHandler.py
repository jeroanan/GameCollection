from UI.Handlers.Handler import Handler


class SignupHandler(Handler):
    def get_page(self, params):
        interactor = self.interactor_factory.create("AddUserInteractor")
        interactor.execute(params.get("userid", ""), params.get("password", ""))

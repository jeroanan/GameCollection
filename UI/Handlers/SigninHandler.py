from Cryptography.BCryptHashProvider import BCryptHashProvider
from UI.Handlers.Handler import Handler
from User import User


class SigninHandler(Handler):
    
    def get_page(self, params):
        interactor = self.interactor_factory.create("LoginInteractor")
        interactor.set_hash_provider(BCryptHashProvider())
        return str(interactor.execute(self.__get_user(params)))

    def __get_user(self, params):
        u = User()
        u.user_id = params.get("userid", "")
        u.password = params.get("password", "")
        return u

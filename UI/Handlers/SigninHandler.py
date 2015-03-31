import cherrypy

from Cryptography.BCryptHashProvider import BCryptHashProvider
from UI.Handlers.Handler import Handler
from User import User


class SigninHandler(Handler):
    
    def get_page(self, params):
        interactor = self.interactor_factory.create("LoginInteractor")
        interactor.set_hash_provider(BCryptHashProvider())
        user = self.__get_user(params)
        success = interactor.execute(user)
        print(success)
        if success:
            print("Ahoy!")
            cherrypy.session["user_id"] = user.user_id
        return str(success)

    def __get_user(self, params):
        u = User()
        u.user_id = params.get("userid", "")
        u.password = params.get("password", "")
        return u

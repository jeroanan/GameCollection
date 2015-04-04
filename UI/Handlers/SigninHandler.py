import cherrypy

from Cryptography.BCryptHashProvider import BCryptHashProvider

from UI.Handlers.Handler import Handler
from User import User


class SigninHandler(Handler):
    
    def get_page(self, params):
        self.check_session()
        self.check_cookies()
        if not self.__validate_params(params):
            return "False"
        login_interactor = self.__get_login_interactor()
        user = self.__params_to_user(params)
        success = login_interactor.execute(user)
        if success:
            self.__do_login(user.user_id)
        return str(success)        
    
    def __validate_params(self, params):
        return "userid" in params and "password" in params

    def __get_login_interactor(self):
        interactor = self.interactor_factory.create("LoginInteractor")
        interactor.set_hash_provider(BCryptHashProvider())        
        return interactor

    def __params_to_user(self, params):
        u = User()
        u.user_id = params.get("userid", "")
        u.password = params.get("password", "")
        return u

    def __do_login(self, user_id):
        self.session.set_value("user_id", user_id)
        self.cookies.set_cookie("session_status", "1")
        self.cookies.set_cookie("user_id", user_id)

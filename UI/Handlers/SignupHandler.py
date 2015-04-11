from Cryptography.BCryptHashProvider import BCryptHashProvider
from Interactors.Exceptions.UserExistsException import UserExistsException
from User import User
from UI.Handlers.Handler import Handler

class SignupHandler(Handler):
    def get_page(self, params):        
        self.check_session()
        if not self.validate_params(params, ["userid", "password"]):
            return "False"
        u = self.__get_user_from_params(params)        
        try:
            self.__add_user(u)
        except UserExistsException:
            return "True"

        self.__do_login(u)
        return "True"
        
    def __get_user_from_params(self, params):
        return self.__get_user(params.get("userid", ""), params.get("password", ""))        

    def __get_user(self, user_id, password):
        u = User()
        u.user_id = user_id
        u.password = password        
        return u

    def __add_user(self, user):
        add_user_interactor = self.interactor_factory.create("AddUserInteractor")
        add_user_interactor.set_hash_provider(BCryptHashProvider())
        add_user_interactor.execute(user)        

    def __do_login(self, user):
        interactor = self.interactor_factory.create("LoginInteractor")
        interactor.execute(user)
        self.session.set_value("user_id", user.user_id)

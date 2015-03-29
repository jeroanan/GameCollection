from User import User
from UI.Handlers.Handler import Handler


class SignupHandler(Handler):
    def get_page(self, params):
        interactor = self.interactor_factory.create("AddUserInteractor")
        interactor.execute(self.__get_user(params.get("userid", ""), params.get("password", "")))
        
    def __get_user(self, user_id, password):
        u = User()
        u.user_id = user_id
        u.password = password
        return u

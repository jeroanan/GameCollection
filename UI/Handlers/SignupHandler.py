# Icarus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Icarus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Icarus.  If not, see <http://www.gnu.org/licenses/>.

from Cryptography.BCryptHashProvider import BCryptHashProvider
from Interactors.Exceptions.UserExistsException import UserExistsException
from User import User
from UI.Handlers.Handler import Handler

class SignupHandler(Handler):

    def get_page(self, params):        
        self.check_session()
        self.check_cookies()

        if not self.validate_params(params, ["userid", "password"]):
            return "False"
        u = self.__get_user_from_params(params)        
        entered_password = u.password
        try:            
            self.__add_user(u)
            u.password = entered_password
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
        actual_user = self.__get_user_from_database(user)
        login_interactor = self.interactor_factory.create("LoginInteractor")
        login_interactor.set_hash_provider(BCryptHashProvider())
        login_interactor.execute(user)
        self.session.set_value("user_id", actual_user.id)
        self.cookies.set_cookie("session_status", "1")
        self.cookies.set_cookie("user_id", user.user_id)

    def __get_user_from_database(self, user):
        get_user_interactor = self.interactor_factory.create("GetUserInteractor")
        return get_user_interactor.execute(user)

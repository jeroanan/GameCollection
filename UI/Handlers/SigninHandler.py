# Copyright (c) 2015 David Wilson
# This file is part of Icarus.

# Icarus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Icarus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Icarus.  If not, see <http://www.gnu.org/licenses/>

import json
import cherrypy

from Cryptography.BCryptHashProvider import BCryptHashProvider

from UI.Handlers.Handler import Handler
from User import User


class SigninHandler(Handler):
    # Handler for signing into Icarus

    def get_page(self, params):
        """Method that receives the call to sign in.
        :param params: A dictionary containinng the params from the client. Expected keys are:
          * userid -- the user id of the login request
          * password -- the password
        :returns: "True" if login succeeded. "False" if not. Also, if login is successful the 
                   "session_status" and "user_id" cookies are set. 
                    The user id is recorded against the session.
        """
        self.check_session()
        self.check_cookies()

        if not self.validate_params(params, ["userid", "password"]):
            return json.dumps({'result': 'failed', 'message': 'failed_validation'})

        user = User.from_dict(params)
        success = self.__login_check(user)

        if success.get('result', '') == 'ok':
            self.__do_login(user)

        return json.dumps(success)

    def __login_check(self, user):
        def get_login_interactor():
            interactor = self.interactor_factory.create("LoginInteractor")
            interactor.set_hash_provider(BCryptHashProvider())        
            return interactor

        def login_status_to_json(login_status):
            if login_status:
                return {'result': 'ok', 'message': 'success'}
            return {'result': 'failed', 'message': 'invalid'}

        login_interactor = get_login_interactor()
        return login_status_to_json(login_interactor.execute(user))

    def __do_login(self, user):
        def get_actual_user():
            get_user_interactor = self.interactor_factory.create("GetUserInteractor")
            return get_user_interactor.execute(user)

        db_user = get_actual_user()
        self.session.set_value("user_id", db_user.id)
        self.cookies.set_cookie("session_status", "1")
        self.cookies.set_cookie("user_id", db_user.user_id)

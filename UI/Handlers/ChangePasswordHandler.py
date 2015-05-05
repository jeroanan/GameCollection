# Copyright (C) 2015 David Wilson
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
from UI.Handlers.Handler import Handler
from User import User

class ChangePasswordHandler(Handler):
    
    def get_page(self, params):
        """Handle parameters for changing the password.
        param params: A dictionary that is expected to contain user_id and password entries.
        TypeError will be thrown when params is None.
        ValueError will be thrown if user_id or password are None/empty.
        """
        def validate():
            if params is None:
                raise TypeError
                
            def throw_if_empty(x):
                if params.get(x, "") =="": raise ValueError(x)

            ps = ["user_id", "password"]
            list(map(throw_if_empty, ps))            


        validate()
        interactor = self.interactor_factory.create("ChangePasswordInteractor")
        interactor.interactor_factory = self.interactor_factory
        interactor.set_hash_provider(BCryptHashProvider())
        u = User()
        u.user_id = params["user_id"]
        u.password = params["password"]
        interactor.execute(u)

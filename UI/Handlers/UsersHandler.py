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
# along with Icarus.  If not, see <http://www.gnu.org/licenses/>.

from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class UsersHandler(AuthenticatedHandler):
    
    def get_page(self, params):
        super().get_page(params)
        interactor = self.interactor_factory.create("GetUsersInteractor")
        users = interactor.execute()
        return self.renderer.render("users.html", title="User Management", users=users)

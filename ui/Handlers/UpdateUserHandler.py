"""Handles requests to update the details of a user"""
# Copyright (c) 2015, 2026 David Wilson
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

from ui.Handlers.AuthenticatedHandler import AuthenticatedHandler
from icarus_user import User

class UpdateUserHandler(AuthenticatedHandler):
    """Handles requests to update the details of a user"""

    def get_page(self, params):
        """Handles requests to update the details of a user
        :param params: A dictionary containing the following keys:
                       * id
        """
        super().get_page(params)
        interactor = self.interactor_factory.create("UpdateUserInteractor")
        interactor.execute(User.from_dict(params))

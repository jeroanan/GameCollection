"""Handles requests to add a genre"""
# Copyright (c) David Wilson 2015, 2026
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

from genre import Genre
from ui.handlers.authenticated_handler import AuthenticatedHandler


class AddGenreHandler(AuthenticatedHandler):
    """Handles requests to add a genre"""

    def get_page(self, params):
        """Handle requests to add a genre.
        :param params: A dictionary containing the details of the genre to add. The dictionary 
                       can contain the following keys:
                          * name
                          * description
        """
        super().get_page(params)
        if not self.validate_params(params, ["name"]):
            raise ValueError("name")

        if not self.validate_params(params, ["description"]):
            raise ValueError("description")

        interactor = self.interactor_factory.create("AddGenreInteractor")
        interactor.execute(Genre.from_dict(params))

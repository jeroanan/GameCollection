# Copyright (c) 20115 David Wilson
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

from Genre import Genre
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler

class DeleteGenreHandler(AuthenticatedHandler):
    # Handles requests to delete a genre

    def get_page(self, params):
        """Handles a request to delete a genre.
        :param params: A dictionary containing the following keys:
           * id
        :returns: None
        """
        super().get_page(params)
        interactor = self.interactor_factory.create("DeleteGenreInteractor")
        interactor.execute(Genre.from_dict(params))

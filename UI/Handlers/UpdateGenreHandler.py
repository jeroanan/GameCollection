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


class UpdateGenreHandler(AuthenticatedHandler):
    # Handle requests to update a genre

    def get_page(self, params):
        """Update a genre given in the params dictionary. This function is designed
        to be called as an ajax call and gives no HTML output.
        :param params: A dictionary containing the details of the genre. Expected keys are:
           * id
           * name
           * description
        :returns: An empty string
        """
        interactor = self.interactor_factory.create("UpdateGenreInteractor") 
        interactor.execute(Genre.from_dict(params))
        return ""

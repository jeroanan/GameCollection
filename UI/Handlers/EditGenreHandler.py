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

class EditGenreHandler(AuthenticatedHandler):
    """Handles requests to edit a genre"""

    def get_page(self, params):
        """Handle a request to edit a genre.
        :param params: A dictionary containing the following keys: 
                          * genreid
        :returns: A rendered HTML page containing the details of the given genre
        """
        super().get_page(params)
        interactor = self.interactor_factory.create("GetGenreInteractor")
        genre = interactor.execute(params.get("genreid", ""))
        return self.renderer.render("editgenre.html", genre=genre, title="Edit Genre")

# Copyright (c) David Wilson 2015
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
from Interactors.GenreInteractors import AddGenreInteractor
from Interactors.InteractorFactory import InteractorFactory
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class AddGenreHandler(AuthenticatedHandler):
    """Handles requests to add a genre"""

    def __init__(self, interactor_factory, renderer):
        """Initialise handler"""
        super().__init__(interactor_factory, renderer)        

    def get_page(self, params):
        """Handle requests to add a genre.
        :param params: A dictionary containing the details of the genre to add. The dictionary can contain the 
                       following keys:
                          * name
                          * description
        """
        super().get_page(params)
        if not self.validate_params(params, ["name", "description"]):
            return ""
        interactor = self.interactor_factory.create("AddGenreInteractor")
        interactor.execute(Genre.from_dict(params))

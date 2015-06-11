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

import UI.Handlers.AuthenticatedHandler as ah


class GenresHandler(ah.AuthenticatedHandler):
    """Handle requests for the genre management page."""

    def __init__(self, interactor_factory, renderer):
        """Initialise the handler"""
        super().__init__(interactor_factory, renderer)
    
    def get_page(self, args):
        """Get data and render the page for the genre management page.
        :returns: A rendered genre management page."""
        super().get_page(args)
        
        def get_from_interactor(interactor_type):
            interactor = self.interactor_factory.create(interactor_type)
            return interactor.execute()

        genres, suggested_genres = (get_from_interactor("GetGenresInteractor"), 
                                    get_from_interactor("GetSuggestedGenresInteractor"))

        return self.renderer.render("genres.html", title="Manage Genres", genres=genres, 
                                    suggested_genres=suggested_genres)

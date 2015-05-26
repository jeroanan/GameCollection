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

from Interactors.Interactor import Interactor


class AddGenreInteractor(Interactor):
    """Add a new genre"""

    def execute(self, genre):
        """Add a new genre.
        :param genre: An object of type Genre. The genre to be added"""
        if genre is None:
            raise TypeError("genre")
        self.validate_string_field("Name", genre.name)

        return self.persistence.add_genre(genre)


class DeleteGenreInteractor(Interactor):
    """Delete a genre"""

    def execute(self, genre):
        """Delete a genre.
        :param genre: An object of type Genre. The genre to be deleted"""
        self.persistence.delete_genre(genre.id)


class GetGenreInteractor(Interactor):
    """Get a genre"""

    def execute(self, genre_id):
        """Get a genre from persistence.
        :param genre_id: The id of the genre to retrieve.
        :returns: An object of type Genre containing details of the requested genre.
        """
        return self.persistence.get_genre_details(genre_id)


class GetGenresInteractor(Interactor):
    """Get all genres"""
    
    def execute(self):
        """Get all genres from persistence
        :returns: A list of Genre objects representing all genres in the system."""
        return self.persistence.get_genres()


class UpdateGenreInteractor(Interactor):
    """Update a genre"""
    def execute(self, genre):
        """Update a genre
        :param genre: An object of type Genre. The genre to be updated."""
        self.persistence.update_genre(genre)

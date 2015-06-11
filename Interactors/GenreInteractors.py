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

import Interactors.Interactor as i


class AddGenreInteractor(i.Interactor):
    """Add a new genre"""

    def execute(self, genre):
        """Add a new genre.
        :param genre: An object of type Genre. The genre to be added"""
        if genre is None:
            raise TypeError("genre")
        self.validate_string_field("Name", genre.name)

        return self.persistence.add_genre(genre)


class DeleteGenreInteractor(i.Interactor):
    """Delete a genre"""

    def execute(self, genre):
        """Delete a genre.
        :param genre: An object of type Genre. The genre to be deleted"""
        self.persistence.delete_genre(genre.id)


class GetGenreInteractor(i.Interactor):
    """Get a genre"""

    def execute(self, genre_id):
        """Get a genre from persistence.
        :param genre_id: The id of the genre to retrieve.
        :returns: An object of type Genre containing details of the requested genre.
        """
        return self.persistence.get_genre_details(genre_id)


class GetGenresInteractor(i.Interactor):
    """Get all genres"""
    
    def execute(self):
        """Get all genres from persistence
        :returns: A list of Genre objects representing all genres in the system."""
        return self.persistence.get_genres()


class GetSuggestedGenresInteractor(i.Interactor):
    
    def __init__(self, get_suggested_genres):
        super().__init__()
        self.__get_suggested_genres = get_suggested_genres

    def execute(self):
        genres = list(self.persistence.get_genres())
        suggested_genres = self.__get_suggested_genres()
        result = [s for s in suggested_genres if s not in genres]
        return sorted(result, key=lambda x: x.name)


class UpdateGenreInteractor(i.Interactor):
    """Update a genre"""
    def execute(self, genre):
        """Update a genre
        :param genre: An object of type Genre. The genre to be updated."""
        self.persistence.update_genre(genre)

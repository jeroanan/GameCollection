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

from Interactors.Interactor import Interactor


class GetGenreInteractor(Interactor):

    def execute(self, genre_id):
        """Get a genre from persistence.
        :param genre_id: The id of the genre to retrieve.
        :returns: An object of type Genre containing details of the requested genre.
        """
        return self.persistence.get_genre_details(genre_id)

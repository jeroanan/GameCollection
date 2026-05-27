"""Represents a Genre"""
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

from dataclasses import dataclass, field

@dataclass
class Genre:
    """Represents a Genre"""
    id: str = field(default="")
    name: str = field(default="")
    description: str = field(default="")

    @staticmethod
    def from_dict(dictionary: dict[str, str]) -> 'Genre':
        """Creates a new Genre object based on a provided dictionary.
        :param d: A dictionary with the following keys:
           * name
           * description
        :returns: An object of type Genre with its properties set. Missing keys
        from the dictionary will cause that parameter in the object to be left as its default."""
        genre = Genre()
        genre.id = dictionary.get("id", genre.id)
        genre.name = dictionary.get("name", genre.name)
        genre.description = dictionary.get("description", genre.description)
        return genre

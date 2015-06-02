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

class Genre(object):
    """Represents a Genre"""

    def __init__(self):
        """Initialise object state"""
        self.__id = ""
        self.__name = ""
        self.__description = ""

    @property
    def id(self):
        """Get the genre id"""
        return self.__id

    @id.setter
    def id(self, value):
        """Set the genre id"""
        self.__id = value

    @property
    def name(self):
        """Get the genre name"""
        return self.__name

    @name.setter
    def name(self, value):
        """Set the genre name"""
        self.__name = value

    @property
    def description(self):
        """Get the genre description"""
        return self.__description

    @description.setter
    def description(self, value):
        """Set the genre description"""
        self.__description = value

    def __eq__(self, other):
        """Test that this instance of Genre is equal to another.
        This happens by comparing the following properties:
           * id
           * name
        :returns: True if this instance of Genre matches other, otherwise False
        """
        return self.id == other.id and self.name == other.name

    @staticmethod
    def from_dict(dictionary):
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

    @staticmethod
    def from_mongo_result(mongo_result):
        """Creates a nw Genre object based on the provided result from MongoDB.
        :param mongo_result: A dictionary wiht the following keys:
           * _id
           * _Genre__name
           * _Genre__description
        :returns: An object of type Genre with its properties set. Missing keys
        from the dictionary will cause that parameter in the object to be left as its default."""
        genre = Genre()
        genre.id = mongo_result.get("_id", genre.id)
        genre.name = mongo_result.get("_Genre__name", genre.name)
        genre.description = mongo_result.get("_Genre__description", genre.description)
        return genre

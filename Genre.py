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

    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__description = ""

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name

    @staticmethod
    def from_dict(d):
        """Creates a new Genre object based on a provided dictionary.
        :param d: A dictionary with the following keys:
           * name
           * description
        :returns: An object of type Genre with its properties set. Missing keys
        from the dictionary will cause that parameter in the object to be left as its default."""
        g = Genre()
        g.name = d.get("name", g.name)
        g.description = d.get("description", g.description)
        return g
    
    @staticmethod
    def from_mongo_result(mongo_result):
        """Creates a nw Genre object based on the provided result from MongoDB.
        :param mongo_result: A dictionary wiht the following keys:
           * _id
           * _Genre__name
           * _Genre__description
        :returns: An object of type Genre with its properties set. Missing keys
        from the dictionary will cause that parameter in the object to be left as its default."""
        g = Genre()
        g.id = mongo_result.get("_id", g.id)
        g.name = mongo_result.get("_Genre__name", g.name)
        g.description = mongo_result.get("_Genre__description", g.description)
        return g

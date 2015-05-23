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

class Platform(object):
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
        return self.name == other.name and self.description == other.description
        
    @staticmethod
    def from_dict(d):
        """Initialises an instance of Platform from a dictionary.
        :param d: A dictionary containing the following keys:
           * name
           * description
        :returns: An instance of Platform with its properties set. Keys missing from d
                  will be initialised to their default values.
        """
        p = Platform()
        p.name = d.get("name", p.name)
        p.description = d.get("description", p.description)
        return p

    @staticmethod
    def from_mongo_result(mongo_result):
        """Initialises an instance of Platform from a dictionary.
        :param mongo_result: A MongoDB result as a dictionary. The following keys are expected:
           * _id
           * _Platform__name
           * _Platform__description
        :returns: An instance of Platform with its properties set. Keys missing from mongo_result
                  will be initialised to their default values.
        """
        p =  Platform()
        p.id = mongo_result["_id"]
        p.name = mongo_result["_Platform__name"]
        p.description = mongo_result["_Platform__description"]
        return p

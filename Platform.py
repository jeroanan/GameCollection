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
    """Represents a platform"""

    def __init__(self):
        """Initialise object state"""
        self.__id = ""
        self.__name = ""
        self.__description = ""

    @property
    def id(self):
        """Get the platform id"""
        return self.__id

    @id.setter
    def id(self, value):
        """Set the platform id"""
        self.__id = value

    @property
    def name(self):
        """Get the platform name"""
        return self.__name

    @name.setter
    def name(self, value):
        """Set the platform name"""
        self.__name = value

    @property
    def description(self):
        """Get the platform description"""
        return self.__description

    @description.setter
    def description(self, value):
        """Set the platform description"""
        self.__description = value

    def __eq__(self, other):
        """Test that this instance of Platform is equal to another.
        This happens by comparing the following properties:
           * name
           * description
        :param other: Another instance of Platform
        :returns: True if the two instances of Platform, otherwise False
        """
        return self.name == other.name and self.description == other.description

    @staticmethod
    def from_dict(dictionary):
        """Initialises an instance of Platform from a dictionary.
        :param d: A dictionary containing some or all of the following keys:
           * id
           * name
           * description
        :returns: An instance of Platform with its properties set. Keys missing from d
                  will be initialised to their default values.
        """
        platform = Platform()
        platform.id = dictionary.get("id", platform.id)
        platform.name = dictionary.get("name", platform.name)
        platform.description = dictionary.get("description", platform.description)
        return platform

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
        platform = Platform()
        platform.id = mongo_result["_id"]
        platform.name = mongo_result["_Platform__name"]
        platform.description = mongo_result["_Platform__description"]
        return platform

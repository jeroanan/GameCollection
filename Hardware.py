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

import functools as ft
import json


class Hardware():
    """Represents an item of hardware"""

    def __init__(self):
        """Initialise object state"""
        self.__id = ""
        self.__hardware_type = ""
        self.__name = ""
        self.__platform = ""
        self.__num_owned = ""
        self.__num_boxed = ""
        self.__notes = ""
        self.__user_id = ""

    @property
    def id(self):
        """Get the unique identifier of the hardware item"""
        return self.__id

    @id.setter
    def id(self, value):
        """Set the unique identifier of the hardware item"""
        self.__id = value

    @property
    def hardware_type(self):
        """Get the hardware type of the hardware item"""
        return self.__hardware_type

    @hardware_type.setter
    def hardware_type(self, val):
        """Set the hardware type of the hardware item"""
        self.__hardware_type = val

    @property
    def name(self):
        """Get the name of the hardware item"""
        return self.__name

    @name.setter
    def name(self, value):
        """Set the name of the hardware item"""
        self.__name = value

    @property
    def platform(self):
        """Get the platform of the hardware item"""
        return self.__platform

    @platform.setter
    def platform(self, value):
        """Set the platform of the hardware item"""
        self.__platform = value

    @property
    def num_owned(self):
        """Get the number of pieces of this hardware item owned"""
        return self.__num_owned

    @num_owned.setter
    def num_owned(self, value):
        """Set the number of pieces of this hardware item owned"""
        self.__num_owned = value

    @property
    def num_boxed(self):
        """Get the number of pieces of this hardware item boxed"""
        return self.__num_boxed

    @num_boxed.setter
    def num_boxed(self, value):
        """Set the number of pieces of this hardware item boxed"""
        self.__num_boxed = value

    @property
    def notes(self):
        """Get notes for this hardware item"""
        return self.__notes

    @notes.setter
    def notes(self, value):
        """Set notes for this hardware item"""
        self.__notes = value

    @property
    def user_id(self):
        """Get the user_id against this hardware item"""
        return self.__user_id

    @user_id.setter
    def user_id(self, value):
        """Set the user_id against this hardware item"""
        self.__user_id = value

    def __eq__(self, other):
        """Is this instance of Hardware equal to another instance of hardware?
        The following fields are checked for equality:
           * id
           * name
           * num_owned
           * num_boxed
           * notes
           * user_id
        :param other: An instance of Hardware. The object to compare the current one against
        :returns: True if this object is equal to other. Otherwise False
        """
        return (self.id == other.id and self.name == other.name and 
                self.num_owned == other.num_owned and self.num_boxed == other.num_boxed and 
                self.notes == other.notes and self.user_id == other.user_id)

    @staticmethod
    def from_mongo_result(mongo_result):
        """Initialises Hardware object from a MongoDB result.
        :param mongo_result: A MongoDB result as a dictionary. The following keys are expected:
                             * _id
                             * _Hardware__name
                             * _Hardware__num_owned
                             * _Hardware__num_boxed
                             * _Hardware__notes
                             * _Hardware__hardware_type
        :returns: A Hardware object with its properties properly initialised. 
                  Any missing keys from mongo_db will cause the object to have that property 
                  initialised as its default.
        """
        # hardware.attr, mongo_result.key
        mappings = {"id": "_id",
                    "name": "_Hardware__name",
                    "platform": "_Hardware__platform",
                    "num_owned": "_Hardware__num_owned",
                    "num_boxed": "_Hardware__num_boxed",
                    "notes": "_Hardware__notes",
                    "hardware_type": "_Hardware__hardware_type"}

        return Hardware._from_dict(mongo_result, mappings)

    @staticmethod
    def from_dict(dictionary):
        """Initialises Hardware object from a dictionary.
        :param d: A dictionary containing the following keys:
                 * name
                 * platform
                 * numcopies
                 * numboxed
                 * notes
                 * hardware_type
        :returns: A Hardware object with its properties properly initialised. Any missing keys from d will cause the
                  object to have that properly initialised as its default.
        """

        # hardware.attr, d.key
        mappings = {"id": "id",
                    "name": "name",
                    "platform": "platform",
                    "num_owned": "numcopies",
                    "num_boxed": "numboxed",
                    "notes": "notes",
                    "user_id": "userid",
                    "hardware_type": "hardwaretype"}

        return Hardware._from_dict(dictionary, mappings)

    @staticmethod
    def _from_dict(dictionary, mappings):
        hardware = Hardware()

        set_attr = ft.partial(setattr, hardware)
        get_attr = ft.partial(getattr, hardware)
        dict_get = lambda x: dictionary.get(x[0], get_attr(x[1]))

        list(map(lambda m: set_attr(m, dict_get((mappings[m],m))), mappings))
        return hardware
        
    def to_json(self):
        attrs = ["hardware_type", "name", "platform", "num_owned", "num_boxed", "notes"]
        result = {}

        result["id"] = str(self.id)
        
        for a in attrs:
            result[a] = getattr(self, a)
        
        return json.dumps(result)

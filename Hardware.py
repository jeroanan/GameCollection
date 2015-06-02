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


class Hardware():
    """Represents an item of hardware"""

    def __init__(self):
        """Initialise object state"""
        self.__id = ""
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
        :returns: A Hardware object with its properties properly initialised. 
                  Any missing keys from mongo_db will cause the object to have that property 
                  initialised as its default.
        """
        hardware = Hardware()
        hardware.id = mongo_result.get("_id", hardware.id)
        hardware.name = mongo_result.get("_Hardware__name", hardware.name)
        hardware.platform = mongo_result.get("_Hardware__platform", hardware.platform)
        hardware.num_owned = mongo_result.get("_Hardware__num_owned", hardware.num_owned)
        hardware.num_boxed = mongo_result.get("_Hardware__num_boxed", hardware.num_boxed)
        hardware.notes = mongo_result.get("_Hardware__notes", hardware.notes)
        return hardware

    @staticmethod
    def from_dict(d):
        """Initialises Hardware object from a dictionary.
        :param d: A dictionary containing the following keys:
                 * name
                 * platform
                 * numcopies
                 * numboxed
                 * notes
        :returns: A Hardware object with its properties properly initialised. Any missing keys from d will cause the
                  object to have that properly initialised as its default.
        """
        hardware = Hardware()
        hardware.id = d.get("id", hardware.id)
        hardware.name = d.get("name", hardware.name)
        hardware.platform = d.get("platform", hardware.platform)
        hardware.num_owned = d.get("numcopies", hardware.num_owned)
        hardware.num_boxed = d.get("numboxed", hardware.num_boxed)
        hardware.notes = d.get("notes", hardware.notes)
        hardware.user_id = d.get("userid", hardware.user_id)
        return hardware

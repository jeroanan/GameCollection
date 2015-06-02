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
    """An item of hardware"""

    def __init__(self):
        """Initialise field values"""
        self.__id = ""
        self.__name = ""
        self.__platform = ""
        self.__num_owned = ""
        self.__num_boxed = ""
        self.__notes = ""
        self.__user_id = ""

    @property
    def id(self):
        """The unique identifier of the hardware item"""
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        """The name of the hardware item"""
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def platform(self):
        """The platform of the hardware item"""
        return self.__platform

    @platform.setter
    def platform(self, value):
        self.__platform = value

    @property
    def num_owned(self):
        """The number of pieces of this hardware item owned"""
        return self.__num_owned

    @num_owned.setter
    def num_owned(self, value):
        self.__num_owned = value

    @property
    def num_boxed(self):
        """The number of pieces of this hardware item boxed"""
        return self.__num_boxed

    @num_boxed.setter
    def num_boxed(self, value):
        self.__num_boxed = value

    @property
    def notes(self):
        """Notes for this hardware item"""
        return self.__notes

    @notes.setter
    def notes(self, value):
        self.__notes = value

    @property 
    def user_id(self):
        """The user_id against this hardware item"""
        return self.__user_id 

    @user_id.setter
    def user_id(self, value):
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
        return (self.id == other.id and self.name == other.name and self.num_owned == other.num_owned and
                self.num_boxed == other.num_boxed and self.notes == other.notes and self.user_id == other.user_id)

    @staticmethod
    def from_mongo_result(mongo_result):
        """Initialises Hardware object from a MongoDB result.
        :param mongo_result: A MongoDB result as a dictionary. The following keys are expected:
                             * _id
                             * _Hardware__name
                             * _Hardware__num_owned
                             * _Hardware__num_boxed
                             * _Hardware__notes
        :returns: A Hardware object with its properties properly initialised. Any missing keys from mongo_db will cause 
                  the object to have that property initialised as its default.
        """
        h = Hardware()
        h.id = mongo_result.get("_id", h.id)
        h.name = mongo_result.get("_Hardware__name", h.name)
        h.platform = mongo_result.get("_Hardware__platform", h.platform)
        h.num_owned = mongo_result.get("_Hardware__num_owned", h.num_owned)
        h.num_boxed = mongo_result.get("_Hardware__num_boxed", h.num_boxed)
        h.notes = mongo_result.get("_Hardware__notes", h.notes)
        return h

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
        h = Hardware()
        h.id = d.get("id", h.id)
        h.name = d.get("name", h.name)
        h.platform = d.get("platform", h.platform)
        h.num_owned = d.get("numcopies", h.num_owned)
        h.num_boxed = d.get("numboxed", h.num_boxed)
        h.notes = d.get("notes", h.notes)
        h.user_id = d.get("userid", h.user_id)
        return h

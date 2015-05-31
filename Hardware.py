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

    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__platform = ""
        self.__num_owned = ""
        self.__num_boxed = ""
        self.__notes = ""

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
    def platform(self):
        return self.__platform

    @platform.setter
    def platform(self, value):
        self.__platform = value

    @property
    def num_owned(self):
        return self.__num_owned

    @num_owned.setter
    def num_owned(self, value):
        self.__num_owned = value

    @property
    def num_boxed(self):
        return self.__num_boxed

    @num_boxed.setter
    def num_boxed(self, value):
        self.__num_boxed = value

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, value):
        self.__notes = value

    def __eq__(self, other):
        return (self.id == other.id and self.name == other.name and self.num_owned == other.num_owned and
                self.num_boxed == other.num_boxed and self.notes == other.notes)

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
        return h

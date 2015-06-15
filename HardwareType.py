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

import functools as ft


class HardwareType(object):
    """Represents a type of hardware"""
    
    def __init__(self):
        """Initialise object state"""
        self.__id = ""
        self.__name = ""
        self.__description = ""

    @property
    def id(self):
        """Get the hardware type id"""
        return self.__id

    @id.setter
    def id(self, val):
        """Set the hardware type id"""
        self.__id = val

    @property
    def name(self):
        """Get the hardware type name"""
        return self.__name

    @name.setter
    def name(self, val):
        """Set the hardware type name"""
        self.__name = val
        
    @property
    def description(self):
        """Get the hardware type description"""
        return self.__description

    @description.setter
    def description(self, val):
        """Set the hardware type description"""
        self.__description = val

    @staticmethod
    def from_dict(dictionary):
        mappings = ["id", "name", "description"]
        hardware_type = HardwareType()

        set_attr = ft.partial(setattr, hardware_type)
        get_attr = ft.partial(getattr, hardware_type)

        list(map(lambda m: set_attr(m, dictionary.get(m, get_attr(m))), mappings))
        return hardware_type
        
    def __eq__(self, other):
        return self.name == other.name

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

class GetHardwareListInteractorParams(object):
    """Parameters to be passed to GetHardwareListInteractor.execute"""

    def __init__(self):
        """Initialise object state"""        
        self.__number_of_items = 999999
        self.__platform = None
        self.__sort_field = ""
        self.__sort_direction = ""
        self.__user_id = ""

    @property
    def number_of_items(self):
        """Get the number of hardware items to retrieve"""
        return self.__number_of_items

    @number_of_items.setter
    def number_of_items(self, val):
        """Set the number of hardware items to retrieve"""
        self.__number_of_items = val

    @property
    def sort_field(self):
        """Get the field to sort hardware items by"""
        return self.__sort_field

    @sort_field.setter
    def sort_field(self, val):
        """Set the field to sort hardware items by"""
        self.__sort_field = val

    @property
    def sort_direction(self):
        """Get the direction to sort hardware items in"""
        return self.__sort_direction

    @sort_direction.setter
    def sort_direction(self, val):
        """Set the direction to sort hardware items in"""
        self.__sort_direction = val

    @property
    def platform(self):
        """Get the platform to retrieve hardware for"""
        return self.__platform

    @platform.setter
    def platform(self, val):
        """Set the platform to retrieve hardware for"""
        self.__platform = val

    @property
    def user_id(self):
        """Get the user_id to retrieve games for"""
        return self.__user_id

    @user_id.setter
    def user_id(self, val):
        """Set the user_id to retrieve games for"""
        self.__user_id = val

    @staticmethod
    def from_dict(dictionary):
        """Initialises an instance of GetHardwareListInteractorParams from a dictionary.
        :param dictionary: A dictionary containing the following keys:
           * number_of_items
           * platform
           * sort_field
           * sort_direction
           * user_id
        :returns: An instance of GetHardwareListInteractorParams with its properties set. 
        Where a key from dictionary is missing, the default value is used.
        """
        p = GetHardwareListInteractorParams()
        p.number_of_items = dictionary.get("number_of_items", p.number_of_items)
        p.platform = dictionary.get("platform", p.platform)
        p.sort_field = dictionary.get("sort_field", p.sort_field)
        p.sort_direction = dictionary.get("sort_direction", p.sort_direction)
        p.user_id = dictionary.get("user_id", p.user_id)

        return p

    def __eq__(self, other):
        return (self.number_of_items==other.number_of_items and 
                self.platform==other.platform and 
                self.sort_field==other.sort_field and
                self.sort_direction==other.sort_direction and
                self.user_id==other.user_id)

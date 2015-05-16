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
    
    def __init__(self):
        self.__sort_field = ""
        self.__sort_direction = ""
        self.__user_id = ""
        self.__number_of_items = 999999

    @property
    def sort_field(self):
        return self.__sort_field

    @sort_field.setter
    def sort_field(self, val):
        self.__sort_field = val

    @property
    def sort_direction(self):
        return self.__sort_direction

    @sort_direction.setter
    def sort_direction(self, val):
        self.__sort_direction = val

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, val):
        self.__user_id = val

    @property
    def number_of_items(self):
        return self.__number_of_items

    @number_of_items.setter
    def number_of_items(self, val):
        self.__number_of_items = val

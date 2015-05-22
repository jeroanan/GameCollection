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


class User(object):

    def __init__(self):
        self.__id = ""
        self.__user_id = ""
        self.__password = ""

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, val):
        self.__user_id = val

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, val):
        self.__password = val

    @property
    def id(self):
        return self.__id
        
    @id.setter
    def id(self, val):
        self.__id = val        

    def __eq__(self, other):
        return self.user_id==other.user_id

    @staticmethod
    def from_dict(d):
        """Initialises a User object from a dictionary
        :param d: A dictionary with the following keys:
           * userid
           * password
        :returns: A populated User object. Any keys missing from d will have their values left as default.
        """
        u = User()
        u.user_id = d.get("userid", u.user_id)
        u.password = d.get("password", u.password)
        u.id = d.get("id", u.id)
        return u


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
    """Represents a User"""

    def __init__(self):
        """Initialise class state"""
        self.__id = ""
        self.__user_id = ""
        self.__password = ""

    @property
    def user_id(self):
        """Get the user's user_id"""
        return self.__user_id

    @user_id.setter
    def user_id(self, val):
        """Set the user's user_id"""
        self.__user_id = val

    @property
    def password(self):
        """Get the user's password"""
        return self.__password

    @password.setter
    def password(self, val):
        """Set the user's password"""
        self.__password = val

    @property
    def id(self):
        """Get the user's uuid"""
        return self.__id

    @id.setter
    def id(self, val):
        """Set the user's uuid"""
        self.__id = val

    def __eq__(self, other):
        """Test whether this instance of User is equal to another.
        Currently this tests both object's user_id property
        :param other: Another instance of User
        :returns: True if this instance of User is equal to other. False otherwise."""
        return self.user_id == other.user_id

    @staticmethod
    def from_dict(dictionary):
        """Initialises a User object from a dictionary
        :param d: A dictionary with the following keys:
           * userid
           * password
        :returns: A populated User object.
                  Any keys missing from d will have their values left as default.
        """
        user = User()
        user.user_id = dictionary.get("userid", user.user_id)
        user.password = dictionary.get("password", user.password)
        user.id = dictionary.get("id", user.id)
        return user

    @staticmethod
    def from_mongo_result(mongo_result):
        """Initialises a User object from a MongoDB resultset
        :param mongo_result: A dictionary with the following keys:
           * _id
           * _User__user_id
           * _User__password
        :returns: A populated User object.
                 Any keys missing from mongo_result will have their values left as default.
        """
        user = User()

        if mongo_result is None:
            return user

        user.id = mongo_result.get("_id", user.id)
        user.user_id = mongo_result.get("_User__user_id", user.user_id)
        user.password = mongo_result.get("_User__password", user.password)
        return user

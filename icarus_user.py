"""Represents a User"""
# Copyright (c) David Wilson 2015, 2026
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

from dataclasses import dataclass, field

@dataclass
class User:
    """Represents a User"""
    id: str = field(default="")
    user_id: str = field(default="")
    password: str = field(default="")

    @staticmethod
    def from_dict(dictionary: dict[str, str]) -> 'User':
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

"""Represents a platform"""
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
class Platform:
    """Represents a platform"""

    id: str = field(default="")
    name: str = field(default="")
    description: str = field(default="")

    # TODO: Probably be able to unfiy this dict stuff with the other domain objs.
    @staticmethod
    def from_dict(dictionary):
        """Initialises an instance of Platform from a dictionary.
        :param d: A dictionary containing some or all of the following keys:
           * id
           * name
           * description
        :returns: An instance of Platform with its properties set. Keys missing from d
                  will be initialised to their default values.
        """
        platform = Platform()
        platform.id = dictionary.get("id", platform.id)
        platform.name = dictionary.get("name", platform.name)
        platform.description = dictionary.get("description", platform.description)
        return platform

    @staticmethod
    def from_mongo_result(mongo_result):
        """Initialises an instance of Platform from a dictionary.
        :param mongo_result: A MongoDB result as a dictionary. The following keys are expected:
           * _id
           * _Platform__name
           * _Platform__description
        :returns: An instance of Platform with its properties set. Keys missing from mongo_result
                  will be initialised to their default values.
        """
        platform = Platform()
        platform.id = mongo_result["_id"]
        platform.name = mongo_result["_Platform__name"]
        platform.description = mongo_result["_Platform__description"]
        return platform

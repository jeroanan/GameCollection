"""Parameters to be passed to GetHardwareListInteractor.execute"""
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
class GetHardwareListInteractorParams:
    """Parameters to be passed to GetHardwareListInteractor.execute"""
    number_of_items: int = field(default=999999)
    platform: str = field(default=None)
    sort_field: str = field(default="name")
    sort_direction: str = field(default="")
    user_id: str = field(default="")

    #TODO: Cleanup, unify
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

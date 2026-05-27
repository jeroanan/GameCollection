"""Represents an item of hardware"""
# Copyright (c) 2015, 2026 David Wilson
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
import functools as ft
import json
from typing import Any

@dataclass
class Hardware():
    """Represents an item of hardware"""
    id: str = field(default="")
    hardware_type: str = field(default="")
    name: str = field(default="")
    platform: str = field(default="")
    num_owned: str = field(default="")
    num_boxed: str = field(default="")
    notes: str = field(default="")
    user_id: str = field(default="")

    @staticmethod
    def from_dict(dictionary: dict[str, Any]) -> "Hardware":
        """Initialises Hardware object from a dictionary.
        :param dictionary: A dictionary containing the following keys:
                            * name
                            * platform
                            * numcopies
                            * numboxed
                            * notes
                            * hardware_type
        :returns: A Hardware object with its properties properly initialised. Any missing keys 
                    from dictionary will cause the object to have that properly initialised as 
                    its default.
        """

        # hardware.attr, d.key
        mappings = {"id": "id",
                    "name": "name",
                    "platform": "platform",
                    "num_owned": "numcopies",
                    "num_boxed": "numboxed",
                    "notes": "notes",
                    "user_id": "userid",
                    "hardware_type": "hardwaretype"}

        return Hardware._from_dict(dictionary, mappings)

    #TODO: Can probably clean this dict stuff up between the domain objects
    @staticmethod
    def _from_dict(dictionary: dict[str, Any], mappings: dict[str, str]) -> "Hardware":
        hardware = Hardware()

        set_attr = ft.partial(setattr, hardware)
        get_attr = ft.partial(getattr, hardware)

        def dict_get(x: tuple[str, str]) -> Any:
            return dictionary.get(x[0], get_attr(x[1]))

        list(map(lambda m: set_attr(m, dict_get((mappings[m],m))), mappings))
        return hardware

    def to_json(self) -> str:
        """Convert this Hardware object to a JSON string"""

        attrs = ["hardware_type", "name", "platform", "num_owned", "num_boxed", "notes"]
        result = {}

        result["id"] = str(self.id)

        for a in attrs:
            result[a] = getattr(self, a)

        return json.dumps(result)

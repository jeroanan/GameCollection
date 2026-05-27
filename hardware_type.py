"""Represents a type of hardware"""
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
import functools as ft

@dataclass
class HardwareType:
    """Represents a type of hardware"""
    id: str = field(default="")
    name: str = field(default="")
    description: str = field(default="")

    @staticmethod
    def from_dict(dictionary: dict[str, str]) -> 'HardwareType':
        """Create HardwareType from dictionary"""
        mappings = {"id": "id",
                    "name": "name",
                    "description": "description"}
        return HardwareType._map_from_dict(dictionary, mappings)

    @staticmethod
    def _map_from_dict(dictionary: dict[str, str], mappings: dict[str, str]) -> 'HardwareType':
        hardware_type = HardwareType()

        set_attr = ft.partial(setattr, hardware_type)
        get_attr = ft.partial(getattr, hardware_type)

        list(map(lambda m:
                 set_attr(mappings[m], dictionary.get(m, get_attr(mappings[m]))), mappings))
        return hardware_type

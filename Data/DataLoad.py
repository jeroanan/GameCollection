"""Load suggested data from JSON files."""
# Copyright (c) 2015, 2026 David Wilson
# This file is part of Icarus.

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

import json

import genre
import hardware_type as hardware
import Platform as platform

# TODO: Maybe make this into a class?

#                          (filename, root_element, output_type)xc
_load_types = {"platform": ("Data/SuggestedPlatforms.json", "platforms", platform.Platform),
               "genre": ("Data/Genres.json", "genres", genre.Genre),
               "hardwaretypes": ("Data/HardwareTypes.json", "hardware_types", hardware.HardwareType)
}

def _load_data(load_type):
    """Load suggested data from a JSON file.
    :param load_type: The type of data to load. One of "platform", "genre", "hardwaretypes".
    :return: A list of the loaded data objects.
    """
    file_name, root_element, output_type = _load_types[load_type]

    with open(file_name, encoding="utf-8") as f:
        data = json.load(f)
        return [output_type.from_dict(x) for x in data[root_element]]

def load_suggested_platforms():
    """Load suggested platforms from JSON file.
    :return: A list of Platform objects.
    """
    return _load_data("platform")

def load_suggested_genres():
    """Load suggested genres from JSON file.
    :return: A list of Genre objects.
    """
    return _load_data("genre")

def load_suggested_hardware_types():
    """Load suggested hardware types from JSON file.
    :return: A list of HardwareType objects.
    """
    return _load_data("hardwaretypes")

"""Mapping utilities for handling data transformations."""
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
# along with Icarus.  If not, see <http://www.gnu.org/licenses/>

from copy import copy

def do_mapping(mappings, mongo_result, dest):
    """Maps the results of a MongoDB query to an object."""
    d = copy(dest)
    for k in mappings:
        if k in mongo_result:
            setattr(d, mappings[k], mongo_result[k])
    return d

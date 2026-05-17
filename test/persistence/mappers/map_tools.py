"""Tools for use with mapper tests"""
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

#TODO: Don't think any of this is actually used...

def get_map_checker(target_mapper):
    """Returns a function that checks whether the given field of the mapped object
    is equal to the expected value."""
    def map_checker(expected_value, field_name):
        return expected_value == getattr(mapped, field_name)

    mapped = target_mapper.map()
    return map_checker

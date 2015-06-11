# Copyright (c) 2015 David Wilson
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

import Genre as genre
import Platform as platform


#                          (filename, root_element, output_type)xc
_load_types = {"platform": ("Data/SuggestedPlatforms.json", "platforms", platform.Platform),
               "genre": ("Data/Genres.json", "genres", genre.Genre)
}

def _load_data(load_type):
    
    file_name, root_element, output_type = _types[load_type]

    with open(file_name) as f:
        data = json.load(f)
        return [output_type.from_dict(x) for x in data[root_element]]    
    
def load_suggested_platforms():
    return _load_data("platform")

def load_suggested_genres():
    return _load_data("genre")

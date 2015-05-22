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

from Data.DataLoad import DataLoad
from Platform import Platform


class LoadSuggestedPlatforms(DataLoad):
    def __init__(self):
        super().__init__("Data/SuggestedPlatforms.json", "platforms")

    def get(self):
        return [Platform.from_dict(x) for x in self.data]

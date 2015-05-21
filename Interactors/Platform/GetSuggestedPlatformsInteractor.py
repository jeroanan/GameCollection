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

from Interactors.Interactor import Interactor


class GetSuggestedPlatformsInteractor(Interactor):

    def __init__(self, suggested_platforms):
        super().__init__()
        self.__suggested_platforms = suggested_platforms

    def execute(self):
        platforms = list(self.persistence.get_platforms())
        suggested_platforms = self.__suggested_platforms.get()
        result = [p for p in suggested_platforms if p not in platforms]
        return sorted(result, key=lambda x: x.name)

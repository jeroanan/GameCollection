"""Parameters for GetGamesInteractor.execute"""
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
class GetGamesInteractorParams:
    """Parameters for GetGamesInteractor.execute"""
    sort_field: str = field(default="title")
    sort_direction: str = field(default="ASC")
    number_of_games: int = field(default=999999)
    platform: str = field(default=None)
    user_id: str = field(default="")

    #TOO: Cleanup, unify
    @staticmethod
    def from_dict(dictionary):
        """Initialise an instance of GetGamesInteractorParams from a dictionary.
        :param dictionary: A dictionary containing the following keys:
           * number_of_games
           * sort_field
           * sort_direction
           * user_id
           * platform
        :returns: An instance of GetGamesInteractorParams with its properties set.
                  Where a key is missing from dictionary, the corresponding property will
                  left as its default."""
        params = GetGamesInteractorParams()
        params.number_of_games = dictionary.get("number_of_games", params.number_of_games)
        params.sort_field = dictionary.get("sort_field", params.sort_field)
        params.sort_direction = dictionary.get("sort_direction", params.sort_direction)
        params.user_id = dictionary.get("user_id", params.user_id)
        params.platform = dictionary.get("platform", params.platform)
        return params

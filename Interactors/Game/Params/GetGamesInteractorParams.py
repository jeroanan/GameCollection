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

class GetGamesInteractorParams(object):
    """Parameters for GetGamesInteractor.execute"""

    def __init__(self):
        """Initialise object state"""
        self.__sort_field = "title"
        self.__sort_direction = "ASC"
        self.__number_of_games = 999999
        self.__platform = None
        self.__user_id = ""

    @property
    def sort_field(self):
        """Get the field to sort games by"""
        return self.__sort_field

    @sort_field.setter
    def sort_field(self, val):
        """Set the field to sort games by"""
        self.__sort_field=val

    @property
    def sort_direction(self):
        """Get the direction to sort games in"""
        return self.__sort_direction

    @sort_direction.setter
    def sort_direction(self, val):
        """Set the direction to sort games in"""
        self.__sort_direction = val

    @property
    def number_of_games(self):
        """Get the number of games to be retrieved"""
        return self.__number_of_games

    @number_of_games.setter
    def number_of_games(self, val):
        """Set the number of games to be retrieved"""
        self.__number_of_games = val

    @property
    def platform(self):
        """Get the platform to retrieve games for"""
        return self.__platform

    @platform.setter
    def platform(self, val):
        """Set the platform to retrieve games for"""
        self.__platform = val

    @property
    def user_id(self):
        """Get the user id to retrieve games for"""
        return self.__user_id

    @user_id.setter
    def user_id(self, val):
        """Set the user id to retrieve games for"""
        self.__user_id = val

    def __eq__(self, other):
        """Test that this instance of GetGamesInteractor is equal to another.
        This is done by comparing the following properties:
           * sort_field
           * sort_direction
           * number_of_games
           * platform
        :returns: True if this instance of GetGamesInteractor matches other. False otherwise."""
        return (self.sort_field == other.sort_field and
                self.sort_direction == other.sort_direction and
                self.number_of_games == other.number_of_games and
                self.platform == other.platform)

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

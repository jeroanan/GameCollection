"""Methods for Persistence classes to implement"""

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

from typing import Protocol

from game import Game
from genre import Genre
from hardware import Hardware
from hardware_type import HardwareType
from icarus_platform import Platform
from interactors.params.get_games_interactor_params import GetGamesInteractorParams
from interactors.params.get_hardware_list_interactor_params import GetHardwareListInteractorParams
from icarus_user import User

class AbstractPersistence(Protocol):
    """Provides a list of methods for persistence objects to implement."""

    #Games

    def add_game(self, game: Game, user_id: str) -> None:
        """Add a single game.
        :param params: The game to add
        :param user_id: The id of the current user (actual id rather than username)
        :returns: None
        """

    def count_games(self, user_id: str) -> int:
        """Counts the games in the user's collection.
        :param user_id: The uuid of the current user.
        :returns: The number of games in the user's collection
        """

    def delete_game(self, game: Game, user_id: str) -> None:
        """Delete the given game if it belongs to the given user
        :param game: the game to be deleted
        :param user_id: A string containing the uuid of the given user
        :returns: None
        """

    def get_all_games(self, params: GetGamesInteractorParams) -> list[Game]:
        """Gets a list of games.
        :param params: An object of type GetGamesInteractorParams
        :returns: A list of Game
        """

    def get_all_games_for_platform(self, params: GetGamesInteractorParams) -> list[Game]:
        """Gets a list of games for a platform.
        :param params: The parameters
        :returns: A list of Game
        """

    def get_game(self, game_id: str, user_id: str) -> Game:
        """Gets a specific game if it matches the given user
        :param game_id: The uuid of the game
        :param user_id: The uuid of the given user
        :returns: The matching game
        """

    def update_game(self, game: Game, user_id: str) -> None:
        """Update the given game if it belongs to the given user
        :param game: The game to be updated
        :param user_id: The uuid of the given user
        :returns: None
        """

    #Genres

    def add_genre(self, genre: Genre) -> None:
        """Add a genre
        :param genre: The genre to be added.
        """

    def delete_genre(self, genre_id: str) -> None:
        """Delete a genre.
        :param genre_id: The ObjectId of the genre to be deleted.
        :returns: None
        """

    def get_genre_details(self, genre_id: str) -> Genre:
        """Get the details of a genre.
        :param genre_id: The object id of the genre to be retrieved.
        :returns: The matching genre.
        """

    def get_genres(self) -> list[Genre]:
        """Get all genres.
        :returns: All genres in the system.
        """

    def update_genre(self, genre: Genre) -> None:
        """Update the details of a genre
        :param genre: The genre to be updated.
        """

    #Hardware

    def add_hardware_type(self, hardware_type: HardwareType) -> None:
        """Add a hardware type.
        :param hardware_type: The hardware type to add.
        """

    def count_hardware(self, user_id: str) -> int:
        """Counts the items of hardware in the user's collection
        :param user_id: The uuid of the current user.
        :returns: The number of items of hardware
        """

    def count_hardware_types(self) -> int:
        """Counts the number of hardware types in the system
        :returns: The number of hardware types in the system
        """

    def delete_hardware(self, hardware_id: str, user_id: str) -> None:
        """Delete the given item of hardware.
        :param hardware_id: The uuid of the item of hardware to be deleted
        :param user_id: The uuid of the current user
        """

    def delete_hardware_type(self, hardware_type: HardwareType) -> None:
        """Delete the given hardware type.
        :param hardware_type: The hardware type to be deleted
        """

    def get_hardware_details(self, platform_id: str, user_id: str) -> Hardware:
        """Gets the details of a specific item of hardware.
        param hardware_id: The uuid of the item of hardware to retrieve.
        param user_id: The uuid of the current user.
        returns: An instance of Hardware containing the requested item of hardware.
        """

    def get_hardware_list(self, params: GetHardwareListInteractorParams) -> list[Hardware]:
        """Get a list of all hardware in the user's collection
        param params: The search parameters
        returns: The list of hardware
        """
        #TODO: Is this superfluous? do we need just a search_hardware type?

    def get_hardware_list_for_platform(self, params: GetHardwareListInteractorParams) -> list[Hardware]:
        """Get a list of all hardware for a platform in the user's collection
        :param params: An instance of GetHardwareListInteractorParams
        :returns: A list of instances of Hardware
        """
        #TODO: Is this superfluous? do we need just a search_hardware type?

    def get_hardware_type(self, hardware_type: HardwareType) -> HardwareType:
        """Get a specific hardware type record.
        :param hardware_type: An instance of HardwareType. The hardware type to get.
        :returns: An instance of HardwareType. The requested hardware type.
        """

    def get_hardware_types_list(self) -> list[HardwareType]:
        """Gets the list of hardware types
        :returns: A list of objects of type HardwareType containing the list of hardware.
        """

    def save_hardware(self, hardware: Hardware, user_id: str) -> None:
        """Save an item of hardware.
        :param hardware: An instance of Hardware. The item of hardware to be saved.
        :param user_id: The uuid of the user whose collection the item of hardware should be added
                        to.
        :returns: None
        """

    def update_hardware(self, hardware: Hardware, user_id: str) -> None:
        """Update the given item of hardware
        :param hardware: An instance of Hardware. The item of hardware to be updated.
        :param user_id: The uuid of the current user.
        :returns: None
        """

    def update_hardware_type(self, hardware_type: HardwareType) -> None:
        """Update the given hardware type
        :param hardware_type: The hardware type to be updated
        """

    #Platforms

    def add_platform(self, platform: Platform) -> None:
        """Add a platform
        :param platform: An object of type platform. The platform to be added.
        """

    def delete_platform(self, platform: str) -> None:
        """Delete a platform
        :param platform: The id of the platform to be deleted
        """

    def get_platform(self, platform_id: str) -> Platform:
        """Get a platform
        :param platform_id: The uuid of a platform
        :returns: an object of type platform containing the requested platform
        """

    def get_platforms(self) -> list[Platform]:
        """Get a list of platforms
        :returns: A list of type Platform of all stored platforms
        """

    def update_platform(self, platform: Platform) -> None:
        """Update the details of a platform
        :param platform: An object of type platform. The platform to be updated.
        """

    #Search

    def search(self, search_term: str, sort_field: str, sort_dir: str, user_id: str) -> list[Game]:
        """Search the games collection
        :param search_term: The term to do the search upon
        :param sort_field: The field to sort results by
        :param sort_dir: The direction to sort results in
        :param user_id: The uuid of the current user
        :returns: the search results
        """

    #Users

    def add_user(self, user: User) -> None:
        """Add a user
        :param user: An object of type User. The user to add.
        """

    def change_password(self, user: User) -> None:
        """Change a user's password
        :param user: An object of type user. The user whose password is to be changed.
        The password property is the new password.
        """

    def delete_user(self, user: User) -> None:
        """Delete a user
        :param user: An object of type user. Contains the id of the user to be deleted.
        """

    def get_all_users(self) -> list[User]:
        """Get all users
        :returns: A list of User. All users.
        """

    def get_user(self, user: User) -> User:
        """Get a user
        :param user: An object of type User. The user to get.
        :returns: An object of type User. The desired user.
        """

    def update_user(self, user: User) -> None:
        """Update the details of a user
        :param user: An object of type User. The id field is set to the id of the user to update.
                     The rest of the fields contain the new values.
        """

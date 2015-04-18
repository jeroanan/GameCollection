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

# Provides a list of methods for persistence objects to implement.
class AbstractPersistence(object):

    """Add a single game.
    :param params: An object of type Game
    :param user_id: The id of the current user (actual id rather than username)
    :returns: None
    """
    def add_game(self, game, user_id):
        pass

    """Gets a list of games.
    :param params: An object of type GetGamesInteractorParams
    :returns: A list of Game
    """
    def get_all_games(self, params):
        pass

    """Gets a list of games for a platform.
    :param params: An object of type GetGamesInteractorParams
    :returns: A list of Game
    """
    def get_all_games_for_platform(self, params):
        pass
    
    """Counts the games in the user's collection.
    :param user_id: The uuid of the current user.
    :returns: The number of games in the user's collection
    """
    def count_games(self, user_id):
        pass

    """Counts the items of hardware
    :returns: The number of items of hardware
    """
    def count_hardware(self):
        pass

    """Gets a specific game if it matches the given user
    :param game_id: A string containing the uuid of the game
    :param user_id: A string containing the uuid of the given user
    :returns: An object of type Game
    """
    def get_game(self, game_id, user_id):
        pass

    """Get a list of platforms
    :returns: A list of type Platform of all stored platforms
    """
    def get_platforms(self):
        pass

    """Get a platform
    :param platform_id: The uuid of a platform
    :returns: an object of type platform containing the requested platform
    """
    def get_platform(self, platform_id):
        pass

    """Add a platform
    :param platform: An object of type platform. The platform to be added.
    """
    def add_platform(self, platform):
        pass

    """Update the details of a platform
    :param platform: An object of type platform. The platform to be updated.
    """
    def update_platform(self, platform):
        pass

    """Delete a platform
    :param platform: An object of type platform. The platform to be deleted.
    """
    def delete_platform(self, platform):
        pass

    """Update the given game if it belongs to the given user
    :param game_id: An object of type Game -- the game to be updated
    :param user_id: A string containing the uuid of the given user
    :returns: None
    """
    def update_game(self, game):
        pass

    """Delete the given game if it belongs to the given user
    :param game_id: An object of type Game -- the game to be deleted
    :param user_id: A string containing the uuid of the given user
    :returns: None
    """
    def delete_game(self, game, user_id):
        pass

    """Get a list of all hardware in the user's collection
    param sort_field: The field to sort the hardware on
    param sort_direction: The order to sort the hardware in
    param user_id: The uuid of the user
    returns: A list of instances of Hardware 
    """
    def get_hardware_list(self, sort_field, sort_direction, user_id):
        pass

    """Gets the details of a specific item of hardware.
    param hardware_id: The uuid of the item of hardware to retrieve.
    param user_id: The uuid of the current user.
    returns: An instance of Hardware containing the requested item of hardware.
    """
    def get_hardware_details(self, platform_id, user_id):
        pass

    """Save an item of hardware.
    param hardware: An instance of Hardware. The item of hardware to be saved.
    param user_id: The uuid of the user whose collection the item of hardware should be added to.
    returns: None
    """
    def save_hardware(self, hardware, user_id):
        pass

    """Update the given item of hardware
    param hardware: An instance of Hardware. The item of hardware to be updated.
    param user_id: The uuid of the current user.
    returns: None
    """
    def update_hardware(self, hardware, user_idx):
        pass

    """Delete the given item of hardware.
    param hardware_id: The uuid of the item of hardware to be deleted
    param user_id: The uuid of the current user
    """
    def delete_hardware(self, hardware_id, user_id):
        pass

    def get_genres(self):
        pass

    def add_genre(self, genre):
        pass

    def get_genre_details(self, genre_id):
        pass

    def update_genre(self, genre):
        pass

    def delete_genre(self, genre_id):
        pass

    """Search the games collection
    param search_term: The term to do the search upon
    param sort_field: The field to sort results by
    param sort_dir: The direction to sort results in
    param user_id: The uuid of the current user
    returns: the search results
    """
    def search(self, search_term, sort_field, sort_dir, user_id):
        pass

    """Get a user
    :param: An object of type User. The user to get.
    :returns: An object of type User. The desired user.
    """
    def get_user(self, user):
        pass

    """Add a user
    :param: An object of type User. The user to add.xs
    """
    def add_user(self, user):
        pass

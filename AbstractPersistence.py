"""Methods for Persistence classes to implement"""

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


class AbstractPersistence(object):
    """Provides a list of methods for persistence objects to implement."""

    #Games

    def add_game(self, game, user_id):
        """Add a single game.
        :param params: An object of type Game
        :param user_id: The id of the current user (actual id rather than username)
        :returns: None
        """
        pass

    def count_games(self, user_id):
        """Counts the games in the user's collection.
        :param user_id: The uuid of the current user.
        :returns: The number of games in the user's collection
        """
        pass

    def delete_game(self, game, user_id):
        """Delete the given game if it belongs to the given user
        :param game_id: An object of type Game -- the game to be deleted
        :param user_id: A string containing the uuid of the given user
        :returns: None
        """
        pass

    def get_all_games(self, params):
        """Gets a list of games.
        :param params: An object of type GetGamesInteractorParams
        :returns: A list of Game
        """
        pass    

    def get_all_games_for_platform(self, params):
        """Gets a list of games for a platform.
        :param params: An object of type GetGamesInteractorParams
        :returns: A list of Game
        """
        pass    

    def get_game(self, game_id, user_id):
        """Gets a specific game if it matches the given user
        :param game_id: A string containing the uuid of the game
        :param user_id: A string containing the uuid of the given user
        :returns: An object of type Game
        """
        pass

    def update_game(self, game):
        """Update the given game if it belongs to the given user
        :param game_id: An object of type Game -- the game to be updated
        :param user_id: A string containing the uuid of the given user
        :returns: None
        """
        pass

    #Genres

    def add_genre(self, genre):
        """Add a genre
        :param genre: An object of type Genre. The genre to be added.
        """
        pass    

    def delete_genre(self, genre_id):
        """Delete a genre.
        :param genre_id: The ObjectId of the genre to be deleted.
        :returns: None
        """
        pass

    def get_genre_details(self, genre_id):
        """Get the details of a genre.
        :param genre_id: The object id of the genre to be retrieved.
        :returns: An object of type Genre containing the genre.
        """
        pass

    def get_genres(self):
        """Get all genres.
        :returns: A list of type Genre that contains all genres in the system.
        """
        pass

    def update_genre(self, genre):
        """Update the details of a genre
        :param genre: An object of type genre. The genre to be updated.
        """
        pass

    #Hardware

    def add_hardware_type(self, hardware_type):
        """Add a hardware type.
        :param hardware_type: An object of type HardwareType. The hardware type to add.
        """
        pass

    def count_hardware(self, user_id):
        """Counts the items of hardware in the user's collection
        :param user_id: The uuid of the current user.
        :returns: The number of items of hardware
        """
        pass

    def count_hardware_types(self):
        """Counts the number of hardware types in the system
        :returns: The number of hardware types in the system
        """
        pass

    def delete_hardware(self, hardware_id, user_id):
        """Delete the given item of hardware.
        :param hardware_id: The uuid of the item of hardware to be deleted
        :param user_id: The uuid of the current user
        """
        pass
    
    def delete_hardware_type(self, hardware_type):
        """Delete the given hardware type.
        :param hardware_type: The hardware type to be deleted
        """
        pass

    def get_hardware_details(self, platform_id, user_id):
        """Gets the details of a specific item of hardware.
        param hardware_id: The uuid of the item of hardware to retrieve.
        param user_id: The uuid of the current user.
        returns: An instance of Hardware containing the requested item of hardware.
        """
        pass

    def get_hardware_list(self, params):
        """Get a list of all hardware in the user's collection
        param params: An instance of GetHardwareListInteractorParams
        returns: A list of instances of Hardware
        """
        pass

    def get_hardware_list_for_platform(self, params):
        """Get a list of all hardware for a platform in the user's collection
        :param params: An instance of GetHardwareListInteractorParams
        :returns: A list of instances of Hardware
        """
        pass  

    def get_hardware_type(self, hardware_type):
        """Get a specific hardware type record.
        :param hardware_type: An instance of HardwareType. The hardware type to get.
        :return: An instance of HardwareType. The requested hardware type.
        """
        pass

    def get_hardware_types_list(self):
        """Gets the list of hardware types
        :returns: A list of objects of type HardwareType containing the list of hardware.
        """
        pass

    def save_hardware(self, hardware, user_id):
        """Save an item of hardware.
        :param hardware: An instance of Hardware. The item of hardware to be saved.
        :param user_id: The uuid of the user whose collection the item of hardware should be added
                        to.
        :returns: None
        """
        pass

    def update_hardware(self, hardware, user_idx):
        """Update the given item of hardware
        :param hardware: An instance of Hardware. The item of hardware to be updated.
        :param user_id: The uuid of the current user.
        :returns: None
        """
        pass

    def update_hardware_type(self, hardware_type):
        """Update the given hardware type
        :param hardware_type: The hardware type to be updated
        """
        pass

    #Platforms

    def add_platform(self, platform):
        """Add a platform
        :param platform: An object of type platform. The platform to be added.
        """
        pass

    def delete_platform(self, platform):
        """Delete a platform
        :param platform: An object of type platform. The platform to be deleted.
        """
        pass

    def get_platform(self, platform_id):
        """Get a platform
        :param platform_id: The uuid of a platform
        :returns: an object of type platform containing the requested platform
        """
        pass

    def get_platforms(self):
        """Get a list of platforms
        :returns: A list of type Platform of all stored platforms
        """
        pass    

    def update_platform(self, platform):
        """Update the details of a platform
        :param platform: An object of type platform. The platform to be updated.
        """
        pass

    #Search

    def search(self, search_term, sort_field, sort_dir, user_id):
        """Search the games collection
        :param search_term: The term to do the search upon
        :param sort_field: The field to sort results by
        :param sort_dir: The direction to sort results in
        :param user_id: The uuid of the current user
        :returns: the search results
        """
        pass

    #Users

    def add_user(self, user):
        """Add a user
        :param user: An object of type User. The user to add.
        """
        pass

    def change_password(self, user):
        """Change a user's password
        :param user: An object of type user. The user whose password is to be changed.
        The password property is the new password.
        """
        pass

    def delete_user(self, user):
        """Delete a user
        :param user: An object of type user. Contains the id of the user to be deleted.
        """
        pass

    def get_all_users(self):
        """Get all users
        :returns: A list of User. All users.
        """
        pass

    def get_user(self, user):
        """Get a user
        :param user: An object of type User. The user to get.
        :returns: An object of type User. The desired user.
        """
        pass    

    def update_user(self, user):
        """Update the details of a user
        :param user: An object of type User. The id field is set to the id of the user to update.
                     The rest of the fields contain the new values.
        """
        pass

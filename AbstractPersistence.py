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

    def count_games(self):
        pass

    def count_hardware(self):
        pass

    """Gets a specific game if it matches the given user
    :param game_id: A string containing the uuid of the game
    :param user_id: A string containing the uuid of the given user
    :returns: An object of type Game
    """
    def get_game(self, game_id, user_id):
        pass

    def get_platforms(self):
        pass

    def get_platform(self, platform_id):
        pass

    def add_platform(self, platform):
        pass

    def update_platform(self, platform):
        pass

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

    def get_hardware_details(self, platform_id):
        pass

    def save_hardware(self, hardware):
        pass

    def update_hardware(self, hardware):
        pass

    def delete_hardware(self, hardware_id):
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

    def search(self, search_term, sort_field, sort_dir):
        pass

    def get_user(self, user):
        pass

    def add_user(self, user):
        pass

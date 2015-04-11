class AbstractPersistence(object):

    def add_game(self, game):
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

    def get_game(self, game_id):
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

    def update_game(self, game):
        pass

    def delete_game(self, game):
        pass

    def get_hardware_list(self, sort_field, sort_direction):
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

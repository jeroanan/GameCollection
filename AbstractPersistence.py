

class AbstractPersistence(object):

    def add_game(self, game):
        pass

    def get_all_games(self):
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

    def get_hardware_list(self):
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

    def delete_genre(self, genrre_id):
        pass
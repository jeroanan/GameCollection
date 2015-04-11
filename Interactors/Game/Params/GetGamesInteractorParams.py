class GetGamesInteractorParams(object):
    
    def __init__(self):
        self.__sort_field = ""
        self.__sort_direction = "ASC"
        self.__number_of_games = 999999
        self.__platform = None
        self.__user_id = ""

    @property
    def sort_field(self):
        return self.__sort_field

    @sort_field.setter
    def sort_field(self, val):
        self.__sort_field=val

    @property
    def sort_direction(self):
        return self.__sort_direction

    @sort_direction.setter
    def sort_direction(self, val):
        self.__sort_direction = val

    @property
    def number_of_games(self):
        return self.__number_of_games

    @number_of_games.setter
    def number_of_games(self, val):
        self.__number_of_games = val

    @property
    def platform(self):
        return self.__platform

    @platform.setter
    def platform(self, val):
        self.__platform = val

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, val):
        self.__user_id = val
    
    def __eq__(self, other):
        return (self.sort_field == other.sort_field and 
                self.sort_direction == other.sort_direction and 
                self.number_of_games == other.number_of_games and 
                self.platform == other.platform)

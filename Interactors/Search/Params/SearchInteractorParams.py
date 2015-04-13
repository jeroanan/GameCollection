class SearchInteractorParams(object):

    def __init__(self):
        self.__search_term = ""
        self.__sort_field = ""
        self.__sort_direction = ""
        self.__user_id = ""

    @property
    def search_term(self):
        return self.__search_term

    @search_term.setter
    def search_term(self, val):
        self.__search_term = val

    @property
    def sort_field(self):
        return self.__sort_field

    @sort_field.setter
    def sort_field(self, val):
        self.__sort_field = val

    @property
    def sort_direction(self):
        return self.__sort_direction

    @sort_direction.setter
    def sort_direction(self, val):
        self.__sort_direction = val
    
    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, val):
        self.__user_id = val

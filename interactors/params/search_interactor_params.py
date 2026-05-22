"""Class to hold parameters for SearchInteractor"""
class SearchInteractorParams:
    """Class to hold parameters for SearchInteractor"""

    def __init__(self):
        self.__search_term = ""
        self.__sort_field = ""
        self.__sort_direction = ""
        self.__user_id = ""

    @property
    def search_term(self):
        """Get the search term to search for"""
        return self.__search_term

    @search_term.setter
    def search_term(self, val):
        self.__search_term = val

    @property
    def sort_field(self):
        """Get the field to sort search results by"""
        return self.__sort_field

    @sort_field.setter
    def sort_field(self, val):
        self.__sort_field = val

    @property
    def sort_direction(self):
        """Get the direction to sort search results in"""
        return self.__sort_direction

    @sort_direction.setter
    def sort_direction(self, val):
        self.__sort_direction = val

    @property
    def user_id(self):
        """Get the user_id to retrieve games for"""
        return self.__user_id

    @user_id.setter
    def user_id(self, val):
        self.__user_id = val

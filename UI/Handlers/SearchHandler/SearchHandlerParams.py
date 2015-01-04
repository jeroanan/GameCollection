class SearchHandlerParams(object):

    def __init__(self):
        self.__search_term = ""
        self.__sort_field = ""
        self.__sort_direction = ""

    @property
    def search_term(self):
        return self.__search_term

    @search_term.setter
    def search_term(self, value):
        self.__search_term = value

    @property
    def sort_field(self):
        return self.__sort_field

    @sort_field.setter
    def sort_field(self, value):
        self.__sort_field = value

    @property
    def sort_direction(self):
        return self.__sort_direction

    @sort_direction.setter
    def sort_direction(self, value):
        self.__sort_direction = value

    def __eq__(self, other):
        return (self.search_term == other.search_term and self.sort_field == other.sort_field and
                self.sort_direction == other.sort_direction)
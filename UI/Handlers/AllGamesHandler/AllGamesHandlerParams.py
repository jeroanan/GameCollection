class AllGamesHandlerParams(object):

    def __init__(self):
        self.__sort_field = ""
        self.__sort_direction = ""
        self.__platform = ""

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

    @property
    def platform(self):
        return self.__platform

    @platform.setter
    def platform(self, value):
        self.__platform = value

    def __eq__(self, other):
        return (self.sort_field == other.sort_field and self.sort_direction == other.sort_direction and
                self.platform == other.platform)
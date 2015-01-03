class IndexHandlerParams(object):
    def __init__(self):
        self.__game_sort = None
        self.__game_sort_direction = None
        self.__hardware_sort = None
        self.__hardware_sort_direction = None

    @property
    def game_sort(self):
        return self.__game_sort

    @game_sort.setter
    def game_sort(self, value):
        self.__game_sort = value

    @property
    def game_sort_direction(self):
        return self.__game_sort_direction

    @game_sort_direction.setter
    def game_sort_direction(self, value):
        self.__game_sort_direction = value

    @property
    def hardware_sort(self):
        return self.__hardware_sort

    @hardware_sort.setter
    def hardware_sort(self, value):
        self.__hardware_sort = value

    @property
    def hardware_sort_direction(self):
        return self.__hardware_sort_direction

    @hardware_sort_direction.setter
    def hardware_sort_direction(self, value):
        self.__hardware_sort_direction = value

    def __eq__(self, other):
        return (self.game_sort == other.game_sort and self.game_sort_direction == other.game_sort_direction and
                self.hardware_sort == other.hardware_sort and
                self.hardware_sort_direction == other.hardware_sort_direction)
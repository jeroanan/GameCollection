class AddPlatformHandlerParams(object):

    def __init__(self):
        self.__name = ""
        self.__description = ""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    def __eq__(self, other):
        return self.name == other.name and self.description == other.description
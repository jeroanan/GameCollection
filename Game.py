class Game(object):

    def __init__(self):
        self.__id = ""
        self.__title = ""
        self.__platform = ""
        self.__num_copies = 0
        self.__num_boxed = 0
        self.__num_manuals = 0
        self.__notes = ""

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def platform(self):
        return self.__platform

    @platform.setter
    def platform(self, value):
        self.__platform = value

    @property
    def num_copies(self):
        return self.__num_copies

    @num_copies.setter
    def num_copies(self, value):
        self.__num_copies = value

    @property
    def num_boxed(self):
        return self.__num_boxed

    @num_boxed.setter
    def num_boxed(self, value):
        self.__num_boxed = value

    @property
    def num_manuals(self):
        return self.__num_manuals

    @num_manuals.setter
    def num_manuals(self, value):
        self.__num_manuals = value

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, value):
        self.__notes = value
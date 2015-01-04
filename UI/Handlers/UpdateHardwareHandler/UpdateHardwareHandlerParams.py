class UpdateHardwareHandlerParams(object):

    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__platform = ""
        self.__num_owned = ""
        self.__num_boxed = ""
        self.__notes = ""

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def platform(self):
        return self.__platform

    @platform.setter
    def platform(self, value):
        self.__platform = value

    @property
    def num_owned(self):
        return self.__num_owned

    @num_owned.setter
    def num_owned(self, value):
        self.__num_owned = value

    @property
    def num_boxed(self):
        return self.__num_boxed

    @num_boxed.setter
    def num_boxed(self, value):
        self.__num_boxed = value

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, value):
        self.__notes = value

    def __eq__(self, other):
        return (self.id == other.id and self.name == other.name and self.platform == other.platform and
                self.num_owned == other.num_owned and self.num_boxed == other.num_boxed and self.notes == other.notes)
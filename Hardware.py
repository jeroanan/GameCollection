class Hardware():

    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__platform = ""
        self.__num_owned = ""
        self.__num_boxed = ""

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
    def numowned(self):
        return self.__num_owned

    @numowned.setter
    def numowned(self, value):
        self.__num_owned = value

    @property
    def numboxed(self):
        return self.__num_boxed

    @numboxed.setter
    def numboxed(self, value):
        self.__num_boxed = value
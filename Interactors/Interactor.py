class Interactor(object):

    def __init__(self):
        self.__persistence = None

    @property
    def persistence(self):
        return self.__persistence

    @persistence.setter
    def persistence(self, value):
        self.__persistence = value
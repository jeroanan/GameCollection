class Interactor(object):

    def __init__(self):
        self.__gateway = None

    @property
    def games_gateway(self):
        return self.__gateway

    @games_gateway.setter
    def games_gateway(self, value):
        self.__gateway = value
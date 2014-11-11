from Game import Game


class GamesInteractor(object):
    def __init__(self):
        self.__gateway = None

    def get_my_games(self):
        return self.__gateway.get_all_games()

    @property
    def games_gateway(self):
        return self.__gateway

    @games_gateway.setter
    def games_gateway(self, value):
        self.__gateway = value

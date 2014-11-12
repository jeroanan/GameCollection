from Interactors.Interactor import Interactor


class GetGamesInteractor(Interactor):

    def execute(self):
        return self.__persistence.get_all_games()

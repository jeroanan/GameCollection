from Interactors.Interactor import Interactor


class GetGamesInteractor(Interactor):

    def execute(self, number_of_games=999999):
        return self.persistence.get_all_games(number_of_games=number_of_games)

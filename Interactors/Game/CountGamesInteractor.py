from Interactors.Interactor import Interactor


class CountGamesInteractor(Interactor):
    def execute(self):
        return self.persistence.count_games()

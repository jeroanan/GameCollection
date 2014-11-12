from Interactors.Interactor import Interactor


class GetGamesInteractor(Interactor):

    def execute(self):
        return self.persistence.get_all_games()

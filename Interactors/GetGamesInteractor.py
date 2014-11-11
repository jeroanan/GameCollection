from Interactors.Interactor import Interactor


class GetGamesInteractor(Interactor):

    def execute(self, game=None):
        return self.games_gateway.get_all_games()

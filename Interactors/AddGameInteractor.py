from Interactors.Interactor import Interactor


class AddGameInteractor(Interactor):

    def execute(self, game):
        self.games_gateway.add_game(game)

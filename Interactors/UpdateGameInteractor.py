from Interactors.Interactor import Interactor


class UpdateGameInteractor(Interactor):

    def execute(self, game):
        self.persistence.update_game(game)
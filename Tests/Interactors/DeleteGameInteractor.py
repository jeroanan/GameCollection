from Interactors.Interactor import Interactor


class DeleteGameInteractor(Interactor):
    def execute(self, game):
        self.persistence.delete_game(game)

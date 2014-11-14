from Interactors.Interactor import Interactor


class GetGameInteractor(Interactor):

    def execute(self, game_id):
        return self.persistence.get_game(game_id)
from Interactors.Interactor import Interactor


class AddGameInteractor(Interactor):

    def execute(self, game):
        self.__persistence.add_game(game)

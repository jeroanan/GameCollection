from Interactors.Interactor import Interactor


class DeleteGameInteractor(Interactor):

    def execute(self, game):
        self.__validate(game)
        self.persistence.delete_game(game)

    def __validate(self, game):
        if game is None:
            raise TypeError("game")
        if game.id is None or game.id.strip() == "":
            raise ValueError("Game id must be set")

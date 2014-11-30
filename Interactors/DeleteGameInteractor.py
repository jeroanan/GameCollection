from Interactors.Interactor import Interactor


class DeleteGameInteractor(Interactor):

    def execute(self, game):
        self.__validate(game)
        self.persistence.delete_game(game)

    def __validate(self, game):
        if game is None:
            raise TypeError("game")
        self.validate_string_field("Game id", game.id)

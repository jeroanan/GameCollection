from Interactors.Interactor import Interactor


class UpdateGameInteractor(Interactor):

    def execute(self, game):
        self.__validate(game)
        self.persistence.update_game(game)

    def __validate(self, game):
        if game is None:
            raise TypeError("game")
        self.validate_string_field("Game title", game.title)
        self.validate_string_field("Game platform", game.platform)
        self.validate_integer_field("Number of copies", game.num_copies)
        self.validate_integer_field("Number boxed", game.num_boxed)
        self.validate_integer_field("Number of manuals", game.num_manuals)
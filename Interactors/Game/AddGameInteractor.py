from Interactors.Interactor import Interactor


class AddGameInteractor(Interactor):

    def execute(self, game):
        self.__validate(game)
        self.persistence.add_game(game)

    def __validate(self, game):
        if game is None:
            raise TypeError("game")
        self.__validate_game_id(game)
        self.validate_string_field("Game title", game.title)
        self.validate_string_field("Platform", game.platform)
        self.validate_integer_field("Number of copies", game.num_copies)
        self.validate_integer_field("Number of boxed items", game.num_boxed)
        self.validate_integer_field("Number of manuals", game.num_manuals)

    def __validate_game_id(self, game):
        if len(game.id) > 0:
            raise ValueError("Game id must be empty when adding a new game")
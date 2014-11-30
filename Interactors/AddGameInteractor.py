from Interactors.Interactor import Interactor


class AddGameInteractor(Interactor):

    def execute(self, game):
        self.__validate(game)
        self.persistence.add_game(game)

    def __validate(self, game):
        if game is None:
            raise TypeError("game")
        self.__validate_game_id(game)
        self.__validate_game_title(game)
        self.__validate_platform(game)
        self.__validate_num_copies(game)
        self.__validate_num_boxed(game)
        self.__validate_num_manuals(game)

    def __validate_game_id(self, game):
        if len(game.id) > 0:
            raise ValueError("Game id must be empty when adding a new game")

    def __validate_game_title(self, game):
        self.__validate_string_field("Game title", game.title)

    def __validate_platform(self, game):
        self.__validate_string_field("Platform", game.platform)

    def __validate_string_field(self, field_name, field_value):
        if field_value is None or field_value.strip() == "":
            raise ValueError("%s must have a value" % field_name)

    def __validate_num_copies(self, game):
        self.__validate_integer_field("Number of copies", game.num_copies)

    def __validate_num_boxed(self, game):
        self.__validate_integer_field("Number of boxed items", game.num_boxed)

    def __validate_num_manuals(self, game):
        self.__validate_integer_field("Number of manuals", game.num_manuals)

    def __validate_integer_field(self, field_name, field_value):
        if not str(field_value).isdigit():
            raise ValueError("%s must be a number" % field_name)


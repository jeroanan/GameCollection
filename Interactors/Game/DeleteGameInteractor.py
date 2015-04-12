from Interactors.Interactor import Interactor


class DeleteGameInteractor(Interactor):

    """Tell persistence to delete the given game.
    :param game_id: An object of type Game -- the game to be deleted
    :param user_id: A string containing the uuid of the given user
    :returns: None
    """
    def execute(self, game, user_id):
        self.__validate(game)
        self.persistence.delete_game(game, user_id)

    def __validate(self, game):
        if game is None:
            raise TypeError("game")
        self.validate_string_field("Game id", game.id)

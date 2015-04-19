from Interactors.Interactor import Interactor


class GetGameInteractor(Interactor):

    """Gets a specific game from persistence
    :param game_id: The uuid of the game to be retrieved
    :param user_id: The uuid of the current user
    :returns: A game from persistence
    """
    def execute(self, game_id, user_id):
        self.validate_string_field("game id", game_id)
        return self.persistence.get_game(game_id, user_id)

from Interactors.Exceptions.PersistenceException import PersistenceException
from Interactors.Interactor import Interactor


class UpdateGameInteractor(Interactor):

    """Tells persistence to update a game
    :param game: An object of type Game
    :param user_id: The uuid of the current user
    :returns: None
    """
    def execute(self, game, user_id):
        self.__validate(game)
        try:
            self.persistence.update_game(game, user_id)
        except:
            raise PersistenceException

    def __validate(self, game):
        if game is None:
            raise TypeError("game")
        self.validate_string_field("Game title", game.title)
        self.validate_string_field("Game platform", game.platform)
        self.validate_integer_field("Number of copies", game.num_copies)
        self.validate_integer_field("Number boxed", game.num_boxed)
        self.validate_integer_field("Number of manuals", game.num_manuals)

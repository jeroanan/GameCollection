from Game import Game
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class DeleteGameHandler(AuthenticatedHandler):

    """Handles Game Deletion requests.
    This is really intended to be used as an ajax request rather than a webpage, so
    it doesn't give much in the way of user feedback. If the user is not currently logged
    in then it will redirect to the homepage.
    :param args: A dictionary containing the key "gameid". gameid contains the uuid of the game to be deleted.
    :returns: If gameid is not present in args then an empty string is returned. Else None is returned.
    """
    def get_page(self, args):
        super().get_page(args)
        if not self.validate_params(args, ["gameid"]):
            return ""
        game = self.__get_game(args)
        self.__execute_interactor(game)

    def __get_game(self, args):
        game = Game()
        game.id = args.get("gameid", "")
        return game

    def __execute_interactor(self, game):
        interactor = self.interactor_factory.create("DeleteGameInteractor")
        interactor.execute(game, self.session.get_value("user_id"))

from Game import Game
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class DeleteGameHandler(AuthenticatedHandler):

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
        interactor.execute(game)

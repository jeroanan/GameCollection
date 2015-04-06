from Game import Game
from UI.Handlers.Handler import Handler


class DeleteGameHandler(Handler):

    def get_page(self, args):
        self.check_session()
        self.redirect_if_not_logged_in()
        if not self.__validate_args(args):
            return ""
        game = self.__get_game(args)
        self.__execute_interactor(game)

    def __validate_args(self, args):
        return args.get("gameid", "") != ""

    def __get_game(self, args):
        game = Game()
        game.id = args.get("gameid", "")
        return game

    def __execute_interactor(self, game):
        interactor = self.interactor_factory.create("DeleteGameInteractor")
        interactor.execute(game)

from Game import Game
from UI.Handlers.Handler import Handler


class DeleteGameHandler(Handler):

    def get_page(self, args):
        game = self.__get_game(args)
        self.__execute_interactor(game)

    def __get_game(self, args):
        game = Game()
        game.id = args.get("gameid", "")
        return game

    def __execute_interactor(self, game):
        interactor = self.interactor_factory.create("DeleteGameInteractor")
        interactor.execute(game)

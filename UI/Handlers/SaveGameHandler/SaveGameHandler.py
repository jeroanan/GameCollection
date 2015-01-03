import cherrypy
from Game import Game
from UI.Handlers.Handler import Handler


class SaveGameHandler(Handler):

    def get_page(self, params):
        interactor = self.interactor_factory.create("AddGameInteractor")
        interactor.execute(game=(self.__get_game(params)))
        raise cherrypy.HTTPRedirect("/")

    def __get_game(self, params):
        game = Game()
        game.title = params.title
        game.num_copies = params.num_copies
        game.num_boxed = params.num_boxed
        game.num_manuals = params.num_manuals
        game.platform = params.platform
        game.notes = params.notes
        return game

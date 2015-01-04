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
        game.title = params.get("title", "")
        game.num_copies = params.get("numcopies", 0)
        game.num_boxed = params.get("numboxed", 0)
        game.num_manuals = params.get("nummanuals", 0)
        game.platform = params.get("platform", 0)
        game.notes = params.get("notes")
        return game

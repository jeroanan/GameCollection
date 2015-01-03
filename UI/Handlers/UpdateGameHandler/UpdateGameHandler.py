import cherrypy
from Game import Game
from UI.Handlers.Handler import Handler


class UpdateGameHandler(Handler):

    def get_page(self, params):
        interactor = self.interactor_factory.create("UpdateGameInteractor")
        game = Game()
        game.id = id
        game.title = params.title
        game.num_copies = params.num_copies
        game.num_boxed = params.num_boxed
        game.num_manuals = params.num_manuals
        game.platform = params.platform
        game.notes = params.notes
        interactor.execute(game=game)
        raise cherrypy.HTTPRedirect("/")
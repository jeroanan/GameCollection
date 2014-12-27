import cherrypy
from Game import Game
from UI.Handlers.Handler import Handler


class UpdateGameHandler(Handler):

    def get_page(self, id, title, numcopies, numboxed, nummanuals, platform, notes):
        interactor = self.interactor_factory.create("UpdateGameInteractor")
        game = Game()
        game.id = id
        game.title = title
        game.num_copies = numcopies
        game.num_boxed = numboxed
        game.num_manuals = nummanuals
        game.platform = platform
        game.notes = notes
        interactor.execute(game)
        raise cherrypy.HTTPRedirect("/")
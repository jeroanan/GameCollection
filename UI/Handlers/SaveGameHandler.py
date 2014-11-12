import cherrypy
from Game import Game
from UI.Handlers.Handler import Handler


class SaveGameHandler(Handler):

    def get_page(self, title, numcopies, numboxed, nummanuals, platform=None):
        interactor = self.interactor_factory.create("AddGameInteractor")
        game = Game()
        game.title = title
        game.num_copies = numcopies
        game.num_boxed = numboxed
        game.num_manuals = nummanuals
        game.platform = platform
        interactor.execute(game)
        raise cherrypy.HTTPRedirect("/")

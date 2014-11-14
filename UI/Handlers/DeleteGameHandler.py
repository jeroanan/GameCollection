import cherrypy
from Game import Game
from UI.Handlers.Handler import Handler


class DeleteGameHandler(Handler):

    def get_page(self, gameid):
        game = Game()
        game.id = gameid
        interactor = self.interactor_factory.create("DeleteGameInteractor")
        interactor.execute(game)
        raise cherrypy.HTTPRedirect("/")

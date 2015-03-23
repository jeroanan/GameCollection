import cherrypy
from Game import Game
from UI.Handlers.Handler import Handler


class SaveGameHandler(Handler):

    def get_page(self, params):
        interactor = self.interactor_factory.create("AddGameInteractor")
        interactor.execute(game=(self.__get_game(params)))

    def __get_game(self, params):
        game = Game()
        game.title = params.get("title", "")
        game.num_copies = params.get("numcopies", 0)
        game.num_boxed = params.get("numboxed", 0)
        game.num_manuals = params.get("nummanuals", 0)
        game.platform = params.get("platform", 0)
        game.notes = params.get("notes")
        game.date_purchased = params.get("datepurchased")
        game.approximate_date_purchased = self.__is_approximate_purchase_date(params)
        return game

    def __is_approximate_purchase_date(self, params):
        return params.get("approximatepurchaseddate") == "true"
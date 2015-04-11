from Game import Game
from Interactors.Exceptions.PersistenceException import PersistenceException
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class UpdateGameHandler(AuthenticatedHandler):

    def get_page(self, params):
        super().get_page(params)
        if not self.validate_params(params, ["title", "platform"]):
            return ""        
        if not self.__execute_interactor(params):
            return ""           

    def __execute_interactor(self, params):
        try:
            interactor = self.interactor_factory.create("UpdateGameInteractor")
            game = self.__get_game(params)
            interactor.execute(game=game)
            return True
        except PersistenceException:
            return False

    def __get_game(self, params):
        game = Game()
        game.id = params.get("id", "")
        game.title = params.get("title", "")
        game.num_copies = params.get("numcopies", 0)
        game.num_boxed = params.get("numboxed", 0)
        game.num_manuals = params.get("nummanuals", 0)
        game.platform = params.get("platform", "")
        game.notes = params.get("notes", "")
        game.date_purchased = params.get("datepurchased", "")
        game.approximate_date_purchased = self.__is_approximate_purchase_date(params)
        return game

    def __is_approximate_purchase_date(self, params):
        return params.get("approximatepurchaseddate") == "true"

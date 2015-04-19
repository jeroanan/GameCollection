from Game import Game
from Interactors.Exceptions.PersistenceException import PersistenceException
from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class UpdateGameHandler(AuthenticatedHandler):

    """Handles Game Update requests.
    This is really intended to be used as an ajax request rather than a webpage, so
    it doesn't give much in the way of user feedback. If the user is not currently logged
    in then it will redirect to the homepage.
    :param params -- A dictionary representation of a game object. It contains the following keys:
           + id -- the uuid of the game to be updated
           + title -- the title of the game to be updated (mandatory)
           + platform -- the platform of the game to be updated (mandatory)
           + numcopies -- the number of copies of the game
           + numboxed -- the number of boxed copies of the game
           + nummanuals -- the number of manuals owned for the game
           + notes -- any additional notes from the user
           + datepurchased -- the date the game was purchased
           + approximate_date_purchased -- a flag indicating whether the purchase date is approximate
    :returns: If one of the mandatory entries in params is missing or there is a problem saving then an empty
              string. Else return None.
    """
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
            interactor.execute(game=game, user_id=self.session.get_value("user_id"))
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

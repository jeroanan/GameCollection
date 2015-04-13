from Interactors.Interactor import Interactor


class CountGamesInteractor(Interactor):

    """Gets the count of games in the user's collection from persistence
    param user_id: The uuid of the user
    returns: The number of games in the user's collection
    """
    def execute(self, user_id):
        return self.persistence.count_games(user_id)

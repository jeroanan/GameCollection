from Interactors.Interactor import Interactor


class GetGamesInteractor(Interactor):

    """Gets a list of games from persistence. If a platform is specified
    then get games for that platform, else get games for all platforms.
    :param params: An object of type GetGamesInteractorParams
    :returns: A list of Game
    """
    def execute(self, params):
        self.validate_string_field("User Id", params.user_id)
        if params.platform == "" or params.platform is None:
            return self.persistence.get_all_games(params)

        return self.persistence.get_all_games_for_platform(params)

